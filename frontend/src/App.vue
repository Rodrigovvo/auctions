<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Footer from './components/Footer.vue'

</script>

<template>
  <html>
    <header>
        <!-- Navbar -->
          <nav class="navbar navbar-expand-lg justify-content-end">
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/offers">Ofertas</RouterLink>
            <RouterLink to="/clients">Clientes</RouterLink>
            <RouterLink to="/enterprises">Empresas</RouterLink>
          </nav>
          <hr>
        <!-- End Navbar -->
    </header>

    <RouterView />
    <Footer />

  </html>
</template>

<style>
@import '@/assets/base.css';

#app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;

  font-weight: normal;
}

header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

a {
  text-decoration: none;
  color: rgb(0, 3, 189);
  transition: 0.4s;
}

@media (hover: hover) {
  a:hover {
    background-color: hsla(240, 20%, 80%, 0.350);
  }
}

nav {
  width: 100%;
  font-size: 14px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}


</style>
