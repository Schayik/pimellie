<script setup>
import BasicNav from '@/components/BasicNav.vue'
import LocationIcon from '@/components/icons/LocationIcon.vue'
import MapStandard from '@/components/icons/MapStandard.vue'

import { onMounted } from 'vue'
onMounted(() => {
  window.scrollTo(0, 0)
})
</script>

<template>
  <div class="mh-100">
    <header>
      <h1>The Schedule</h1>
    </header>

    <BasicNav>
      <RouterLink to="#welcome">
        <div class="icon-relative">
          <LocationIcon class="icon-absolute location" />
          <p class="date-weekday">THU</p>
          <p class="date-month">JULY</p>
          <p class="date-daynumber">11</p>
        </div>
        <p>Welcome drinks</p>
      </RouterLink>
      <RouterLink to="#wedding">
        <div class="icon-relative">
          <LocationIcon class="icon-absolute location" />
          <p class="date-weekday">FRI</p>
          <p class="date-month">JULY</p>
          <p class="date-daynumber">12</p>
        </div>
        <p>The Main Event</p>
      </RouterLink>
      <RouterLink to="#day-two">
        <div class="icon-relative">
          <LocationIcon class="icon-absolute location" />
          <p class="date-weekday">SAT</p>
          <p class="date-month">JULY</p>
          <p class="date-daynumber">13</p>
        </div>
        <p>Day Two</p>
      </RouterLink>
    </BasicNav>
  </div>
  <main>
    <MapStandard id="welcome" class="location-map" markerLocation="town" />

    <section>
      <h3>Welcome Drinks</h3>
      <h4><i>For those already in West Cork!</i></h4>
      <p>
        Thursday, July 11<br />
        Bantry town centre
      </p>

      <p>Low key meetup</p>
    </section>

    <MapStandard id="wedding" class="location-map" markerLocation="blairscove" />

    <section>
      <h3>The Main Event</h3>
      <p>Friday, July 12<br />Blairscove House<br />Durrus, Cork, P75 FE44</p>

      <table>
        <tbody>
          <tr>
            <td>1.30PM</td>
            <td class="timetable-line first"></td>
            <td>Bus collection in Bantry (Town Centre)</td>
          </tr>

          <tr>
            <td>1:45PM</td>
            <td class="timetable-line"></td>
            <td>Hug your friends and take your seats</td>
          </tr>

          <tr>
            <td>2.00PM</td>
            <td class="timetable-line"></td>
            <td>Ceremony</td>
          </tr>

          <tr>
            <td>2:45PM</td>
            <td class="timetable-line"></td>
            <td>Drinks reception and speeches</td>
          </tr>

          <tr>
            <td>5PM</td>
            <td class="timetable-line"></td>
            <td>Dinner bell</td>
          </tr>

          <tr>
            <td>8.30PM</td>
            <td class="timetable-line"></td>
            <td>Party!</td>
          </tr>

          <tr>
            <td>2AM</td>
            <td class="timetable-line last"></td>
            <td>
              Bus return to Bantry
              <span class="subtext"> Buses are available throughout the night</span>
            </td>
          </tr>
        </tbody>
      </table>
    </section>

    <MapStandard id="day-two" class="location-map" markerLocation="ma-murphy" />

    <section>
      <h3>Day Two</h3>
      <h4><i>For those still standing...</i></h4>
      <p>Saturday, July 13<br />Ma Murphy's Bar<br />7 New Street, Bantry, Cork</p>

      <table>
        <tbody>
          <tr>
            <td>5PM</td>
            <td class="timetable-line first"></td>
            <td>Recovery creamy Beamish</td>
          </tr>

          <tr>
            <td></td>
            <td class="timetable-line"></td>
            <td>More drinks, pizza and trad music</td>
          </tr>

          <tr>
            <td>12AM</td>
            <td class="timetable-line last"></td>
            <td>Close the night</td>
          </tr>
        </tbody>
      </table>
    </section>
  </main>

  <div class="h-10"></div>
</template>

<style scoped lang="scss">
header {
  padding: 1rem;

  > h1 {
    font-family: 'bevietnammedium';
    font-size: 33px;
  }
}

.location-map {
  margin-top: 4rem;
  width: 100%;
  height: auto;
}

section {
  padding: 1rem;
}

table {
  border-collapse: collapse;

  margin-top: 0.5rem;
  > tbody > tr {
    vertical-align: top;

    > td:first-child {
      text-align: right;
    }
    > td.timetable-line {
      position: relative;
      padding-left: 1rem;
      padding-right: 1rem;

      &:before {
        content: ' ';
        position: absolute;
        top: 15px;
        left: calc(1rem - 3px);

        height: 5px;
        width: 5px;
        background-color: black;
        border-radius: 50%;
        display: inline-block;
      }

      &:after {
        content: ' ';
        position: absolute;
        top: 0;
        bottom: 0;
        left: calc(1rem - 1px);
        border-left: 1px solid #111;
      }

      &.first:after {
        top: 15px;
      }

      &.last:after {
        bottom: calc(100% - 15px);
      }
    }

    > td:last-child {
      > span.subtext {
        display: block;
        font-size: 14px;
      }
    }
  }
}
</style>
