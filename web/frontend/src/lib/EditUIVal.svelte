<script lang="ts">
  import { link } from 'svelte-spa-router'
  let props = $props(); // get props passed to this component  


  function max200(event) {
    if(event.target.value > 200) {
      event.target.value = 200;
    } else if(event.target.value < 0) {
      event.target.value = 0;
    }

  }

// $effect(() => {
//     // set textarea height by counting newlines from description
//   let lines = props.description.split('\n').length; 
//   let textarea = document.getElementsByClassName('comment')[0] as HTMLTextAreaElement;
//   if(textarea) {
//     textarea.style.height = (lines * 25) + 'px';
//   }

// });

</script>

<!-- apply color -->

<div class="roundbox {props.color} {props.wide ? 'wide' : ''}"> 
  <p class="i"></p>
  {#if props.wide}
    <h5 style="text-align: left;">{props.title}</h5>
  {:else}
    <h4>{props.title}</h4>
  {/if}

  {#if props.comment}
    <textarea id={props.title} class="comment" bind:value={props.description}></textarea>
  {:else}
  <input id={props.title} class="desc" type="number" min="0" max="200" oninput={max200} value={props.description} />
  {/if}
</div>





<style>

  h4{
    margin-bottom: 40px;
  }

  .desc{
    text-align: right;
    font-size: 14pt;
    border: none;
    width: 100%;
    height: 36px;
    background-color: rgba(255, 255, 255, 0.5);
  }

  .comment{
    font-size: 12pt;
    width: calc(100%);
    text-align: left;
    background-color: rgba(255, 251, 190, 0.5);
    height: fit-content;
    field-sizing: content;
  }

 
  .roundbox{
    border: 3px solid rgb(255, 255, 255);
    border-radius: 20px;
    box-shadow: 7px 7px 10px rgb(78, 78, 78);
    padding: 5px 15px;
    margin: 15px auto;
    /* background-color: #f0f8ff; */
    width: 200px;
    height: fit-content;
  }

  .wide{
    width: calc(100% - 60px);
  }

  /* apply color */
  .red{
    background-color: #ffcccc;
  }
  .green{
    background-color: #ccffcc;
  }
  .blue{
    background-color: #ccccff;
  }
  .transparent{
    background-color: #ffffff80;
  }

  .abnormal{
    background-color: #ffc772;
  }
  .emergency{
    background-color: #ff6666;
  }

  </style>