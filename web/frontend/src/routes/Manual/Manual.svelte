<script>
import Top from '../../lib/Top.svelte'
import MenuTitle from '../../lib/MenuTitle.svelte';
import { link } from 'svelte-spa-router'
import MenuButton from '../../lib/MenuButton.svelte';
import logo_search from '../../assets/search.svg'
import logo_diary from '../../assets/diary.svg'
import logo_manual from '../../assets/help.svg'
import ParaDeco from '../../lib/ParaDeco.svelte';
</script>


<Top />
<main>
  <MenuTitle title="Manual" icon={logo_manual} />
  <ParaDeco color="white_transparent" title={`Resources for using the app`} size="12" shadow="shadow" />
  <div class="wrapper">
    <div class="cultivate">
      <ParaDeco color="white_transparent" title={`Cultivating Cucurbits`} size="24" shadow="shadow" />
      <div><a use:link href={"#/manual/germination"}> <MenuButton title={"🌱 Germination / Seedling"} site={"#/manual/germination"} size="small" /> </a></div>
      <div><a use:link href={"#/manual/vegetative"}>  <MenuButton title={"🥬 Vegetative Growth"} site={"#/manual/vegetative"} size="small" />        </a></div>
      <div><a use:link href={"#/manual/flowering"}>    <MenuButton title={"🌼 Flowering"} site={"#/manual/flowering"} size="small" />        </a></div>
      <div><a use:link href={"#/manual/fruit-setting"}>  <MenuButton title={"🥒 Fruit Setting / Harvesting"} site={"#/manual/fruit-setting"} size="small" />  </a></div>
    </div>
    <div class="appmanual">
       <ParaDeco color="white_transparent" title={`Application Manual`} size="24" shadow="shadow" />
      <div><a use:link href={"#/manual/diagnosis"}>   <MenuButton title={"Diagnosis"} site={"#/manual/diagnosis"} icon={logo_search} size="large" /> </a></div>
      <div><a use:link href={"#/manual/diary"}>   <MenuButton title={"Diary"} site={"#/manual/diary"} icon={logo_diary} size="large" />        </a></div>
    </div>
  </div>
</main>


<style>
  .center{
    text-align: center;
  }
  .wrapper{
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: center;
    margin: 20px;
  }
  .cultivate, .appmanual{
    display: flex;
    flex-direction: column;
    align-items: center;
    min-width: 300px;
    max-width: 700px;
    height: fit-content;
    margin: 20px auto;

  }
  .cultivate-buttons{
    width: 250px; /* default width */
    margin: 20px 0;
    font-size: 12pt;
  }
  /* .app-buttons{
    width: 250px;
    height: 120px;
    margin: 30px 0;
    font-size: 24pt;
  } */
  button {
    transition: background-image 300ms, background-color 300ms, filter 300ms; 
    background-color: none;
    background-image: url('../../assets/btbg.png');
    background-size: cover;
  }
  button:hover {
    background-image: none;
    background-color: #e5ff89;
    filter: drop-shadow(0 0 2em #050a68aa);
  }

</style>
