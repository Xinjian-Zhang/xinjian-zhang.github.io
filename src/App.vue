<template>
  <div id="particles-js"></div>
  <div class="container mx-auto px-4 min-h-screen relative z-10">
    <div class="language-selector absolute top-4 right-4 flex space-x-2">
      <button v-for="lang in languages" :key="lang.code" @click="setLanguage(lang.code)" 
              class="w-10 h-10 rounded-full flex items-center justify-center transition-transform hover:scale-110">
        <img :src="lang.flag" :alt="lang.name" class="w-6 h-6 rounded-full">
      </button>
    </div>
    
    <div class="flex flex-col items-start justify-center min-h-screen py-10">
      <div class="max-w-4xl p-6 md:p-8 mb-10 w-full md:w-auto">
        <h1 class="text-3xl md:text-4xl mb-2">{{ content.hello }}</h1>
        <h2 class="text-2xl md:text-3xl mb-6">
          {{ content.im }}
  <span class="highlight-name bg-white/20 px-2 py-1 rounded text-3xl md:text-4xl">
    {{ content.name }}
  </span>
</h2>

        
        <div class="mb-6">
          <p class="flex flex-wrap items-center mb-3">
            <span class="mr-2">✨</span> {{ content.passionate }} ˅
          </p>
          <p class="flex flex-wrap items-center mb-3">
            <span class="font-semibold mx-1 ml-8 text-base">{{ content.productMgmt }}, {{ content.productOps }}, {{ content.techWriting }}</span>
            {{ content.and }}
            <span class="font-semibold ml-1 text-base">{{ content.frontendDev }}</span>
          </p>
          
          <p class="flex flex-wrap items-center mb-3">
            <span class="mr-2">💕</span> {{ content.lover }} 
            <span class="ml-1">🍺</span> {{ content.craftBeer }},
            <span class="ml-1">🎸</span> {{ content.jrock }}  {{ content.and }} 
            <span class="ml-1">🏍️</span> {{ content.motorcycle }}
          </p>
          
          <p class="flex flex-wrap items-center">
            <span class="mr-2">🏠</span> {{ content.springCity }} -- {{ content.kunming }}
          </p>
        </div>
        
        <div class="flex flex-wrap gap-4">
          <a href="https://github.com/Xinjian-Zhang" target="_blank" class="px-5 py-2 rounded-lg flex items-center transition-all hover:bg-white/20">
            <div class="w-7 h-7 rounded-full bg-white/10 flex items-center justify-center mr-3">
              <svg class="w-4 h-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
              </svg>
            </div>
            Github
          </a>
          <a href="mailto:1xinjian.zhang@gmail.com" class="px-5 py-2 rounded-lg flex items-center transition-all hover:bg-white/20">
            <div class="w-7 h-7 rounded-full bg-white/10 flex items-center justify-center mr-3">
              <svg class="w-4 h-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                <polyline points="22,6 12,13 2,6"></polyline>
              </svg>
            </div>
            E-mail
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, reactive } from 'vue'
import { gsap } from 'gsap'

export default {
  name: 'App',
  setup() {
    const currentLang = ref('zh')
    
    const languages = [
      {
        code: 'zh',
        name: '中文',
        flag: '/src/assets/china.png'
      },
      {
        code: 'en',
        name: 'English',
        flag: '/src/assets/united-kingdom.png'
      },
      {
        code: 'lv',
        name: 'Latviešu',
        flag: '/src/assets/latvia.png'
      },
      {
        code: 'ja',
        name: '日本語',
        flag: '/src/assets/japan.png'
      }
    ]
    
    const translations = {
      zh: {
        hello: '你好。',
        im: '我是',
        name: '张新健',
        passionate: '热衷于',
        productMgmt: '产品管理',
        productOps: '产品运营',
        techWriting: '技术写作',
        and: '和',
        frontendDev: '前端开发',
        lover: '热爱',
        craftBeer: '精酿啤酒',
        jrock:'日本摇滚乐',
        motorcycle: '摩旅',
        springCity: '春城',
        kunming: '昆明, 云南, 中国'
      },
      en: {
        hello: 'Hello.',
        im: 'I\'m',
        name: 'Xinjian Zhang',
        passionate: 'Passionate about',
        productMgmt: 'Product Management',
        productOps: 'Product Operations',
        techWriting: 'Technical Writing',
        and: 'and',
        frontendDev: 'Frontend Development',
        lover: 'Lover of',
        craftBeer: 'Craft Beer',
        jrock:'Japanese Rock',
        motorcycle: 'Motorcycle Touring',
        springCity: 'Spring City',
        kunming: 'Kunming, Yunnan, China'
      },
      lv: {
        hello: 'Sveiki.',
        im: 'Es esmu',
        name: 'Sjiņdzjana Džan',
        passionate: 'Aizrautīgs par',
        productMgmt: 'Produktu vadību',
        productOps: 'Produktu darbību',
        techWriting: 'Tehnisko rakstīšanu',
        and: 'un',
        frontendDev: 'Frontend izstrādi',
        lover: 'Aizraujos ar',
        craftBeer: 'Amatniecības alu',
        jrock:'Japānas Roks',
        motorcycle: 'Mototūrēm',
        springCity: 'Pavasara pilsēta',
        kunming: 'Kunminga, Juņnaņa, Ķīna'
      },
      ja: {
        hello: 'こんにちは。',
        im: '私は',
        name: '張新健',
        passionate: '情熱を持っている分野',
        productMgmt: '製品管理',
        productOps: '製品オペレーション',
        techWriting: '技術文書',
        and: 'と',
        frontendDev: 'フロントエンド開発',
        lover: '「趣味」',
        craftBeer: 'クラフトビール',
        jrock:'日本のロック',
        motorcycle: 'ツーリング',
        springCity: '春の都市',
        kunming: '昆明、雲南、中国'
      }
    }
    
    const content = reactive({...translations.zh})
    
    const setLanguage = (lang) => {
      currentLang.value = lang
      Object.assign(content, translations[lang])
      
      gsap.to('.language-selector button', {
        rotation: 360,
        backgroundColor: '#af3ec4',
        color: '#fff',
        boxShadow: '0 0 10px #ff6ec4',
        transformOrigin: 'center',
        transform: 'scale(1.2)',
        stagger: 0.1,
        duration: 1,
        ease: 'power2.out',
        yoyo: true,
        repeat: 1
      })
    }
    
    return {
      currentLang,
      languages,
      content,
      setLanguage
    }
  },
  mounted() {
    gsap.from('.language-selector button', {
      scale: 1.2,
      duration: 0.5,
      ease: 'power3.out',
      delay: 0.3
    })
  
    gsap.utils.toArray('.flex-wrap a').forEach(button => {
      button.addEventListener('mouseenter', () => {
        gsap.to(button, {
          backgroundColor: '#ag3ef4',
          color: '#fff',
          boxShadow: '0 0 10px #ff6ec4',
          transformOrigin: 'center',
          scale: 1.1,
          duration: 0.3,
          ease: 'power2.out',
        
        })
      })
  
      button.addEventListener('mouseleave', () => {
        gsap.to(button, {
          backgroundColor: 'transparent',
          scale: 1,
          duration: 0.3,
          ease: 'power2.out',
        })
      })
    })
  }
}
</script>