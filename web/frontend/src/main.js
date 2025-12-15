import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.min.js'
import { mount } from 'svelte'
import './app.css'
import App from './Main.svelte'

const app = mount(App, {
  target: document.getElementById('cudiary'),
})

export default app
