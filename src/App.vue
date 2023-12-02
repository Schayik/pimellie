<script setup>
import { RouterView } from 'vue-router'

import IconCheers from '@/components/icons/IconCheers.vue'
import IconChemie from '@/components/icons/IconChemie.vue'
import IconHome from '@/components/icons/IconHome.vue'
</script>

<template>
  <RouterView />

  <nav>
    <div class="nav-wrapper">
      <div class="background"></div>

      <RouterLink to="/timeline">
        <IconChemie class="icon" />
        <p>WEDDING</p>
      </RouterLink>
      <RouterLink to="/">
        <IconHome class="icon" />
        <p>HOME</p>
      </RouterLink>
      <RouterLink to="/info">
        <IconCheers class="icon" />
        <p>INFO</p>
      </RouterLink>
    </div>
  </nav>
</template>

<style scoped lang="scss">
nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;

  z-index: 5;

  > .nav-wrapper {
    margin-left: auto;
    margin-right: auto;
    max-width: 36rem;

    background: linear-gradient(180deg, rgba(255, 255, 255, 0.00) 0%, #FFF 100%);

    display: flex;
    justify-content: space-around;

    > .background {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;

      border-top: 1px solid black;

      background-color: white;
      height: 30px;

      z-index: -1;
    }
    > a {
      display: flex;
      flex-direction: column;
      align-items: center;

      text-decoration: none;
      color: black;

      > .icon {
        width: 108px;
        height: 90px;
      }

      > p {
        font-family: 'bevietnamthin';
        font-size: 15px;
      }
      &.router-link-active > p {
        font-family: 'bevietnammedium';
      }
    }
  }
}
</style>
