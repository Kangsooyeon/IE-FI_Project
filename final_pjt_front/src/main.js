import { createApp } from 'vue'
import { createPinia } from 'pinia'
import vuetify from './plugins/vuetify'

import App from './App.vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap.css'
import { Tooltip, Toast, Popover } from 'bootstrap';

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.use(vuetify)
app.mount('#app')
