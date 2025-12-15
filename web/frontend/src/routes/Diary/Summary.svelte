<script lang="ts">
import fastapi from '../../lib/api.js'
import Top from '../../lib/Top.svelte'
import MenuTitle from '../../lib/MenuTitle.svelte'
import ParaDeco from '../../lib/ParaDeco.svelte';
import logo_summary from '../../assets/summary.svg'

let diaries = $state({}); // local state variable
let plants = $state({}); // local state variable
let filteredDiaries = $state({}); // local state variable
let selectedPlantId = "";
////////////////////////

function get_diary(){
  fastapi('get', `/diary`, {},
    (response) => {
        diaries = response["data"];
        get_plant();
    },
  /* failure_callback */
    (error) => {
        console.error("API Error:", error);
    }
  );
}
get_diary();

function get_plant(){
  fastapi('get', `/plant`, {},
  /* success_callback */
    (response) => {
        plants = response["data"];

        if(plants.length > 0){
          selected({target: {value: plants[0]["plant_id"]}}); // initialize with the first plant
        }
        else {
          console.log("No plants found.");
        }


    },
  /* failure_callback */
    (error) => {
        console.error("API Error:", error);
    }
  );
}



function selected(e){
  const plant_id = ((e as MouseEvent).target as HTMLSelectElement).value;
  console.log("Selected plant ID:", plant_id);

  // show plants start date
  document.getElementById("since").innerHTML = "Planted since <b>"
      + plants.find(p => p["plant_id"] == plant_id)["start_date"].split("T")[0] + "</b>";



  // filter diaries by plant_id
  selectedPlantId = plant_id;
  filteredDiaries = [];
  var i = 0;
  
  Object.entries(diaries).forEach(([key, value]) => {
    if(value["plant_id"] == selectedPlantId){
      filteredDiaries[i++] = value;
    }
  });


  // sort filtered diaries by date ascending
  filteredDiaries = Object.values(filteredDiaries).sort((a, b) => {
    return new Date(a["date"]).getTime() - new Date(b["date"]).getTime();
  });

  console.log("Filtered Diaries:", JSON.stringify(filteredDiaries));


  // remove existing table rows except header
  document.getElementById("plant_head").innerHTML = '<th scope="col">Date</th>';
  document.getElementById("plant_row1").innerHTML = '<td><b>Checked Organ</b></td>';
  document.getElementById("plant_row2").innerHTML = '<td><b>Stage</b></td>';
  document.getElementById("plant_row3").innerHTML = '<td><b>Health</b></td>';
  document.getElementById("plant_row4").innerHTML = '<td><b>Chlorophyll</b></td>';
  document.getElementById("plant_row5").innerHTML = '<td><b>Greenness</b></td>';
  document.getElementById("plant_row6").innerHTML = '<td><b>Image</b></td>';


  var f: string;
  if(i === 0){
    console.log("No diaries found for the selected plant ID.");
    let th = document.createElement("th") as HTMLTableCellElement;
    th.rowSpan = 6;
    th.style.verticalAlign = "middle";
    th.innerHTML = "No diary entries found for the selected plant.";
    document.getElementById("plant_head").appendChild(document.createElement("th") as HTMLTableCellElement);
    document.getElementById("plant_row1").appendChild(th);

    document.getElementById("comment").innerHTML = "";
  }
  else{

    f = JSON.stringify(filteredDiaries);
    console.log("len", i);


    // populate table with filtered diaries
    for (let j = 0; j < i; j++) {
      let th = document.createElement("th") as HTMLTableCellElement;
      th.scope = "col";
      // date with growth time
      var diff = new Date(filteredDiaries[j]["date"]).getTime() -
        new Date(plants.find(p => p["plant_id"] == plant_id)["start_date"]).getTime();
      var diffDays = Math.floor(diff / (1000 * 60 * 60 * 24));

      th.innerHTML = filteredDiaries[j]["date"].split("T")[0] +
      ` (+${diffDays} days)`;
      document.getElementById("plant_head").appendChild(th);

      let td1 = document.createElement("td") as HTMLTableCellElement;
      td1.innerHTML = filteredDiaries[j]["organ_type"];
      document.getElementById("plant_row1").appendChild(td1);

      let td2 = document.createElement("td") as HTMLTableCellElement;
      td2.innerHTML = filteredDiaries[j]["stage"];
      document.getElementById("plant_row2").appendChild(td2);

      let td3 = document.createElement("td") as HTMLTableCellElement;
      td3.innerHTML = filteredDiaries[j]["diagnosis"];
      document.getElementById("plant_row3").appendChild(td3);

      let td4 = document.createElement("td") as HTMLTableCellElement;
      td4.innerHTML = filteredDiaries[j]["chlorophyll_content"];
      document.getElementById("plant_row4").appendChild(td4);

      let td5 = document.createElement("td") as HTMLTableCellElement;
      td5.innerHTML = filteredDiaries[j]["measurement"];
      document.getElementById("plant_row5").appendChild(td5);

      let td6 = document.createElement("td") as HTMLTableCellElement;
      td6.innerHTML = `
      <img class="img rounded" id="${filteredDiaries[j]["id"]}" onclick={view_detail(event)}
      style="max-width: 250px;"
      src="${filteredDiaries[j]["img"]}"
      alt="Plant Image" />
      `;
      document.getElementById("plant_row6").appendChild(td6);
    }

    // if all healthy, show a message
    let allHealthy = true;
    for (let j = 0; j < i; j++) {
      if(filteredDiaries[j]["diagnosis"] !== "Healthy"){
        allHealthy = false;
        break;
      }
    }
    if(allHealthy){
      document.getElementById("comment").innerHTML = "All parts of the plant seems to be healthy. Keep up the good work! 😊";
    }
    else{

      if(filteredDiaries[i - 1]["diagnosis"] !== "Healthy"){
        document.getElementById("comment").innerHTML = "The latest check shows the plant is not healthy. Please take necessary actions. ⚠️";
      }
      else{
        document.getElementById("comment").innerHTML = "Some parts of the plant were not healthy in previous checks. Be cautious. ⚠️";
      }
    }


    // draw graphs using greenness data over time (optional)
    // using canvas or any graph library


  }
  // document.getElementById("filtered-diaries").innerHTML = f;
}


