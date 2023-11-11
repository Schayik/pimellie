<template>
  <header>
    <h1>All magical moments of our wedding</h1>
  </header>

  <main>
    <section>
      <h2>Days</h2>

      <nav>
        <RouterLink to="#welcome">Welcome<br />Thursday, July 11</RouterLink>
        <RouterLink to="#wedding">Wedding<br />Friday, July 12</RouterLink>
        <RouterLink to="#day-two">Day two<br />Saturday, July 13</RouterLink>
      </nav>
    </section>

    <img alt="Durrus and Bantry" class="durrus-bantry" src="@/assets/durrus-bantry.png" />

    <section id="welcome">
      <h2>Welcome</h2>

      <p>
        Thursday, July 11<br />
        Location name<br />
        Location address<br />
      </p>

      <p>Low key meetup</p>

      <ul>
        <li>?PM - Wij zijn er</li>
        <li>?PM - Wij gaan</li>
      </ul>
    </section>

    <img alt="Durrus and Bantry" class="durrus-bantry" src="@/assets/durrus-bantry.png" />

    <section id="wedding">
      <h2>Wedding</h2>

      <p>
        Friday, July 12<br />
        Blairscove House<br />
        Durrus, Cork, P75 FE44<br />
      </p>

      <ul>
        <li>1.30PM - Bus pickup in Bantry town centre</li>
        <li>2PM - Arrive at Blairscove</li>
        <li>2.30PM - Ceremony</li>
        <li>3.30PM - Drinks reception and speeches</li>
        <li>5PM - Dinner bell</li>
        <li>8PM - After dinner speeches</li>
        <li>8.30PM - Party with band</li>
        <li>11PM - Party with DJ</li>
        <li>2PM - Bus return to bantry - Other busses are available throughout the night</li>
        <li>2.30PM - Bus arrival in Bantry - The bus will bring you home</li>
      </ul>
    </section>

    <img alt="Durrus and Bantry" class="durrus-bantry" src="@/assets/durrus-bantry.png" />

    <section id="day-two">
      <h2>Day Two</h2>

      <p>
        Saturday, July 13<br />
        Ma Murphy's Bar<br />
        7 New Street, Bantry, Cork<br />
      </p>

      <ul>
        <li>5PM - Drinks</li>
        <li>7PM - Bites served</li>
        <li>12PM - Bar closes</li>
      </ul>
    </section>
  </main>
</template>

<style scoped lang="scss">
header {
  padding: 1rem;
}

nav {
  > a {
    margin-top: 1rem;
    display: block;

    border: 1px solid black;
    border-radius: 1rem;

    padding: 1rem;

    display: flex;
  }
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

    background-image: url('@/assets/roys-peak.jpeg');
    background-size: cover;
  }
}

.durrus-bantry {
  width: 100vw;
}
</style>
