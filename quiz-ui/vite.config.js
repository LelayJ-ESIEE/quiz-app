import { fileURLToPath, URL } from 'url'

import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/

export default ({ mode }) => {
  // eslint-disable-next-line no-undef
  process.env = {...process.env, ...loadEnv(mode, process.cwd())};

  return defineConfig({
    plugins: [vue()],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    },
    // eslint-disable-next-line no-undef
    base: `${process.env.VITE_BASE}`,
    build: {
      emptyOutDir: true
    }
  });
}