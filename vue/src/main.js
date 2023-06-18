//import { createApp, createElementBlock } from 'vue'
import { createApp } from 'vue'



// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

import axios from 'axios'

import App from './App.vue'
import router from './router'

//createApp(App).mount('#app')  

const app = createApp(App)

app.config.globalProperties.$axios = axios
window.axios = axios
app.use(router)
app.use(VueSweetalert2);
app.mount('#app')