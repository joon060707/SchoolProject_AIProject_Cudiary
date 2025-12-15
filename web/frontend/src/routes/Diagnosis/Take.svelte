<script lang="ts">
// import {formidable} from 'formidable';
import logo from '../../assets/CDR.png'
import MenuTitle from '../../lib/MenuTitle.svelte';
import Top from '../../lib/Top.svelte';
import logo_search from '../../assets/search.svg'
import ParaDeco from '../../lib/ParaDeco.svelte';

// let data = $state(""); // local state variable

///////Webcam////////

// Run the initialization when the component is mounted
$effect(() => {
  // This will run when the component is mounted
  initializeWebcam();
});

// ref: https://developer.mozilla.org/en-US/docs/Web/API/Media_Capture_and_Streams_API/Taking_still_photos
function initializeWebcam() {

  const width = 1024; // We will scale the photo width to this
  let height = 0; // This will be computed based on the input stream

  let streaming = false;

  const video: HTMLVideoElement = document.getElementById("video") as HTMLVideoElement;
  const canvas: HTMLCanvasElement = document.getElementById("canvas") as HTMLCanvasElement;
  const photo: HTMLImageElement = document.getElementById("photo") as HTMLImageElement;
  const startButton: HTMLButtonElement = document.getElementById("start-button") as HTMLButtonElement;
  const allowButton: HTMLButtonElement = document.getElementById("permissions-button") as HTMLButtonElement;
  const sendButton: HTMLButtonElement = document.getElementById("send") as HTMLButtonElement;
  allowButton.addEventListener("click", () => {

    console.log("Requesting camera access...");
    navigator.mediaDevices
      .getUserMedia({ video: true, audio: false })
      .then((stream) => {
        video.srcObject = stream;
        video.play();
        allowButton.style.display = "none";
        startButton.style.display = "block";
      })
      .catch((err) => {
        console.error(`An error occurred: ${err}`);
        // 
        alert("Please allow camera access:\ngo to site settings and enable camera permission.\nedge://settings/privacy/sitePermissions/allPermissions/camera");
      });
  });
  video.addEventListener("canplay", (ev) => {
    if (!streaming) {
      height = video.videoHeight / (video.videoWidth / width);

      video.setAttribute("width", `${width}`);
      video.setAttribute("height", `${height}`);
      canvas.setAttribute("width", `${width}`);
      canvas.setAttribute("height", `${height}`);
      streaming = true;
    }
  });

  // take button event
  startButton.addEventListener("click", (ev) => {
    takePicture();
    ev.preventDefault();
  });

  // upload button event
  sendButton.addEventListener("click", (ev) => {
    // upload the captured photo
    files.accepted = [];

    const dataUrl = photo.getAttribute("src");
    if (dataUrl) {
      fetch(dataUrl)
        .then(res => res.blob())
        .then(blob => {
          const file = new File([blob], Date.now() + "capture.png", { type: "image/png" });
          files.accepted = [file];
          console.log("Captured file for upload:", file);
          send(); // call the send function to upload
        });
    }

    ev.preventDefault();
  });

  // if want to clear photo
  // function clearPhoto() {
  //   const context = canvas.getContext("2d");
  //   context.fillStyle = "#aaaaaa";
  //   context.fillRect(0, 0, canvas.width, canvas.height);

  //   const data = canvas.toDataURL("image/png");
  //   photo.setAttribute("src", data);
  // }
  // clearPhoto();

  function takePicture() {
    const context = canvas.getContext("2d");
    if (width && height) {
      canvas.width = width;
      canvas.height = height;

      // Get the computed CSS filter from the video element.
      // For example, it might return "grayscale(100%)"
      // const videoStyles = window.getComputedStyle(video);
      // const filterValue = videoStyles.getPropertyValue("filter");

      // // Apply the filter to the canvas drawing context.
      // // If there's no filter (i.e., it returns "none"), default to "none".
      // context.filter = filterValue !== "none" ? filterValue : "none";

      // Draw the video frame to the canvas
      context.drawImage(video, 0, 0, width, height);

      // set photo src to the captured image
      const dataUrl = canvas.toDataURL("image/png");
      photo.setAttribute("src", dataUrl);

      // Show the send button
      sendButton.style.display = "block";
    } else {
      // clearPhoto();
    }
  }

}

///////////////

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

</script>


<Top />
<main>
  <MenuTitle title="Diagnosis" icon={logo_search} />
  <ParaDeco color="white_transparent" title="Take a plant photo for diagnosis." size="12" shadow="shadow" />
  <div class="buttons">
    <button id="permissions-button" class="bten">Allow camera</button>
    <button id="start-button" class="bten" style="display: none;">Capture photo</button>
    <button id="send" class="bten" style="display: none;">Upload photo</button>
  </div>   
  <div class="webcam-container">   
      <div class="camera">
        <p class="center">Preview</p>
        <video id="video" poster="{logo}" >Camera not available.</video>
      </div>
      <canvas id="canvas" style="display: none;"></canvas>
      <div class="output">
        <p class="center">Captured Image</p>
        <img id="photo" src="{logo}" alt="The screen capture will appear in this box." />
      </div>
  </div>

</main>


<style>
 
  .center{
    text-align: center;
  }


  .buttons {
    display: flex;
    justify-content: center;
    flex-direction: row;
  }

  .bten{
    transition: background-image 300ms, background-color 300ms, filter 300ms;
    background-image: url('../../assets/btbg.png');
    background-size: cover;
    padding: 10px 20px;
    margin: 20px;
    font-size: 12pt;
    border: 5px solid white;
    border-radius: 20px;
    box-shadow: 5px 5px 5px rgb(78, 78, 78);
  }
  .bten:hover {
    background-image: none;
    background-color: #e5ff89;
    border: 5px solid #8383ff;
    filter: drop-shadow(0 0 2em #050a68aa);
  }  

  .webcam-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    background-color: antiquewhite;
    height: fit-content;
    width: 90%;
    max-width: 1600px;
    margin: 0 auto;
    padding: 20px;
  }

  #video, #photo {
    display: block;
    margin: 20px auto;
    width: 90%;
    max-width: 600px;
    height: auto;
  }

</style>
