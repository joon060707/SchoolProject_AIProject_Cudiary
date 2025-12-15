<script>
import { link } from 'svelte-spa-router'
import fastapi from './api.js';

var props = $props(); // get props passed to this component


var back = document.URL.split('/')[document.URL.split('/').length-1];
var target = document.URL.replace("http://localhost:5173/", '');
target = target.replace(back, '');
// if(target === "#/")
//   target = "http://localhost:5173/#";
if(target.endsWith('/'))
  target = target.substring(0, target.length - 1);
console.log("back target:", target);



function remove_diary(){
  if(confirm("Are you sure to remove this diary entry? This action cannot be undone.")){

    const jsonData = {
      "diary_id": props.diaryid
    };

    console.log("Removing diary ID:", props.diaryid);

      // post with json body
    fetch(`http://localhost:8000/diary/remove/${props.diaryid}`, {
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
                console.log('Remove: ', result);
                
                if(JSON.parse(result)["result"] === "success"){
                  alert("Entry removed successfully.");
                  // redirect to view page
                  window.location.href = `http://localhost:5173/#/diary`;
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
  
}



</script>

<div class="backset">
  <a use:link href={target}>
  <button >{"<"}</button>
  </a>
</div>

<div class="edit">
  <a use:link href={window.location.href + "/edit"}>
  <button >{"Edit"}</button>
  </a>
</div>

<div class="remove">
  <!-- <a use:link href={window.location.href + "/remove"}> -->
  <button onclick={remove_diary} id={props.diaryid} style="background-image: none; background-color: #ff876a;">{"Remove"}</button>
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

  .edit{
    width: 100px;
    position: fixed;
    top: 10px;
    left: 100px;
  }

  .remove{
    width: 100px;
    position: fixed;
    top: 10px;
    right: 100px;
  }

</style>