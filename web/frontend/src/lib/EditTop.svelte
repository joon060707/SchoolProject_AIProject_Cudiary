<script lang="ts">
  import { link } from 'svelte-spa-router'

  var props = $props(); // get props passed to this component


  var back = document.URL.split('/')[document.URL.split('/').length-1];
  var target = document.URL.replace("http://localhost:5173/", '');
  target = target.replace(back, '');
  // if(target === "#/")
  //   target = "http://localhost:5173/#";
  if(target.endsWith('/'))
    target = target.substring(0, target.length - 1);
  console.log("back target:", target);


  var diary_id = $state(""); // local state variable
  cookieStore.get('diary_id').then((cookie) => {
  if (cookie) {
      diary_id = cookie.value;
      console.log("Requested diary ID from cookie:", diary_id);
  } else {
      console.error("No diary ID found in cookies.");
  }
  });


  function apply_changes(){
    // get values from EditUI and EditUIVal components
    const plant_id = props.plantid;
    const plant_name = (document.getElementById("plant_name") as HTMLInputElement).value;
    const unit = (document.getElementById("Unit") as HTMLInputElement).value;
    const organ_type = (document.getElementById("Type") as HTMLInputElement).value;
    const growth_stage = (document.getElementById("Stage") as HTMLInputElement).value;
    const note = (document.getElementById("Comment") as HTMLInputElement).value;
    const Health = (document.getElementById("Health") as HTMLInputElement).value;
    const Chlorophyll = (document.getElementById("Chlorophyll") as HTMLInputElement).value;
    const Greenness = (document.getElementById("Greenness") as HTMLInputElement).value;
    console.log("Applying changes:", plant_id, plant_name, unit, organ_type, growth_stage, note, Health, Chlorophyll, Greenness);

    // implement the apply changes functionality here
    const jsonData = {
    "plant_id": plant_id,
    "plant_name": plant_name,
    "diary_id": diary_id,
    "unit": unit,
    "organ_type": organ_type,
    "growth_stage": growth_stage,
    "note": note,
    "diagnosis": Health,
    "chlorophyll_content": Chlorophyll,
    "measurement": Greenness
  };

  console.log("Sending update request with:", JSON.stringify(jsonData));

  // post with json body
  fetch(`http://localhost:8000/diary/update/${diary_id}`, {
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
              console.log('Update: ', result);

              if(JSON.parse(result)["result"] === "success"){
                alert("Changes applied successfully!");
                // redirect to view page
                window.location.href = `http://localhost:5173/#/diary/${diary_id}`;
              } else {
                alert("Failed to apply changes. Please try again.");
              }
          }
      });
  })
  .catch(error => {
      console.error('Error sending request:', error);
      // Handle error
  });
  
  }
  

</script>

<div class="backset">
  <a use:link href={target}>
  <button >{"<"}</button>
  </a>
</div>

<div class="apply">
  <!-- <a use:link href={window.location.href + "/apply"}> -->
  <button onclick={apply_changes} >{"Apply"}</button>
  <!-- </a> -->
</div>


<style>
  button{
    height: 70px;
    margin: 30px;
    transition: background-image 300ms, background-color 300ms, filter 300ms;
    background-image: url('../assets/btbg.png');
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

  .backset{
    width: 80px;
    position: fixed;
    top: 10px;
    left: 10px;
  }

  .apply{
    width: 100px;
    position: fixed;
    top: 10px;
    right: 100px;
  }

  button:hover {
    background-color: #ffd089;
  }
</style>