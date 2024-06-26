import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/profileview/ProfileView.vue'
import MyInfoView from '@/views/profileview/MyInfoView.vue'
import SubscriptionProductView from '@/views/profileview/SubscriptionProductView.vue'
import RecommendProductView from '@/views/profileview/RecommendProductView.vue'
import ProductListView from '@/views/product/ProductListView.vue'
import ProductDetailView from '@/views/product/ProductDetailView.vue'
import ERView from '@/views/ERView.vue'
import MapView from '@/views/MapView.vue'
import ArticleListView from '@/views/article/ArticleListView.vue'
import ArticleDetailView from '@/views/article/ArticleDetailView.vue'
import ArticleCreateView from '@/views/article/ArticleCreateView.vue'
import {useProjectStore} from '@/stores/project.js'

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
      component: ProfileView,
      children: [
        {
          path: '',
          name: 'profile',
          component: MyInfoView
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
      ]
    },
    {
      path: '/productlist',
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
]
})

router.beforeEach((to, from, next) => {
  const store = useProjectStore()
  // console.log(to.name);
  if (store.isLogin && (to.name==='signup' || to.name==='login')){
    alert('이미 로그인 되어 있습니다.')
    next({name: 'mainpage'})
    return
  }
  if (!store.isLogin && (to.name==='profile' || to.name==='subscriptionproduct' || to.name==='recommendproduct' || to.name==='articlecreate')){
    alert('로그인이 필요한 서비스입니다.')
    next({name: 'login'})
    return
  }
  next()
})

export default router
