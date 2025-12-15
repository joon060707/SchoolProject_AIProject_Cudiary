<script>
  import Router from 'svelte-spa-router'

  // list of routes
  import Cudiary from "./routes/Cudiary.svelte"
  import Newpage from "./routes/[Newpage].svelte"

  // Diary related pages
  import Diary from "./routes/Diary/Diary.svelte"
  import View from "./routes/Diary/View.svelte"
  import Edit from "./routes/Diary/Edit.svelte"
  import Summary from "./routes/Diary/Summary.svelte"

  // Diagnosis related pages
  import Diagnosis from "./routes/Diagnosis/Diagnosis.svelte"
  import Take from './routes/Diagnosis/Take.svelte'
  import Upload from './routes/Diagnosis/Upload.svelte'
  import Process from './routes/Diagnosis/Process.svelte'
  import Result from './routes/Diagnosis/Result.svelte'

  // Manual related pages
  import Manual from "./routes/Manual/Manual.svelte"
  import ManDiag from "./routes/Manual/ManDiag.svelte"
  import ManDiary from "./routes/Manual/ManDiary.svelte"
  import ManSeed from "./routes/Manual/ManSeed.svelte"
  import ManVege from "./routes/Manual/ManVege.svelte"
  import ManFlower from "./routes/Manual/ManFlower.svelte"
  import ManFruit from "./routes/Manual/ManFruit.svelte"


  const routes = {
    '/': Cudiary, // http://localhost:5173/#/
    '/diagnosis': Diagnosis, // http://localhost:5173/#/diagnosis
    '/diagnosis/upload' : Upload, // http://localhost:5173/#/diagnosis/upload
    '/diagnosis/take' : Take, // http://localhost:5173/#/diagnosis/take
    '/diagnosis/process' : Process, // http://localhost:5173/#/diagnosis/process
    '/diagnosis/result' : Result, // http://localhost:5173/#/diagnosis/result

    '/diary': Diary, // http://localhost:5173/#/diary
    '/diary/:id': View, // http://localhost:5173/#/diary/:id
    '/diary/:id/edit': Edit, // http://localhost:5173/#/diary/:id/edit    
    '/summary': Summary, // http://localhost:5173/#/summary

    '/manual': Manual, // http://localhost:5173/#/manual
    '/manual/diagnosis': ManDiag, // http://localhost:5173/#/manual/diagnosis
    '/manual/diary': ManDiary, // http://localhost:5173/#/manual/diary
    '/manual/germination': ManSeed, // http://localhost:5173/#/manual/seed
    '/manual/vegetative': ManVege, // http://localhost:5173/#/manual/vegetable
    '/manual/flowering': ManFlower, // http://localhost:5173/#/manual/flower
    '/manual/fruit-setting': ManFruit, // http://localhost:5173/#/manual/fruit

    '/*': Newpage, // http://localhost:5173/#/anything/else
    // default: Newpage,
    // ':id': Newpage, // http://localhost:5173/#/123
  }
</script>

<!-- This is the main router outlet -->
<Router {routes}/>