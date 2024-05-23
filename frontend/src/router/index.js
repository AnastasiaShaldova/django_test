import { createRouter, createWebHistory } from 'vue-router'
import ImageList from '../views/ImageList.vue'

const routes = [
  {
    path: '/',
    name: 'Главная',
    component: ImageList
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router