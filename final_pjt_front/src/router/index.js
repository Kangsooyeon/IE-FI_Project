import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/profileview/ProfileView.vue'
import MyInfoView from '@/views/profileview/MyInfoView.vue'
import MyInfoUpdateView from '@/views/profileview/MyInfoUpdateView.vue'
import SubscriptionProductView from '@/views/profileview/SubscriptionProductView.vue'
import RecommendProductView from '@/views/profileview/RecommendProductView.vue'
import MyAnCView from '@/views/profileview/MyAnCView.vue'
import ProductListView from '@/views/product/ProductListView.vue'
import ProductDetailView from '@/views/product/ProductDetailView.vue'
import ERView from '@/views/ERView.vue'
import MapView from '@/views/MapView.vue'
import ArticleListView from '@/views/article/ArticleListView.vue'
import ArticleDetailView from '@/views/article/ArticleDetailView.vue'
import ArticleCreateView from '@/views/article/ArticleCreateView.vue'
import ArticleUpdateView from '@/views/article/ArticleUpdateView.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'mainpage',
      component: MainPageView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
      children: [
        {
          path: 'myinfo',
          name: 'myinfo',
          component: MyInfoView
        },
        {
          path: 'myinfoupdate',
          name: 'myinfoupdate',
          component: MyInfoUpdateView
        },
        {
          path: 'subscriptionproduct',
          name: 'subscriptionproduct',
          component: SubscriptionProductView
        },
        {
          path: 'recommendproduct',
          name: 'recommendproduct',
          component: RecommendProductView
        },
        {
          path: 'myanc',
          name: 'myanc',
          component: MyAnCView
        }
      ]
    },
    {
      path: '/product',
      name: 'productlist',
      component: ProductListView
    },
    {
      path: '/product/:fin_prdt_cd',
      name: 'productdetail',
      component: ProductDetailView
    },
    {
      path: '/er',
      name: 'er',
      component: ERView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/article',
      name: 'articlelist',
      component: ArticleListView
    },
    {
      path: '/article/create',
      name: 'articlecreate',
      component: ArticleCreateView
    },
    {
      path: '/article/:id',
      name: 'articledetail',
      component: ArticleDetailView
    },
    {
      path: '/article/:id/update',
      name: 'articleupdate',
      component: ArticleUpdateView
    },
]
})

export default router
