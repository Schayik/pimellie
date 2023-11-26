<script setup>
import BasicNav from '@/components/BasicNav.vue'
import LocationIcon from '@/components/icons/LocationIcon.vue'
import MapStandard from '@/components/icons/MapStandard.vue'
</script>

<template>
  <header>
    <h1>All magical moments of our wedding</h1>
  </header>

  <BasicNav>
    <h3>Days</h3>
    <RouterLink to="#welcome">
      <div class="icon-relative">
        <LocationIcon class="icon-absolute location" />
        <p class="date-weekday">THU</p>
        <p class="date-month">JULY</p>
        <p class="date-daynumber">11</p>
      </div>
      <p>Welcome</p>
    </RouterLink>
    <RouterLink to="#wedding">
      <div class="icon-relative">
        <LocationIcon class="icon-absolute location" />
        <p class="date-weekday">FRI</p>
        <p class="date-month">JULY</p>
        <p class="date-daynumber">12</p>
      </div>
      <p>Wedding</p>
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

  <main>
    <MapStandard class="map" />

    <section>
      <h3>Welcome</h3>
      <p>
        Thursday, July 11<br />
        Bantry town centre
      </p>

      <p>Low key meetup</p>
    </section>

    <MapStandard class="map" />

    <section>
      <h3>Wedding</h3>
      <p>Friday, July 12<br />Blairscove House<br />Durrus, Cork, P75 FE44</p>

      <table>
        <tbody>
          <tr>
            <td>1.30PM</td>
            <td class="timetable-line first"></td>
            <td>Bus pickup in Bantry town centre</td>
          </tr>

          <tr>
            <td>2PM</td>
            <td class="timetable-line"></td>
            <td>Arrive at Blairscove</td>
          </tr>

          <tr>
            <td>2.30PM</td>
            <td class="timetable-line"></td>
            <td>Ceremony</td>
          </tr>

          <tr>
            <td>3.30PM</td>
            <td class="timetable-line"></td>
            <td>Drinks reception and speeches</td>
          </tr>

          <tr>
            <td>5PM</td>
            <td class="timetable-line"></td>
            <td>Dinner bell</td>
          </tr>

          <tr>
            <td>8PM</td>
            <td class="timetable-line"></td>
            <td>After dinner speeches</td>
          </tr>

          <tr>
            <td>8.30PM</td>
            <td class="timetable-line"></td>
            <td>Party with band</td>
          </tr>

          <tr>
            <td>11PM</td>
            <td class="timetable-line"></td>
            <td>Party with DJ</td>
          </tr>

          <tr>
            <td>2AM</td>
            <td class="timetable-line"></td>
            <td>
              Bus return to bantry
              <span class="subtext">Other busses are available throughout the night</span>
            </td>
          </tr>

          <tr>
            <td>2.30AM</td>
            <td class="timetable-line last"></td>
            <td>
              Bus arrival in Bantry
              <span class="subtext">The bus will bring you home</span>
            </td>
          </tr>
        </tbody>
      </table>
    </section>

    <MapStandard class="map" />

    <section>
      <h3>Day Two</h3>
      <p>Saturday, July 13<br />Ma Murphy's Bar<br />7 New Street, Bantry, Cork</p>

      <table>
        <tbody>
          <tr>
            <td>5PM</td>
            <td class="timetable-line first"></td>
            <td>Drinks</td>
          </tr>

          <tr>
            <td>7PM</td>
            <td class="timetable-line"></td>
            <td>Bites served</td>
          </tr>

          <tr>
            <td>12PM</td>
            <td class="timetable-line last"></td>
            <td>Bar closes</td>
          </tr>
        </tbody>
      </table>
    </section>
  </main>

  <div class="h-16"></div>
</template>

<style scoped lang="scss">
header {
  padding: 1rem;

  > h1 {
    font-family: 'bevietnammedium';
    font-size: 33px;
  }
}

.map {
  margin-top: 4rem;
  width: 100%;
  height: auto;
}

section {
  padding: 1rem;

  > h2 {
    color: black;
  }
  > h3 {
    color: black;
  }
  > p {
    color: black;
  }

  &.roys-peak {
    min-height: 80vh;

    background-image: url('@/assets/roys-peak.png');
    background-size: cover;
  }
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

.durrus-bantry {
  width: 100vw;
}
</style>
