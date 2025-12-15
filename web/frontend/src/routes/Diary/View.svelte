<script>
import fastapi from '../../lib/api.js'
import ViewTop from '../../lib/ViewTop.svelte'
import ResultUI from '../../lib/ResultUI.svelte';
import MenuTitle from '../../lib/MenuTitle.svelte';
import ParaDeco from '../../lib/ParaDeco.svelte';
import logo_diary from '../../assets/diary.svg'

let diary_id = $state(); // local state variable
let diary = $state(""); // local state variable // "" is necessary to initialize as a string
let plant_id = $state(); // local state variable
let plant = $state(""); // local state variable
let diffDays = $state(0); // local state variable
// $inspect(data); // for debugging

let healthcolor = $state("green");
let chlorophyllcolor = $state("green");
let measurementcolor = $state("green");
let stagecolor = $state("blue");



cookieStore.get('diary_id').then((cookie) => {
  if (cookie) {
      diary_id = cookie.value;
      console.log("Requested diary ID from cookie:", diary_id);
      get_diary();
  } else {
      console.error("No diary ID found in cookies.");
  }
});


function get_diary(){
  fastapi('get', `/diary/${diary_id}`, {},
  /* success_callback */
    (response) => {
        diary = response["data"];
        document.getElementById("comment_txt").innerHTML = diary["note"].replace(/\n/g, "<br>");

        plant_id = diary["plant_id"];
        console.log(plant_id);

        get_plant();
    },
  /* failure_callback */
    (error) => {
        console.error("API Error:", error);
    }
  );
}

function get_plant(){
  fastapi('get', `/plant/${plant_id}`, {},
  /* success_callback */
    (response) => {
        plant = response["data"];

        plant["start_date"] = plant["start_date"].split('T')[0]; // format date

        // total growth days = diary[date] - plant[start_date]
        const diary_date = new Date(diary["date"]);
        const plant_start_date = new Date(plant["start_date"]);
        const diffTime = Math.abs(diary_date.getTime() - plant_start_date.getTime());
        diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        console.log("Total growth days:", diffDays);



        // set color based on values

        // stage: if vegetative with growth days > 30, abnormal
        // if flowering with growth days < 20, abnormal
        // 
        if( (diary["stage"] === "Vegetative") && (diffDays > 30) ||
            (diary["stage"] === "Flowering") && (diffDays < 20) ){
          stagecolor = "abnormal"; 
        }
        else{  
          stagecolor = "blue";
        }


        // health
        if(diary["diagnosis"] === "Healthy"){
          healthcolor = "green";
        }
        else{
          healthcolor = "abnormal";
        }

        // chlorophyll
        if(diary["chlorophyll_content"] === "Normal" || diary["chlorophyll_content"] === "High"){
          chlorophyllcolor = "green";
        }
        else{
          chlorophyllcolor = "abnormal";
        }

        // measurement
        if(diary["stage"] === "Fruiting"){
          if(diary["measurement"] > 20){
            measurementcolor = "green";
          }
          else{
            measurementcolor = "abnormal";
          }
        }
        else{ // vegetative or flowering
          if(diary["measurement"] > 60){
            measurementcolor = "green";
          }
          else{
            measurementcolor = "abnormal";
          }
        }

    },
  /* failure_callback */
    (error) => {
        console.error("API Error:", error);
    }
  );
}



</script>

<!-- This contains removal button -->
<ViewTop diaryid={diary_id} />
<main>
  <!-- <p class="center">Sorry but you requested a value that does not exist.</p>
  <p class="center">requested value: {diary_id}</p>
  <p class="center">{JSON.stringify(diary)}</p>
  <p class="center">{JSON.stringify(plant)}</p> -->

  <MenuTitle title="View Diary" icon={logo_diary} />

  <div class="info center">
      <h3 style="color:green">🥒Plant name: <b>{plant["plant_name"]}</b> (ID: {plant["plant_id"]})</h3>
      <h4>🌱Growth since <b>{plant["start_date"]}, {diffDays} Day(s)</b></h4>
      <!-- ResultUI -->
      <div class="roundbox transparent wide">
        <p class="i"></p>
        <h5 style="text-align: left;">Comment</h5>
        <p id="comment_txt" class="comment"></p>
      </div>
  </div>


  <div class="wrapper">
    <div class="side">
      <ParaDeco color="white" title="Classification" size="24" shadow="shadow" />
      <div class="ResultSet">
        <ResultUI title="Unit" description={diary["unit"]} color="blue"/>
        <ResultUI title="Type" description={diary["organ_type"]} color="blue"/>
        <ResultUI title="Stage" description={diary["stage"]} color={stagecolor}/>
      </div>  
      <ParaDeco color="white" title="Diagnosis" size="24" shadow="shadow" />
      <div class="ResultSet">
        <ResultUI title="Health" description={diary["diagnosis"]} color={healthcolor}/>
        <ResultUI title="Chlorophyll" description={diary["chlorophyll_content"]} color={chlorophyllcolor}/>
        <ResultUI title="Greenness" description={diary["measurement"]} color={measurementcolor}/>
      </div>
    </div>

    <div class="side">
       <ParaDeco color="white" title="Image" size="24" shadow="shadow" />
      <img class="preview" src={diary["img"]} alt="Plant Image" />
    </div> 
  </div>
</main>


<style>

  
  h2{
    margin-top: 30px;
    margin-bottom: 10px;
  }
 
  .center{
    text-align: center;
  }

   .preview {
    width: 100%;
    max-width: 550px;
    border: 4px solid rgb(255, 255, 255);
    box-shadow: 5px 5px 5px rgb(78, 78, 78);
    border-radius: 15px;
    margin: 20px 0;
  }

  .wrapper{
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: center;
    margin: 20px;
  }

  .side{
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 700px;
    height: fit-content;
    margin: 20px auto;
    padding: 20px 10px;
    background-color: rgba(255, 255, 255, 0.411);
    border-radius: 40px;
    border-width: 5px;
    border-style: solid;
    border-color: rgba(0, 255, 98, 0.411);
    box-shadow: 0px 0px 10px rgb(0, 0, 0);
  }

  .ResultSet{
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: center;
    /* resultbox = 200px */
    width: 100%; 
  }
    
  .comment{
    font-size: 12pt;
    text-align: left;
  }

 
  .roundbox{
    border: 3px solid rgb(255, 255, 255);
    border-radius: 20px;
    box-shadow: 7px 7px 10px rgb(78, 78, 78);
    padding: 5px 15px;
    margin: 15px auto;
    /* background-color: #f0f8ff; */
    width: 200px;
    height: fit-content;
  }

  .wide{
    width: calc(100% - 60px);
  }

  .transparent{
    background-color: #ffffff80;
  }

 

</style>
