<script setup>
import BasicNav from '@/components/BasicNav.vue'
import Cheers from '@/components/icons/IconCheers.vue'
import Chemie from '@/components/icons/IconChemie.vue'

import { onMounted } from 'vue'
onMounted(() => {
  window.scrollTo(0, 0)
})
</script>

<template>
  <header>
    <h1>Ellie & Pim</h1>
    <h3>12 • 07 • 2024</h3>
  </header>

  <main>
    <BasicNav class="mt-2">
      <a href="https://docs.google.com/forms/d/e/1FAIpQLScnZSZgcjCkUiuSRODqgPzdYmSIAT_TipBUB21cM2daAwcTrg/viewform?usp=sf_link">
        <div class="icon-relative">
          <Chemie class="icon-absolute flowers" />
        </div>
        <p>RSVP</p>
      </a>
    </BasicNav>

    <section class="nijmegen">
      <h2 >We met ...</h2>
      <h3>Nijmegen, Nederland, 2017</h3>
      <img class="mt-1" src="@/assets/nijmegen.png" alt="Nijmegen, Nederland, 2017" />
    </section>

    <section class="roys-peak-close">
      <h2>Engaged!</h2>
      <p class="mx-4">
        Sometimes it's worth<br />
        waking up early
      </p>
      <h3 class="mt-2">Roys Peak, New Zealand, 2023</h3>
    </section>

    <section>
      <h2>Our wedding</h2>
      <p>
        Time to celebrate<br />
        with our family and dearest friends
      </p>
      <h3 class="mt-2">West Cork, Ireland, 2024</h3>
    </section>

    <BasicNav>
      <RouterLink to="/timeline">
        <div class="icon-relative">
          <Chemie class="icon-absolute flowers" />
        </div>
        <p>The Schedule</p>
      </RouterLink>
      <RouterLink to="/info">
        <div class="icon-relative">
          <Cheers class="icon-absolute waving" />
        </div>
        <p>The Details</p>
      </RouterLink>
    </BasicNav>
  </main>

  <div class="h-10"></div>
</template>

<style scoped lang="scss">
header {
  min-height: 100vh;
  min-height: 100svh;
  padding: 8rem 1rem;

  background-image: url('/roys-peak-far-563x900.png');
  background-size: cover;
  background-position: center;

  display: flex;
  flex-direction: column;

  > h1 {
    font-size: 50px;
    text-align: center;
    color: black;
  }
  > h3 {
    font-size: 19px;
    text-align: center;
    color: black;
  }
}

section {
  padding: 4rem 1rem;

  display: flex;
  flex-direction: column;
  align-items: center;

  > h2 {
    font-size: 30px;
    text-align: center;
  }
  > h3 {
    font-size: 19px;
    color: black;
    text-align: center;
  }
  > p {
    font-size: 19px;
    line-height: auto;
    color: black;
    text-align: center;
  }

  &.nijmegen {
    img {
      width: 100%;
    }
  }

  &.roys-peak-close {
    min-height: 100vh;

    background-image: url('@/assets/roys-peak-close-563x690.png');
    background-size: cover;
  }

  > .chemy-icon {
    height: 90px;
    width: 90px;
  }
}
</style>
