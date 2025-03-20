// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  // Mode statique
  ssr: true,

  nitro: {
    prerender: {
      crawlLinks: true,
      routes: ['/']
    },
    server: {
      port: process.env.PORT
    }
  },

  // Modules utiles
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
  ],

  // Configuration des répertoires publics
  dir: {
    public: 'public'
  },

  // Configuration de Leaflet
  plugins: [
    '~/plugins/leaflet.client.ts'
  ],

  build: {
    transpile: ['@vue-leaflet/vue-leaflet']
  },

  compatibilityDate: '2025-03-20',

  app: {
    head: {
      link: [
        { 
          rel: 'icon', 
          type: 'image/png', 
          href: '/favicon-16x16.png',
          sizes: '16x16'
        },
        { 
          rel: 'icon', 
          type: 'image/png', 
          href: '/favicon-32x32.png',
          sizes: '32x32'
        },
        // Pour les appareils Apple
        { 
          rel: 'apple-touch-icon', 
          href: '/apple-touch-icon.png',
          sizes: '180x180'
        }
      ]
    }
  }
})