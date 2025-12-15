<script lang="ts">
import { link } from 'svelte-spa-router'
let props = $props(); // get props passed to this component  
let its = $state<string[]>([]);

if (props.title === "Unit") {
  its = ["Whole plant", "Single organ"];
} else if (props.title === "Type") {
  its = ["Leaf", "Flower", "Fruit"];
} else if (props.title === "Stage") {
  its = ["Seedling", "Vegetative", "Flowering", "Fruiting"];
} else if (props.title === "Health") {
  its = ["Healthy", "Should be harvested", "Too early flowering", "Too late flowering", "Chlorophyll deficiency"];
} else if (props.title === "Chlorophyll") {
  its = ["Low", "Normal", "High"];
}
// else if (props.title === "Measurement") {
//   its = Array.from({ length: 101 }, (_, i) => i.toString());
// }






</script>

    <!-- unit = random_choice("Whole plant", "Single organ")
    organ_type = random_choice("Leaf", "Stem", "Fruit")
    growth_stage = random_choice("Seedling", "Vegetative", "Flowering", "Fruiting")

    diagnosis = random_choice("Healthy", "Disease A", "Disease B", "Nutrient Deficiency")
    chlorophyll_content = random_choice("Normal", "Low", "High")
    measurement = random.randint(0, 100) -->


<!-- apply color -->
<div class="roundbox {props.color}"> 
  <p class="i"></p>
  <h4>{props.title}</h4>
  <select id={props.title} class="desc" value={props.description}>
    {#each its as it}
      <option value={it}>{it}</option>
    {/each}
  </select>
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

  .abnormal{
    background-color: #ffc772;
  }
  .emergency{
    background-color: #ff6666;
  }

  </style>