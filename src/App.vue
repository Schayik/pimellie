<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="phone-only">
    <RouterView />
  </div>
</template>

<style>
#app {
  padding: 0;
}

.phone-only {
  max-width: 36rem;
  margin-left: auto;
  margin-right: auto;
}
</style>
