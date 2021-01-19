import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import ArticleView from "@/views/ArticleView.vue"
import ArticlesView from "@/views/ArticlesView.vue"
import LoginView from "@/views/LoginView.vue"
import NewView from "@/views/NewView.vue"

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    // name: 'Home',
    // component: Home
    redirect: '/articles'
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/article/:id',
    name: "Article",
    component: ArticleView
  },
  {
    path: '/articles',
    name: "Articles",
    component: ArticlesView
  },
  {
    path: '/login',
    name: "Login",
    component: LoginView
  },
  {
    path: '/new',
    name: "New",
    component: NewView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
