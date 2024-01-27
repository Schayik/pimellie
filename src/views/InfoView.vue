<script setup>
import BasicNav from '@/components/BasicNav.vue'
import Chemie from '@/components/icons/IconChemie.vue'
import Home from '@/components/icons/IconHome.vue'
import Travel from '@/components/icons/TravelIcon.vue'

import { onMounted } from 'vue'
onMounted(() => {
  window.scrollTo(0, 0)
})
</script>

<template>
  <div class="mh-100">
    <header id="top">
      <h1>The Details</h1>
    </header>

    <BasicNav>
      <RouterLink to="#wedding">
        <div class="icon-relative">
          <Chemie class="icon-absolute" />
        </div>
        <p>The Day of</p>
      </RouterLink>
      <RouterLink to="#places-to-stay">
        <div class="icon-relative">
          <Home class="icon-absolute" />
        </div>
        <p>Places to stay</p>
      </RouterLink>
      <RouterLink to="#travel">
        <div class="icon-relative">
          <Travel class="icon-absolute" />
        </div>
        <p>Travel</p>
      </RouterLink>
    </BasicNav>

    <img src="@/assets/brewdog-563x422.png" class="landscape-image" />
  </div>

  <main>
    <section id="wedding">
      <div class="section-title">
        <div class="icon-relative">
          <Chemie class="icon-absolute" />
        </div>
        <h3>The Day of</h3>
      </div>

      <h4>Dress Code</h4>

      <p>
        We want our guests to be comfortable and relaxed on the day; but we would love to see
        everyone look their best! Cocktail attire is encouraged.
      </p>

      <h4>Transport on the day</h4>

      <p>
        Blairscove is approximately 10 minutes outside Bantry town. We will be collecting you on the
        party bus and returning you safely to Bantry afterwards. Buses will be running throughout
        the evening, taxis are few and far between in Bantry so please do not rely on them.
        Blairscove is not walkable as the roads are dark and unsafe with no footpaths, please don't
        walk home!
      </p>

      <h4>Parking</h4>

      <p>
        There is limited parking available at Blairscove, please let us know if you're planning to
        drive and we can ensure there is a spot for your car.
      </p>

      <h4>Weather</h4>

      <p>
        Even though you would expect a beautiful sunny day in mid July; please note that the weather
        in Ireland doesn't always play ball... We are hoping to have an outdoor ceremony and
        reception; alternative arrangements will be made if the sun doesn't shine!
      </p>

      <h4>Talen</h4>

      <p>
        Gelukkig begrijpt en spreekt de meerderheid van onze familie en vrienden Engels, maar we
        zullen de hele dag beide talen gebruiken om al onze gewaardeerde gasten erbij te betrekken!
      </p>

      <h4>Gifts</h4>

      <p>
        Your presence is the best present to us (really!); however if you would like to still give
        us a small gift, a donation to our honeymoon would be extremely appreciated!
      </p>
    </section>

    <section id="places-to-stay">
      <div class="section-title">
        <div class="icon-relative">
          <Home class="icon-absolute" />
        </div>
        <h3>Places to stay</h3>
      </div>

      <h4>Our Recommendations</h4>

      <ul class="location-favourites">
        <li>
          <span>•</span>
          <p><a href="https://www.themaritime.ie/">The Maritime Hotel</a> <b>$$</b></p>
        </li>

        <li>
          <span>•</span>
          <p><a href="https://www.westlodgehotel.ie/">The Westlodge Hotel</a> <b>$$</b></p>
        </li>

        <li>
          <span>•</span>
          <p>
            Guest houses and holiday homes available through
            <a href="https://www.airbnb.ie/">AirBnB</a> or
            <a href="https://www.booking.com/">Booking.com</a>
            <b> $</b>
          </p>
        </li>
      </ul>
    </section>

    <section id="travel">
      <div class="section-title">
        <div class="icon-relative">
          <Travel class="icon-absolute" />
        </div>
        <h3>Getting to West Cork</h3>
      </div>

      <p>
        Part of the charm of West Cork lies in the fact that it is quite isolated. We would
        recommend car hire for your trip, but public transport is available; albeit limited!
      </p>
      <h4>Airports</h4>

      <ul class="getting-there-airports">
        <li><b>Cork</b></li>
        <li>
          <span>•</span>1h 15min by car (<a
            href="https://www.corkairport.com/to-from-the-airport/by-rental-car"
          >
            Car Hire </a
          >)
        </li>
        <li>
          <span>•</span>2h by bus from Cork City centre (<a
            href="https://www.buseireann.ie/inner.php?id=406&form-view-timetables-from=&form-view-timetables-to=&form-view-timetables-route=236&form-view-timetables-submit=1"
            >Bus Eireann</a
          >)
        </li>
        <li><b>Shannon</b></li>
        <li>
          <span>•</span>3h by car (<a
            href="https://www.shannonairport.ie/passengers/explore-ireland/car-hire/"
            >Car Hire</a
          >)
        </li>

        <li><b>Dublin</b></li>

        <li>
          <span>•</span>4h 15min by car (<a
            href="https://www.dublinairport.com/to-from-the-airport/car-rental"
            >Car Hire</a
          >)
        </li>
        <li>
          <span>•</span>7h by bus (<a
            href="https://www.aircoach.ie/plan-journey/fares/route-704-cork-dublin-city-centre-and-dublin-airport"
            >Air Coach</a
          >
          &
          <a
            href="https://www.buseireann.ie/inner.php?id=406&form-view-timetables-from=&form-view-timetables-to=&form-view-timetables-route=236&form-view-timetables-submit=1"
            >Bus Eireann</a
          >)
        </li>
      </ul>

      <h4>Ferries</h4>
      <p>
        Roscoff, France to Cork
        <a
          href="https://www.brittany-ferries.ie/ferry-routes/ireland-france-ferries/cork-roscoff/about"
          >Brittany Ferries</a
        >
      </p>
    </section>

    <div class="h-10"></div>
  </main>
</template>

<style scoped lang="scss">
header {
  padding: 1rem;

  > h1 {
    font-family: 'aliceregular';
    font-size: 40px;
    text-align: center;
  }
}

section {
  padding: 1rem;

  h4 {
    margin-top: 2rem;
    font-size: 21px;
  }
}

img.landscape-image {
  margin-top: 1rem;
  width: 100%;
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

ul.getting-there-airports {
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
