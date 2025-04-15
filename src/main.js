import { createApp } from 'vue'
import App from './App.vue'
import './style.css'
import { initParticles } from './particles'

document.addEventListener('DOMContentLoaded', () => {
  initParticles();
});

createApp(App).mount('#app')