</script>


<Top />
<main>

  <MenuTitle title="Summary" icon={logo_summary} />

  <div class="inputset">
    <label class="f24" for="plant-id">Plant Name:</label>
    <select class="f24" onchange={selected} id="plant-id">
      {#each plants as plant}
        <option value={plant["plant_id"]}>{plant["plant_name"]}</option>
      {/each}
    </select>
  </div>
  <br/>
  <ParaDeco id="since" color="white_transparent" size="12" />
  <ParaDeco id="comment" color="white_transparent" size="12" />

  <p id="filtered-diaries" class="center"></p>

  <div class="table-container">
    <table class="table table-hover">
      <thead>
        <tr id="plant_head">
          <th scope="col">Date</th>
        </tr>
      </thead>
      <tbody>
        <tr id="plant_row1">         
          <td><b>Checked Organ</b></td> 
        </tr>
        <tr id="plant_row2">         
          <td><b>Stage</b></td>
        </tr>
        <tr id="plant_row3">         
          <td><b>Health</b></td> 
        </tr>
        <tr id="plant_row4">         
          <td><b>Chlorophyll</b></td>
        </tr>
        <tr id="plant_row5">         
          <td><b>Greenness</b></td>
        </tr>
        <tr id="plant_row6">         
          <td><b>Image</b></td>
        </tr>
      </tbody>
    </table>
  </div>


  <!-- create a summary table here -->

</main>


<style>
 
  .center{
    text-align: center;
  }
  .inputset {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    margin: 10px auto;
    padding: 10px 50px;
    width: fit-content;
    background-color: rgba(255, 255, 255, 0.596);
    border-radius: 30px;
  }

  .f24{
    font-size: 24px;
    font-weight: bold;
  }


  #plant-id {
    margin-left: 10px;
    padding: 5px;
    background-color: rgba(0, 128, 0, 0.5);
  }
  .table-container {
    overflow-x: auto; /* Enables horizontal scrolling if content overflows */
    margin: 30px auto; /* Centers the container */
    width: fit-content;
    max-width: calc(100% - 60px);
    max-height: calc(85vh - 100px); /* Sets a maximum height */
    border-width: 5px;
    border-style: solid;
    border-radius: 15px;
    border-color: rgba(0, 255, 98, 0.411);
    box-shadow: 2px 2px 10px rgb(0, 0, 0);        
    background-color: white;
  }

  .table{
    margin: 0 auto; /* Centers the table */
    width: auto; /* Allows the table to expand beyond container width */
    white-space: nowrap; /* Prevents text wrapping within cells */
    /* border: 1px solid black; */
    border-collapse: collapse;
  }

  .img{
    max-width: 120px;
    max-height: 100px;
  }

  thead th{
    position: sticky;
    top: 0;
    background-color: white;
    
    z-index: 1;
  }

</style>
