import { createApp } from 'vue';
import { createPinia } from 'pinia';
import vuetify from './plugins/vuetify';
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate';

import App from './App.vue';
import router from './router';

import 'bootstrap/dist/css/bootstrap.css';
import { Tooltip, Toast, Popover } from 'bootstrap';

const app = createApp(App);
const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);
app.use(pinia);

app.use(vuetify);
app.use(router);

app.mount('#app');
