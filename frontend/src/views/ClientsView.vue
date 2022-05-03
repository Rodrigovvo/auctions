<script setup lang="ts">
import Clients from '@/components/Clients.vue'
</script>

<template>
  <main>
    <Clients />
  </main>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
