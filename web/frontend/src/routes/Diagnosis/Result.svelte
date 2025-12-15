<script lang="ts">
import Top from '../../lib/Top.svelte'
import ResultUI from '../../lib/ResultUI.svelte';
import MenuButton from '../../lib/MenuButton.svelte';
import MenuTitle from '../../lib/MenuTitle.svelte';
import logo_edit from '../../assets/edit.svg'
import logo_manual from '../../assets/help.svg'
import logo_search from '../../assets/search.svg'
import ParaDeco from '../../lib/ParaDeco.svelte';

var result = $state(""); // local state variable
var json_result = $state({}); // local state variable
var diary_id = $state(""); // local state variable
var stagecolor = $state("blue"); // local state variable
var healthcolor = $state("green"); // local state variable
var chlorophyllcolor = $state("green"); // local state variable
var measurementcolor = $state("green"); // local state variable
var msg = $state(""); // local state variable
var bgcolor = $state("white"); // local state variable
var stage = $state(""); // local state variable

$effect(() => {
  // This will run when the component is mounted

  cookieStore.get('diagnosis_result').then((cookie) => {
      if (cookie) {
          result = cookie.value;
          console.log("Retrieved diagnosis result from cookie:", result);

          for (const [key, value] of Object.entries(JSON.parse(result)["data"])) {
              console.log(`${key}: ${value}`);
          }

          json_result = JSON.parse(result)["data"];
          diary_id = JSON.parse(result)["id"];

          cookieStore.set({ name: 'diary_id', value: diary_id, path: '/'});


        // stage for link        
        if(json_result["growth_stage"] == "Vegetative")
          stage = "vegetative";
        else if(json_result["growth_stage"] == "Flowering")
          stage = "flowering";
        else if(json_result["growth_stage"] == "Seedling")
          stage = "germination";
        else // fruiting or other
          stage = "fruit-setting";

        // health
        if(json_result["diagnosis"] === "Healthy"){
          healthcolor = "green";
          msg = "😊 Nice!";
          bgcolor = "white";
        }
        else{
          healthcolor = "abnormal";
          msg = "⚠️ Check carefully!";
          bgcolor = "abnormal";
        }

        // chlorophyll
        if(json_result["chlorophyll_content"] === "Normal" || json_result["chlorophyll_content"] === "High"){
          chlorophyllcolor = "green";
        }
        else{
          chlorophyllcolor = "abnormal";
        }

        // measurement
        if(json_result["growth_stage"] === "Fruiting"){
          if(json_result["measurement"] > 20){
            measurementcolor = "green";
          }
          else{
            measurementcolor = "abnormal";
          }
        }
        else{ // vegetative or flowering
          if(json_result["measurement"] > 60){
            measurementcolor = "green";
          }
          else{
            measurementcolor = "abnormal";
          }
        }        





      } else {
          console.error("No diagnosis result found in cookies.");
          alert("No diagnosis result found. Please complete the diagnosis first.");
          window.location.href = '#/diagnosis/'; // redirect to process page
      }
  });

  cookieStore.get('total_growth_days').then((cookie) => {
      if (cookie) {
          const total_growth_days = cookie.value;
          console.log("Total growth days from cookie:", total_growth_days);
          json_result["growth_days"] = `${total_growth_days} Days`;

          if( (json_result["growth_stage"] === "Vegetative") && (cookie.value > 30) ||
            (json_result["growth_stage"] === "Flowering") && (cookie.value < 20) ){
          stagecolor = "abnormal"; 
        }
        else{  
          stagecolor = "blue";
        }
      } else {
          console.error("No total growth days found in cookies.");
          json_result["growth_days"] = "0 Days";
      }
  });

  cookieStore.get('growth_start_date').then((cookie) => {
      if (cookie) {
          const growth_start_date = cookie.value;
          console.log("Growth start date from cookie:", growth_start_date);
          json_result["growth_since"] = `${growth_start_date}`;
      } else {
          console.error("No growth start date found in cookies.");

          // format: 2025-11-04T13:26:17.490Z -> 2025-11-04
          const formatted_date = cookie.value.split('T')[0];
          json_result["growth_since"] = `since ${formatted_date}`;
      }
  });

  cookieStore.get('plant_name').then((cookie) => {
      if (cookie) {
          const plant_name = cookie.value;
          console.log("Plant name from cookie:", plant_name);
          json_result["plant_name"] = plant_name;
      } else {
          console.error("No plant name found in cookies.");
          json_result["plant_name"] = "Unknown Plant";
      }
  });

});

</script>

<Top />
<main>
  <MenuTitle title="Diagnosis Result" icon={logo_search} />

  <div class="wrapper">
    <div class="side">
      <div class="overall">
        <ParaDeco color={bgcolor} title={msg} size="30" shadow="shadow" />
        <ParaDeco color="gray" title={`Inference time: ${parseFloat(json_result["total_elapsed_time"]).toFixed(3)} seconds`}  size="12" />
        <ParaDeco color="gray" bold="bold" title={`ℹ️ ${json_result["diagnosis_detail"]}`} size="12" />
      </div>
      <br/>
      <ParaDeco color="white" title="Classification" size="24" shadow="shadow" />
      <div class="ResultSet">
        <ResultUI title="Unit" description={`${json_result["unit"]} (${(json_result["unit_confidence"]*100).toFixed(2)}%)`} color="blue"/>
        <ResultUI title="Type" description={`${json_result["organ_type"]} (${(json_result["organ_type_confidence"]*100).toFixed(2)}%)`}  color="blue"/>
        <ResultUI title="Stage" description={json_result["growth_stage"]} color={stagecolor}/>
      </div>  
      <ParaDeco color="white" title="Diagnosis" size="24" shadow="shadow" />
      <div class="ResultSet">
        <ResultUI title="Health" description={json_result["diagnosis"]} color={healthcolor}/>
        <ResultUI title="Chlorophyll" description={json_result["chlorophyll_content"]} color={chlorophyllcolor}/>
        <ResultUI title="Greenness" description={json_result["measurement"]} color={measurementcolor}/>
      </div>
    </div>

    <div class="side">
      <ParaDeco class="center" title={json_result["plant_name"]}  shadow="shadow" textColor="gray" color="white" bold="bold" size="20" /> 
      <ParaDeco title={`Growth since ${json_result["growth_since"]} (${json_result["growth_days"]})`} textColor="gray" color="white" bold="bold" size="12" />

      <img class="preview" src={json_result["image_url"]} alt="Plant Image" />

      <div class="ResultSet">
            <MenuButton title="Edit it" site="#/diary/{diary_id}/edit"  icon={logo_edit} size="large" />
            <MenuButton title="Manual" site="#/manual/{stage}"  icon={logo_manual} size="large" />
      </div>
    </div> 
  </div>

</main>


<style>

  

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

 

</style>
