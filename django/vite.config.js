import { defineConfig } from 'vite'
import { resolve } from 'path'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
    base: '/static/',
    plugins: [
        tailwindcss(),
    ],
    build: {
        manifest: 'manifest.json',
        outDir: resolve('./assets'),
        rollupOptions: {
            input: {
                main: resolve('./static/js/main.js'),
            }
        }
    }
})