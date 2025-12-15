<script lang="ts">
import fastapi from '../lib/api.js'

let data = $state(""); // local state variable
$inspect(data).with((type, count) => {
		if (type === 'update') {
      console.log(`Data updated. ${data}`);
		}
	});

function get(){
  fastapi('get', `/diary`, {},
  /* success_callback */
    (response) => {
        data = response["data"];

        sort_id(); // default sort by id


    },
  /* failure_callback */
    (error) => {
        console.error("API Error:", error);
    }
  );
}

get();

// sorting
var sort_direction_date = -1; // 1: ascending, -1: descending
var sort_direction_id = -1; // 1: ascending, -1: descending
var sort_direction_plant_id = -1; // 1: ascending, -1: descending
var sort_direction_plant_name = -1; // 1: ascending, -1: descending
var sort_direction_growth_stage = -1; // 1: ascending, -1: descending

function sort_date(){
  sort_direction_date = -sort_direction_date; // Toggle sort direction
  data.sort((a, b) => {
    return sort_direction_date * (new Date(a.date).getTime() - new Date(b.date).getTime());
  });
}
function sort_id(){
  sort_direction_id = -sort_direction_id; // Toggle sort direction
  data.sort((a, b) => {
    return sort_direction_id * (a.id - b.id);
  });
}
function sort_plant_id(){
  sort_direction_plant_id = -sort_direction_plant_id; // Toggle sort direction
  data.sort((a, b) => {
    return sort_direction_plant_id * (a.plant_id - b.plant_id);
  });
}
function sort_plant_name(){
  sort_direction_plant_name = -sort_direction_plant_name; // Toggle sort direction
  data.sort((a, b) => {
    return sort_direction_plant_name * a.plant_name.localeCompare(b.plant_name);
  });
}
function sort_growth_stage(){
  sort_direction_growth_stage = -sort_direction_growth_stage; // Toggle sort direction
  data.sort((a, b) => {
    // Seedling < Vegetative < Flowering < Fruiting
    const stages = ["Seedling", "Vegetative", "Flowering", "Fruiting"];
    return sort_direction_growth_stage * (stages.indexOf(a.stage) - stages.indexOf(b.stage));
  });
}

////////////////////////
// move to detail page
function view_detail(e){
  const diary_id = ((e as MouseEvent).target as HTMLButtonElement).id;
  console.log("View details for diary ID:", diary_id);
  cookieStore.set({ name: 'diary_id', value: diary_id, path: '/'});
  window.location.href = `#/diary/${diary_id}`;
}

////////////////////////


// id (int, PK)	date (datetime)	plant_id (id, unique, foreign)	stage (str)	organ_type (str)	diagnosis (str)	note (str)	note2 (str)
var cols = ["action", "img","id", "date", "plant_id", "plant_name","note", "stage", "organ_type", "diagnosis"];
var cols_label = ["Action", "Image","Diary ID", "Date", "Plant ID", "Plant Name", "Comment", "Growth Stage", "Organ Type", "Diagnosis"];

</script>

<div class="table-container">
    <table class="table table-hover">
      <thead>
        <tr>
          {#each cols_label as col}
            {#if col === "Diary ID"}
            <th scope="col"><button onclick={sort_id} class="btn h btn-primary"><b>{col}</b></button></th>
            {/if}
            {#if col === "Date"}
            <th scope="col"><button onclick={sort_date} class="btn h btn-primary"><b>{col}</b></button></th>
            {/if}
            {#if col === "Plant ID"}
            <th scope="col"><button onclick={sort_plant_id} class="btn h btn-primary"><b>{col}</b></button></th>
            {/if}
            {#if col === "Plant Name"}
            <th scope="col"><button onclick={sort_plant_name} class="btn h btn-primary"><b>{col}</b></button></th>
            {/if}
            {#if col === "Growth Stage"}
            <th scope="col"><button onclick={sort_growth_stage} class="btn h btn-primary"><b>{col}</b></button></th>
            {/if}
            {#if col !== "Date" && col !== "Diary ID" && col !== "Plant ID" && col !== "Plant Name" && col !== "Growth Stage"}
            <th scope="col">{col}</th>
            {/if}            
            
          {/each}
        </tr>
      </thead>
      <tbody>
        {#if data.length === 0}
          <tr>
            <td colspan={cols.length}>No data available! Please add your diagnosis.</td>
          </tr>
        {/if}

        {#each data as row}
        <tr>          
          {#each cols as col}
            {#if col !== "img" && col !== "action" && col !== "date"}
            <td>{@html JSON.stringify(row[col]).replaceAll("\"", "").substring(0, 14).replaceAll("\\n", "<br>").replaceAll("\\", "")+(JSON.stringify(row[col]).length > 14 ? "..." : "")}</td>
            {/if}
            {#if col === "date"}
            <td>{JSON.stringify(row[col]).replaceAll("\"", "").split("T")[0]}</td>
            {/if}
            {#if col === "img"}
            <td> <img class="img" src={row[col]} alt="Plant Image" /></td>
            {/if}
            {#if col === "action"}
            <!-- cols[2] = id -->
            <td><button id={row[cols[2]]} onclick={view_detail} class="btn btn-primary">View</button></td>
            {/if}
          {/each}
        </tr>
        {/each}
        
      </tbody>
    </table>
</div>

<style>


  .table-container {
    overflow-x: auto; /* Enables horizontal scrolling if content overflows */
    margin: 30px auto; /* Centers the container */
    width: fit-content;
    max-width: calc(100% - 60px);
    max-height: calc(85vh - 100px); /* Sets a maximum height */
    border-width: 5px;
    border-style: solid;
    border-color: rgba(0, 255, 98, 0.411);
    border-radius: 15px;
    box-shadow: 2px 2px 10px rgb(0, 0, 0);        
    background-color: white;
  }

  .table{
    margin: 0 auto; /* Centers the table */
    width: auto; /* Allows the table to expand beyond container width */
    white-space: nowrap; /* Prevents text wrapping within cells */
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

  th, td {
    vertical-align: middle;
    text-align: center;
  }

  .btn{
    width: fit-content;
    height: 80px;
  }

 .h{
    height: 40px;    
  }

</style>
