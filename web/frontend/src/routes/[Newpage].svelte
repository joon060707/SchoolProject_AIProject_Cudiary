<script>
import fastapi from '../lib/api.js'
import Top from '../lib/Top.svelte'
let data = $state(""); // local state variable
// $inspect(data); // for debugging

function get(){
  fastapi('get', `/diary`, {},
  /* success_callback */
    (response) => {
        data = JSON.stringify(response["data"]);
    },
  /* failure_callback */
    (error) => {
        console.error("API Error:", error);
    }
  );
}

// get();
</script>


<Top />
<main>
  <p class="center">Sorry but you requested a value that does not exist. Go back to <a href="/">home</a>.</p>
  <!-- <p class="center">requested value: {1}</p> -->
  <!-- <p class="center">fetched: {data}</p> -->
</main>


<style>
 
  .center{
    text-align: center;
  }

</style>
