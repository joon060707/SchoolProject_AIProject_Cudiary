<script>
import logo from '../../assets/CDR.png'
import MenuTitle from '../../lib/MenuTitle.svelte';
import Top from '../../lib/Top.svelte'
import Dropzone from "svelte-file-dropzone";
import logo_search from '../../assets/search.svg'
import ParaDeco from '../../lib/ParaDeco.svelte';

// let data = $state(""); // local state variable

// file selection handling
let files = {  accepted: [], rejected: []};

// file upload handling
const send = function() {
  const file = files.accepted[0]; // Get the first selected file

  if (file) {
      const formData = new FormData();
      formData.append('file', file); // 'uploadedFile' is the key the server will use

      // Using Fetch API
      // 요청 시작
      fetch('http://localhost:3000/upload', { // Replace with your server-side upload endpoint
          method: 'POST',
          // headers: {
          //     // enctype: 'multipart/form-data', // 파일 형식 확인
          //     // "Content-Type": "multipart/form-data",
          //     // "Access-Control-Allow-Origin": "http://localhost:3000",
          //     // "Access-Control-Allow-Headers": "Content-Type, Authorization"
          // },
          // mode: 'no-cors', // can be vulnerable
          body: formData
      })
      .then(data => {

          // If you need to process the response from the server
          // For example, you might want to display the uploaded image
          data.body.getReader().read().then(({ done, value }) => {
              if (!done) {
                  var addr = new TextDecoder('utf-8').decode(value);
                  // {status: 'success', filepath: 'http://localhost:3000/upload/1762245318685-1762245318672captured_image.png'}
                  console.log('Upload successful:', addr);
                  // Handle success (e.g., display a message)

                  alert('File uploaded successfully!');
                  // document.getElementById('send').removeEventListener('click', send);

                  // if there is a valid address, send it to backend
                  cookieStore.set({ name: 'uploaded_image_url', value: addr, path: '/' });
                  window.location.href = '#/diagnosis/process'; // redirect to process page



                  
                  // if there is a valid address, send it to backend
                  // const urlData = new FormData();
                  // urlData.append('url', addr);

                  // fetch(`http://localhost:8000/url-upload/`, {
                  //     method: 'POST',
                  //     body: urlData
                  // })
                  // .then(response => response.json())
                  // .then(data => {
                  //     console.log('Response from server:', data);
                  //     // Handle the server response
                  // })
                  // .catch(error => {
                  //     console.error('Error sending URL to backend:', error);
                  // });

              }
          });

      })
      .catch(error => {
          console.error('Error during upload:', error);
          // Handle error
      });

  } else {
      console.warn('No file selected.');
  }
};

function handleFilesSelect(e) {
  const { acceptedFiles, fileRejections } = e.detail;
  files.accepted = [...acceptedFiles];
  files.rejected = [...fileRejections];

  if(acceptedFiles.length === 0){
    alert("Invalid file. Please select an image file.");
    return;
  }

  // You can now process the acceptedFiles, e.g., upload them to a server
  console.log("Accepted files:", files.accepted[0]);
  // document.getElementById("result").innerText = `Selected file: ${files.accepted[0].name}`;
  try{
    document.getElementById("preview").src = window.URL.createObjectURL(files.accepted[0]); // no problem

    // document.getElementById("send").style.display = "block";  
    // document.getElementById('send').addEventListener('click', send);  // manual send
    send(); // auto send upon file selection

  }
  catch(err){
    console.error("Error displaying preview:", err);
  }




  
}




</script>


<Top />
<main>
  <MenuTitle title="Diagnosis" icon={logo_search} />

  <ParaDeco color="white_transparent" title="Upload a plant photo for diagnosis." size="12" shadow="shadow" />
  <div class="dropzone-container">
    <Dropzone on:drop={handleFilesSelect} accept={["image/*"]} multiple={false} />
    <!-- <p id="result"></p> -->
    <img id="preview" src="{logo}" />
    <button id="send" class="btn btn-primary" style="display: none;">Send</button>  
    <!--   -->
    <!-- <input id="submit" type="submit" value="Send" class="btn btn-primary" style="display: none;" /> -->
  </div>
  <!-- <form method="post" enctype="multipart/form-data">  </form> -->


</main>


<style>
 
  .center{
    text-align: center;
  }



  .dropzone-container {
    background-color: antiquewhite;
    height: fit-content;
    width: 90%;
    max-width: 1000px;
    margin: 0 auto;
    padding: 20px;
  }

  #preview {
    display: block;
    margin: 20px auto;
    width: 90%;
    max-width: 800px;
    height: auto;
  }

  #send {
    display: block;
    margin: 20px auto;
    padding: 10px 20px;
    font-size: 18px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

</style>
