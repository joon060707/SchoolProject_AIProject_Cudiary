<script lang="ts">
  import { link } from 'svelte-spa-router'
  let props = $props(); // get props passed to this component  

  

</script>


<!-- apply color -->
<div class="roundbox {props.color} {props.wide ? 'wide' : ''}"> 
  <p class="i"></p>
  {#if props.wide}
    <h5 style="text-align: left;">{props.title}</h5>
  {:else}
    <h4>{props.title}</h4>
  {/if}
  <p id="comment_txt" class="{props.wide ? 'comment' : 'desc'}">{props.description}</p>
</div>





<style>

  h4{
    margin-bottom: 40px;
  }

  .desc{
    text-align: right;
    font-size: 14pt;
    
    /* height: 20px; */
  }

  .comment{
    font-size: 12pt;
    text-align: left;
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