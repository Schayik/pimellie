<script setup>
import Cheers from '@/components/icons/IconCheers.vue'
import Chemie from '@/components/icons/IconChemie.vue'
import Flask from '@/components/icons/IconFlask.vue'
</script>

<template>
  <header>
    <h1>Ellie & Pim</h1>
    <h3>12 • 07 • 2024</h3>
  </header>

  <main>
    <section>
      <Flask class="chemy" />
      <p class="mt-2">
        An Irish and a Dutchie<br />
        Working as a chemist<br />
        They study, the measure, they graph<br />
        They like, they love, they laugh<br />
        Exactly what they've missed<br />
        A perfect chemistry<br />
      </p>
      <h3 class="mt-2">Nijmegen, Nederland, 2017</h3>
    </section>

    <section class="roys-peak-engaged">
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
        with our family and dearest friend
      </p>
      <h3 class="mt-2">West Cork, Ireland, 2024</h3>
    </section>

    <nav>
      <RouterLink to="/wedding">
        <div class="icon-relative">
          <Chemie class="icon-absolute flowers" />
        </div>
        <p>All magical moments of our wedding</p>
      </RouterLink>
      <RouterLink to="/info">
        <div class="icon-relative">
          <Cheers class="icon-absolute waving" />
        </div>
        <p>Everything you need and want to know about our wedding</p>
      </RouterLink>
    </nav>
  </main>
</template>

<style scoped lang="scss">
header {
  min-height: 100vh;
  min-height: 100svh;
  padding: 8rem 1rem;

  background-image: url('@/assets/roys-peak.png');
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

  &.roys-peak-engaged {
    min-height: 100vh;

    background-image: url('@/assets/roys-peak-engaged.png');
    background-size: cover;
  }
}

.chemy {
  height: 90px;
  width: 90px;
}

nav {
  padding: 1rem;
  margin-bottom: 10rem;

  display: flex;
  flex-direction: column;
  align-items: center;

  > a {
    margin-bottom: 2rem;
    min-height: 92px;
    max-width: 360px;

    display: flex;
    padding: 1rem 0.5rem;

    border: 1px solid black;
    border-radius: 1rem;

    line-height: 25px;
    color: black;
    text-decoration: none;

    > .icon-relative {
      position: relative;

      width: 108px;
      flex-shrink: 0;

      > .icon-absolute {
        position: absolute;
        width: 108px;
        &.flowers {
          height: 81px;
        }
        &.waving {
          height: 106px;
        }
      }
    }

    > p {
      font-family: 'bevietnammedium';
      margin-left: 1rem;
    }
  }
}
</style>
