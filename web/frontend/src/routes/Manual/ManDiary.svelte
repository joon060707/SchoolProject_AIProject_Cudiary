<script>
import Top from '../../lib/Top.svelte'
import MenuTitle from '../../lib/MenuTitle.svelte';
import logo from '../../assets/CDR.png'
import logo_manual from '../../assets/diary.svg'
import image01 from '../../assets/manual/diary_01.png'
import image02 from '../../assets/manual/diary_02.png'
import image03 from '../../assets/manual/diary_03.png'
import image04 from '../../assets/manual/diary_04.png'
import image05 from '../../assets/manual/diary_05.png'
import image06 from '../../assets/manual/diary_06.png'

</script>


<Top />
<main>
  <MenuTitle title="Diary Manual" icon={logo_manual} />

  

  <div class="manuals">
    <h3 class="center">How to use the Diary Feature</h3>
    <p>This section will provide detailed instructions on how to use the diary feature. Please refer to the following steps:</p>
    <div class="manual">
      <h4>1. Click "Diary"</h4>
      <p>In the main menu, click on the "Diary" button.</p>
      <img src={image01} alt="Diary Step 1" />
    </div>
    <div class="manual">
      <h4>2. Select a diary entry</h4>
      <p>The diary table shows your all diagnosis results. You can check them and sort by date or plant name. You can also visit summary page for an overview.</p>
      <img src={image02} alt="Diary Step 2" />
      <p>If you look a specific diagnosis entry, click the "View" button to view detailed information.</p>
      <img src={image03} alt="Diary Step 2" />
    </div>
    <div class="manual">
      <h4>3. View or edit the diary entry</h4>
      <p>You can view the details of a selected diary entry and make edits if something is incorrect or needs updating. You can even remove the entry if needed.</p>
      <img src={image04} alt="Diary Step 3" />
      <p>After editing, click the "Apply" button to save.</p>
      <img src={image05} alt="Diary Step 3" />      
    </div>
    <div class="manual">
      <h4>4. View Summary</h4>
      <p>The summary page provides an overview of your diary entries, allowing you to quickly assess your plant's health and growth trends. Select one of the plants to see detailed summaries.</p>
      <img src={image06} alt="Diary Step 4" />
    </div>
    

  </div>
</main>


<style>
 
  p{
    margin-bottom: 0;
    margin-top: 10px;
  }
  .center{
    text-align: center;
  }
  .manuals{
    display: flex;
    flex-direction: column;
    align-items: center;
    min-width: 300px;
    max-width: 1000px;
    height: fit-content;
    margin: 20px auto;
    padding: 15px;
    border: 2px solid black;
    border-radius: 30px;
    background-color: rgba(240, 253, 255, 0.801);
    box-shadow: 0px 0px 10px rgb(0, 0, 0);
  }
  .manual{
    display: flex;
    flex-direction: column;
    margin: 10px 0;
    padding: 15px;
    border: 1px solid gray;
    border-radius: 20px;
    background-color: rgb(255, 255, 255);
  }

  img {
    width: auto;
    max-width: 100%;
    border: 2px solid rgb(0, 134, 0);
    border-radius: 15px;
    max-height: 600px;
    margin: 5px auto;
  }

</style>
