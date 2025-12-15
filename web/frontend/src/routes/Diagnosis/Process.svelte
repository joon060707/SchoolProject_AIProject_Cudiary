<script lang="ts">
// import logo from '../../assets/CDR.png'
import MenuTitle from '../../lib/MenuTitle.svelte';
import Top from '../../lib/Top.svelte'
import fastapi from '../../lib/api';
import logo_search from '../../assets/search.svg'
import ParaDeco from '../../lib/ParaDeco.svelte';

var plants = $state(""); // local state variable

// get plant list
function get(){
  fastapi('get', `/plant`, {},
  /* success_callback */
    (response) => {
        plants = response["data"];
    },
  /* failure_callback */
    (error) => {
        console.error("API Error:", error);
    }
  );
}
get();

// get image url from cookie
var addr;
$effect(() => {  // This will run when the component is mounted

  dateInput = document.getElementById("date") as HTMLInputElement;
  photoDateInput = document.getElementById("photo_date") as HTMLInputElement;
  nameInput = document.getElementById("name") as HTMLInputElement;
  descriptionInput = document.getElementById("description") as HTMLTextAreaElement;

  dateInput.value = new Date(Date.now()+9*60*60*1000).toISOString().split('T')[0];
  photoDateInput.value = new Date(Date.now()+9*60*60*1000).toISOString().split('T')[0];
  nameInput.value = "New Plant";
  descriptionInput.value = "";

  cookieStore.get('uploaded_image_url').then((cookie) => {
      if (cookie) {
          addr = cookie.value;
          console.log("Retrieved uploaded image URL from cookie:", addr);

          // Display the image in the preview element
          const preview: HTMLImageElement = document.getElementById("preview") as HTMLImageElement;
          preview.src = addr;

      } else {
          console.error("No uploaded image URL found in cookies.");
          alert("No uploaded image found. Please upload an image first.");
          window.location.href = '#/diagnosis/'; // redirect to process page
      }
  });

  document.getElementById('diagnose').addEventListener('click', send);
  selected({target: {value: 0}}); // default to new plant


});

// common elements
var dateInput: HTMLInputElement;
var nameInput: HTMLInputElement;
var photoDateInput: HTMLInputElement;
var descriptionInput: HTMLTextAreaElement;

// after selecting plant, auto-set date to the stored date
function selected(e){
  const plant_id = e.target.value;
  console.log("Selected plant ID:", plant_id);

  if(plant_id != 0){
    // find the plant in plants
    const selected_plant = plants.find((plant) => plant.plant_id == plant_id);
    if(selected_plant){
      const growth_start_date = selected_plant.start_date;
      // format: yyyy-mm-dd
      const formatted_date = growth_start_date.split('T')[0];
      console.log("Found growth start date:", formatted_date);

      // set the date input value
      dateInput.value = formatted_date;
      dateInput.disabled = true; // disable editing

      // set the name input value
      nameInput.value = selected_plant.plant_name;

    }
  } else {
    // new plant
    // date.now() -> yyyy-mm-dd
    const formatted_date = new Date(Date.now()+9*60*60*1000).toISOString().split('T')[0];
    dateInput.value = formatted_date;
    dateInput.disabled = false; // enable editing

    nameInput.value = "New Plant";
  }
}

