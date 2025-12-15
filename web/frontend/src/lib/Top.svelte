<script>
  import { link } from 'svelte-spa-router'


  

  // compute back target
  var back = document.URL.split('/')[document.URL.split('/').length-1];
  var target = document.URL.replace("http://localhost:5173/", '');
  target = target.replace(back, '');
  // if(target === "#/")
  //   target = "http://localhost:5173/#";
  if(target.endsWith('/'))
    target = target.substring(0, target.length - 1);
  console.log("back target:", target);

</script>

<div class="backset">
  <a use:link href={target}>
  <button >{"<"}</button>
  </a>
</div>

<style>
  button{
    width: 80px;
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
    position: fixed;
    top: 10px;
    left: 10px;
  }

</style>