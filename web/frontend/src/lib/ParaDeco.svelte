<script>
  let props = $props(); // get props passed to this component  
</script>

<div class="roundbox b_{props.color} f{props.size} {props.shadow}">
    <p id={props.id} class="center {props.textColor} {props.bold} f{props.size}" style="margin: 0px;">{props.title}</p>
</div>


<style>

  .roundbox{    
    overflow-x: auto; /* Enables horizontal scrolling if content overflows */
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 15px auto;
    width: fit-content;
    padding: 5px 30px;
  }

/* text size */
  .f12{
    font-size: 12pt;
    border-radius: 15px;
  }
  .f20{
    font-size: 20pt;
    border-radius: 20px;
  }
  .f24{
    font-size: 24pt;
    border-radius: 30px;
    padding: 5px 15px;
  }
  .f30{
    font-size: 30pt;
    border-radius: 40px;
    padding: 5px 10px;
  }
  .f36{
    font-size: 36pt;
    border-radius: 50px;
    padding: 5px 10px;
  }

  /* background colors */
  .b_gray{
        background-color: rgba(228, 228, 228, 0.842);
  }

  .b_white{
        background-color: rgba(255, 255, 255, 0.836);
  }

  .b_white_transparent{
        background-color: rgba(255, 255, 255, 0.5);
  }

  .b_lightgreen{
        background-color: rgba(200, 255, 200, 0.658);
  }
  .b_abnormal{
        background-color: rgba(253, 213, 213, 0.795);
  }

  .center{
    text-align: center;
  }
/* text colors */
  .green{
    color: rgb(0, 99, 38);
  }

  .darkblue{
    color: rgb(0, 8, 124);
  }

  .gray{
    color: rgb(75, 75, 75);
  }

  .bold{
    font-weight: bold;
  }

</style>