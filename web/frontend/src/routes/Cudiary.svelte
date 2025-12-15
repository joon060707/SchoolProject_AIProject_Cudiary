<script>
  import logo from '../assets/CDR.png'
  import logo_search from '../assets/search.svg'
  import logo_diary from '../assets/diary.svg'
  import logo_manual from '../assets/help.svg'
  import MB from '../lib/MenuButton.svelte'

</script>

<main>
  <div class="logo" >
      <img id="logoImg" src={logo} alt="Logo" />
      <h1>Cudiary</h1>
  </div>
  <h4>Welcome to Cudiary!</h4>

    <div class="buttonset">
            <MB title={"Diagnosis"} site={"/diagnosis"} icon={logo_search} size="large" />
            <MB title={"Diary"} site={"/diary"} icon={logo_diary} size="large" />
            <MB title={"Manual"} site={"/manual"} icon={logo_manual} size="large" />
    </div>

  <p class="center">Version 1.0.0 (c) 2025 Cudiary</p>

</main>

<style>
    h4{
        text-align: center;
    }
    h1{
        margin: auto 10px;
    }
  .logo {
    margin: 10px auto;
    display: flex;
    flex-wrap: wrap;
    padding: 1.5em;
    justify-content: center;
  }

  .buttonset{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-bottom: 20px;
  }

  #logoImg {
    height: 120px;
    margin-right: 30px;
  }

  .center{
    text-align: center;
  }


</style>
