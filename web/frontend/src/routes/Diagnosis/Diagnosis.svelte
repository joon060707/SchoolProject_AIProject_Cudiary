<script>
import fastapi from '../../lib/api.js'
import MenuTitle from '../../lib/MenuTitle.svelte';
import Top from '../../lib/Top.svelte'
import MB from '../../lib/MenuButton.svelte'
import logo_take from '../../assets/take.svg'
import logo_upload from '../../assets/upload.svg'
import logo_search from '../../assets/search.svg'
	import ParaDeco from '../../lib/ParaDeco.svelte';

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

get();
</script>


<Top />
<main>
  <MenuTitle title="Diagnosis" icon={logo_search} />
  <ParaDeco color="white_transparent" title="Please either take or upload a plant photo." size="12" shadow="shadow" />
    <div class="buttonset">
            <MB title={"Take"} site={"#/diagnosis/take"} icon={logo_take} size="large" />
            <MB title={"Upload"} site={"#/diagnosis/upload"} icon={logo_upload} size="large" />
    </div>
  <ParaDeco color="lightgreen" title="⚠️ Notice: Please use a photo that shows a clear view of the plant." size="12" shadow="shadow" />
</main>


<style>
 
  .center{
    text-align: center;
  }

   .buttonset{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 50px;
    margin-bottom: 20px;
  }

</style>