// send diagnosis request
function send(){

  cookieStore.delete('total_growth_days');
  cookieStore.delete('growth_start_date');
  cookieStore.delete('plant_name');

  const plantSelect: HTMLSelectElement = document.getElementById("plant-id") as HTMLSelectElement;
  const plant_id = plantSelect.value;

  const growth_date = dateInput.value;

  const photo_date = photoDateInput.value;

  const plant_name = nameInput.value;

  const description = descriptionInput.value;


  // calculate the total growth days
  const growth_start_date = new Date(growth_date);
  // const current_date = new Date(Date.now()+9*60*60*1000); // Korea Standard Time
  const current_date = new Date(photo_date);
  const total_growth_days = Math.floor((current_date.getTime() - growth_start_date.getTime()) / (1000 * 60 * 60 * 24));
  cookieStore.set({ name: 'total_growth_days', value: `${total_growth_days}`, path: '/' });
  cookieStore.set({ name: 'growth_start_date', value: growth_date, path: '/' });
  cookieStore.set({ name: 'plant_name', value: plant_name, path: '/' });

  const jsonData = {
    "plant_id": plant_id,
    "plant_name": plant_name,
    "growth_date": growth_date,
    // "datenow": new Date(Date.now()+9*60*60*1000).toISOString(), // Korea Standard Time
    "datenow": new Date(current_date).toISOString(),
    "description": description,
    "image_url": addr
  };



  console.log("Sending diagnosis request with:", JSON.stringify(jsonData));
  alert('Diagnosis request sent successfully!');
  document.getElementById('loading').style.display = 'block';
  document.getElementById('wrapper').style.display = 'none';

  // post with json body
  fetch(`http://localhost:8000/diagnosis`, {
      method: 'POST',
      body: JSON.stringify(jsonData),
      headers: {
          'Content-Type': 'application/json',
      },
  })
  .then(data => {
    // response from server
      data.body.getReader().read().then(({ done, value }) => {
          if (!done) {
              var result = new TextDecoder('utf-8').decode(value);
              // {status: 'success', diagnosis: 'Healthy', confidence: 0.95}
              console.log('Diagnosis result received:', result);
              // Handle success (e.g., display a message)

              alert('Diagnosis result received successfully!');
              cookieStore.set({ name: 'diagnosis_result', value: result, path: '/'});
              window.location.href = '#/diagnosis/result'; // redirect to process page
          }
      });
      // console.log('Response from server:', data);
      // Handle the server response


  })
  .catch(error => {
      console.error('Error sending diagnosis request:', error);
      // Handle error
  });
}

</script>

<Top />
<main>
  <MenuTitle title="Diagnosis" icon={logo_search} />
  <ParaDeco color="white_transparent" title="Is this plant previously diagnosed, or a new plant?" size="12" shadow="shadow" />
  <div class="container">

    <div id="wrapper">
      <div class="inputset">
        <label for="plant-id">Plant Name:</label>
        <select onchange={selected} id="plant-id">
          {#each plants as plant}
            <option value={plant["plant_id"]}>{plant["plant_name"]}</option>
          {/each}
            <option value={0}>New...</option>
        </select>
      </div>
      <div class="inputset">
        <label for="name">Plant name(optional):</label>
        <input id="name" type="text" />
      </div>
      <div class="inputset">
        <label for="date">Growth start date:</label>
        <input id="date" type="date" />
      </div>
      <div class="inputset">
        <label for="photo_date">Photo taken date:</label>
        <input id="photo_date" type="date" />
      </div>
      <div class="inputset">
        <label for="description">Memo (optional):</label>
        <textArea id="description" placeholder="Enter memo..." ></textArea>
      </div>
      <div class="inputset">
        <button id="diagnose" >Send</button>
      </div>      
      <!-- Loading indicator -->
    </div>

    <div id="loading" style="width:100%; max-width:400px; display: none;">
      <p class="center" style="margin: 50px 0;">Processing...</p>
    </div>



    <img id="preview" alt="preview" src="" />

    <!-- <input id="submit" type="submit" value="Send" class="btn btn-primary" style="display: none;" /> -->
  </div>
  <!-- <form method="post" enctype="multipart/form-data">  </form> -->


</main>


<style>

  .center{
    text-align: center;
  }

  #loading{
    font-size: 24pt;
    font-weight: bold;
    max-width: 400px;
  }

  label {
    margin-right: 10px;
    text-align: right;
  }

  .inputset {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    margin: 10px 0;
  }

  textarea {
    max-width: 500px;
    height: 100px;
  }

  #wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 400px;
    margin-bottom: 20px;
  }

  .container {
    display: flex;
    flex-wrap: wrap;
    background-color: antiquewhite;
    justify-content: center;
    height: fit-content;
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }

  #preview {
    display: block;
    margin: 20px auto;
    width: 90%;
    max-width: 600px;
  }

  button{
    width: 140px;
    height: 70px;
    margin: 30px;
    transition: background-image 300ms, background-color 300ms, filter 300ms;
    background-image: url('../../assets/btbg.png');
    background-size: cover;
    padding: 10px 20px;
    margin: 20px;
    font-size: 16pt;
    border: 5px solid white;
    border-radius: 20px;
    box-shadow: 5px 5px 5px rgb(78, 78, 78);
  }

  button:hover {
    background-image: none;
    background-color: #e5ff89;
    border: 5px solid #8383ff;
    filter: drop-shadow(0 0 2em #050a68aa);
  }  

</style>
