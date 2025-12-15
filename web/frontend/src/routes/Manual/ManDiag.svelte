<script>
import Top from '../../lib/Top.svelte'
import MenuTitle from '../../lib/MenuTitle.svelte';
import logo from '../../assets/CDR.png'
import logo_manual from '../../assets/search.svg'
import image01 from '../../assets/manual/diag_01.png'
import image02 from '../../assets/manual/diag_02.png'
import image03 from '../../assets/manual/diag_03_1.png'
import image04 from '../../assets/manual/diag_03_2.png'
import image05 from '../../assets/manual/diag_03_3.png'
import image06 from '../../assets/manual/diag_04_1.png'
import image07 from '../../assets/manual/diag_04_2.png'
import image08 from '../../assets/manual/diag_05.png'
import image09 from '../../assets/manual/diag_06.png'

</script>


<Top />
<main>
  <MenuTitle title="Diagnosis Manual" icon={logo_manual} />

  

  <div class="manuals">
    <h3 class="center">How to use the Diagnosis Feature</h3>
    <p>This section will provide detailed instructions on how to use the diagnosis feature. Please refer to the following steps:</p>
    <div class="manual">
      <h4>1. Click "Diagnosis"</h4>
      <p>In the main menu, click on the "Diagnosis" button.</p>
      <img src={image01} alt="Diagnosis Step 1" />
    </div>
    <div class="manual">
      <h4>2. Select upload method</h4>
      <p>We support uploading images from your device or capturing a new photo using your camera.</p>
      <img src={image02} alt="Diagnosis Step 2" />
    </div>
    <div class="manual">
      <h4>3-1. (Take) Take a photo</h4>
      <p>If you click "Take", please allow access to your camera through "Allow camera".</p>
      <img src={image03} alt="Diagnosis Step 3" />
      <p>Now, the camera is open. Please take a photo through "Capture photo".</p>
      <img src={image04} alt="Diagnosis Step 3" />
      <p>You can retake the photo if needed. If satisfied, proceed to the next step through "Upload photo".</p>
      <img src={image05} alt="Diagnosis Step 3" />      
    </div>
    <div class="manual">
      <h4>3-2. (Upload) Upload a photo</h4>
      <p>If you click "Upload", please select a photo from your device. You can either drag-and-drop the photo or use the file selector.</p>
      <img src={image06} alt="Diagnosis Step 4" />
      <p>The image will be uploaded immediately.</p>
      <img src={image07} alt="Diagnosis Step 4" />
    </div>
    <div class="manual">
      <h4>4. Add information about the plant</h4>
      <p>If the image contains existing plant, please select the plant from the list. If not, you can add a new plant.
        Please select the correct growth start date. You can also add some memo.</p>
      <p>Then, click "Send" to proceed with the diagnosis. It may take some time to process.</p>
      <img src={image08} alt="Diagnosis Step 5" />
    </div>
    <div class="manual">
      <h4>5. Diagnosis Result</h4>
      <p>The diagnosis result will be displayed here. You can review the details and take actions based on the information provided.</p>
      <img src={image09} alt="Diagnosis Step 6" />
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
