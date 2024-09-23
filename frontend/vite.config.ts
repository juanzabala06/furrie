import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: '../static', // Output directly to the static directory of FastAPI
    emptyOutDir: true,    // Optional: Clears the static directory before each build
  },
  base: '/static/',  // Ensure assets are served from the /static/ path
});