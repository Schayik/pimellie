<script setup>
import BasicNav from '@/components/BasicNav.vue'
import Chemie from '@/components/icons/IconChemie.vue'
import Home from '@/components/icons/IconHome.vue'
import Travel from '@/components/icons/TravelIcon.vue'
import VectorUp from '@/components/icons/VectorUp.vue'

import { onMounted } from 'vue'
onMounted(() => {
  window.scrollTo(0, 0)
})
</script>

<template>
  <header id="top">
    <h1>Everything you need and want to know about our wedding</h1>
  </header>

  <BasicNav>
    <h3>Topics</h3>
    <RouterLink to="#wedding">
      <div class="icon-relative">
        <Chemie class="icon-absolute location" />
      </div>
      <p>Wedding</p>
    </RouterLink>
    <RouterLink to="#places-to-stay">
      <div class="icon-relative">
        <Home class="icon-absolute location" />
      </div>
      <p>Places to stay</p>
    </RouterLink>
    <RouterLink to="#travel">
      <div class="icon-relative">
        <Travel class="icon-absolute location" />
      </div>
      <p>Travel</p>
    </RouterLink>
  </BasicNav>

  <main>
    <section id="wedding">
      <div class="section-title">
        <div class="icon-relative">
          <Chemie class="icon-absolute" />
        </div>
        <h3>Wedding</h3>
      </div>

      <h4>Our favourites</h4>

      <ul class="wedding-dates">
        <li>
          <span>•</span>
          Welcome drinks<br />
          Thursday, July 11<br />
          Location name<br />
          Location address<br />
        </li>

        <li>
          <span>•</span>
          Wedding<br />
          Friday, July 12<br />
          Blairscove House<br />
          Durrus, Cork, P75 FE44<br />
        </li>

        <li>
          <span>•</span>
          Day Two<br />
          Saturday, July 13<br />
          Ma Murphy's Bar<br />
          7 New Street, Bantry, Cork<br />
        </li>
      </ul>

      <p>De tijden vind je op de <RouterLink to="/timeline">wedding-page</RouterLink></p>

      <h4>Clothes</h4>

      <p>
        Vergeet je feestneus niet. Is het binnen of buiten? Cat ipsum dolor sit amet, crusty
        butthole or throw down all the stuff in the kitchen yet who's the baby. Steal raw zucchini
        off kitchen counter i am the best.
      </p>

      <h4>Registry</h4>

      <p>
        Cat ipsum dolor sit amet, crusty butthole or throw down all the stuff in the kitchen yet
        who's the baby. Steal raw zucchini off kitchen counter i am the best.
      </p>

      <RouterLink class="back-to-top" to="#top">
        Back to topic overview<VectorUp class="ml-2" />
      </RouterLink>
    </section>

    <section id="places-to-stay">
      <div class="section-title">
        <div class="icon-relative">
          <Home class="icon-absolute" />
        </div>
        <h3>Places to stay</h3>
      </div>

      <h4>Location</h4>

      <p>Ergens in Bantry, vlakbij Ma Murphy's bar.</p>

      <h4>Our favourites</h4>

      <ul class="location-favourites">
        <li>
          <span>•</span>
          <p><a href="https://www.themaritime.ie/">The Maritime Hotel</a></p>
        </li>

        <li>
          <span>•</span>
          <p><a href="https://www.westlodgehotel.ie/">Westlodge Hotel</a></p>
        </li>

        <li>
          <span>•</span>
          <p>
            There's a lot of smaller guest houses around that can be booked through
            <a href="https://www.airbnb.ie/">AirBnB</a> or
            <a href="https://www.booking.com/">Booking.com</a>
          </p>
        </li>
      </ul>

      <RouterLink class="back-to-top" to="#top">
        Back to topic overview<VectorUp class="ml-2" />
      </RouterLink>
    </section>

    <section id="travel">
      <div class="section-title">
        <div class="icon-relative">
          <Travel class="icon-absolute" />
        </div>
        <h3>Travel</h3>
      </div>

      <h4>Parking</h4>

      <p>
        Cat ipsum dolor sit amet, crusty butthole or throw down all the stuff in the kitchen yet
        who's the baby. Steal raw zucchini off kitchen counter i am the best.
      </p>

      <h4>Airport</h4>

      <p>
        Cat ipsum dolor sit amet, crusty butthole or throw down all the stuff in the kitchen yet
        who's the baby. Steal raw zucchini off kitchen counter i am the best.
      </p>

      <RouterLink class="back-to-top" to="#top">
        Back to topic overview<VectorUp class="ml-2" />
      </RouterLink>
    </section>

    <div class="h-10"></div>
  </main>
</template>

<style scoped lang="scss">
header {
  padding: 1rem;

  > h1 {
    font-family: 'bevietnammedium';
    font-size: 33px;
  }
}

section {
  padding: 1rem;

  h4 {
    margin-top: 1rem;
    font-size: 21px;
  }
}

.section-title {
  margin-top: 4rem;

  display: flex;
  align-items: end;
  border-bottom: 1px solid black;

  > .icon-relative {
    position: relative;
    flex: 0 0 108px;

    margin-left: 1rem;
    margin-right: 1rem;

    > .icon-absolute {
      position: absolute;
      width: 108px;
      height: 90px;

      left: 0;
      right: 0;
      bottom: -7px;
    }
  }

  > h3 {
    font-size: 19px;
    line-height: 32px;
  }
}

ul.wedding-dates {
  padding-left: 0;
  list-style: none;

  > li {
    margin-top: 8px;
    display: flex;
    > span {
      margin-right: 8px;
    }
  }
}

ul.location-favourites {
  padding-left: 0;
  list-style: none;
  margin-top: 8px;

  > li {
    display: flex;
    > span {
      margin-right: 8px;
    }
    > p {
      margin-top: 0;
    }
    > a {
      color: black;
    }
  }
}

p {
  margin-top: 8px;

  > a {
    color: black;
  }
}

a.back-to-top {
  display: block;
  margin-top: 8px;
  font-family: 'bevietnamthin';
  text-decoration: none;
  color: #7f7f7f;
}
</style>
