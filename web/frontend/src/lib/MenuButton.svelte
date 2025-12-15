<script>
  import { link } from 'svelte-spa-router'
  let props = $props(); // get props passed to this component  


</script>

<a use:link href={props.site}>
<button class={props.size}>
  {#if props.size == "large" || props.size == undefined}
  <img class={`icon ilarge`} src={props.icon} alt={props.title} />
  {/if}
  {props.title}</button>
</a>

<style>
  button {
    /* will-change: filter; */
    transition: background-image 300ms, background-color 300ms, filter 300ms;
    background-image: url('../assets/btbg.png');
    background-size: cover;
    padding: 10px;

  }

  .large{
    margin: 30px;
    font-size: 24pt;
    width: 250px; /* default width */
    height: 140px; /* default height */
    border: 5px solid white;
    border-radius: 40px;
    box-shadow: 7px 7px 10px rgb(78, 78, 78);
  }

  .small{
    margin: 20px;
    font-size: 12pt;
    width: 250px; /* default width */
    /* height: 140px; */
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

  .icon{
    margin-right: 15px;
    vertical-align: middle;
  }

  .ilarge {
    height: 40px;
  }
  .ismall {
    height: 20px;
  }
  </style>