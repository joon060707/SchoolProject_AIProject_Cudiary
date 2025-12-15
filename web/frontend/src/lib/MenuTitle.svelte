<script>
  let props = $props(); // get props passed to this component  
</script>

<div class="menutitle">
  {#if props.icon}
  <img class="icon" src={props.icon} alt={props.title} />
  {/if}
    <p class="center text_dark" style="margin: 0px;">{props.title}</p>
</div>


<style>

  .menutitle{    
    overflow-x: auto; /* Enables horizontal scrolling if content overflows */
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 30px auto;
    width: fit-content;
    padding: 0px 50px;
    height: 100px;
    font-size: 30pt;
    /* background-color: lightgray; */

    /* wrapped with rounded corners, white background */
    border-radius: 40px;
    background-color: rgba(255, 255, 255, 0.63);
  }

  .center{
    text-align: center;
  }

  .text_dark{
    color: rgb(0, 99, 38);
  }

  .icon{
    height: 40px;
    margin-right: 20px;
    vertical-align: middle;
  }
</style>