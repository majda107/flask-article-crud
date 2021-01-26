import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import ArticleView from "@/views/ArticleView.vue"
import ArticlesView from "@/views/ArticlesView.vue"
import LoginView from "@/views/LoginView.vue"
import NewView from "@/views/NewView.vue"
import EditorView from "@/views/EditorView.vue"
import PageView from "@/views/PageView.vue"
import PagesView from "@/views/PagesView.vue"
import PageDetailView from "@/views/PageDetailView.vue"

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
  },
  {
    path: '/editor',
    name: "View",
    component: EditorView
  },
  {
    path: '/page/:name',
    name: "Page",
    component: PageView
  },
  {
    path: '/pages',
    name: "Pages",
    component: PagesView,

    children: [
      {
        path: '/pages/:name',
        component: PageDetailView
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
