<template>
  <header>
    <h1>Everything you need and want to know about our wedding</h1>
  </header>

  <main>
    <section id="topics">
      <h2>Topics</h2>

      <nav>
        <RouterLink to="#wedding">Wedding</RouterLink>
        <RouterLink to="#places-to-stay">Places to stay</RouterLink>
        <RouterLink to="#travel">Travel</RouterLink>
      </nav>
    </section>

    <section id="wedding">
      <h2>Wedding</h2>

      <h2>Locations</h2>

      <ul>
        <li>
          Welcome<br>
          Thursday, July 11<br>
          Location name<br>
          Location address<br>
        </li>

        <li>
          Wedding<br>
          Friday, July 12<br>
          Blairscove House<br>
          Durrus, Cork, P75 FE44<br>
        </li>

        <li>
          Day Two<br>
          Saturday, July 13<br>
          Ma Murphy's Bar<br>
          7 New Street, Bantry, Cork<br>
        </li>
      </ul>

      <p>
        De tijden vind je op de <RouterLink to="/wedding">wedding-page</RouterLink>
      </p>

      <h2>Clothes</h2>

      <p>
        Vergeet je feestneus niet. ...
      </p>

      <h2>Registry</h2>

      <p>
        Bla bla bla. ..
      </p>

      <RouterLink to="#topics">Back to topic overview ^</RouterLink>

    </section>

    <section id="places-to-stay">
      <h2>Places to stay</h2>

      <h2>Location</h2>

      <p>
        Ergens in Bantry, vlakbij Ma Murphy's bar.
      </p>

      <h2>Our favourites</h2>

      <ul>
        <li>The Maritime</li>
        <li>West Lodge</li>
        <li>There's a lot of smaller guest houses around that can be booked through Airbnb or Bookng.com</li>
      </ul>

      <RouterLink to="#topics">Back to topic overview ^</RouterLink>
    </section>

    <section id="travel">
      <h2>Travel</h2>

      <h2>Parking</h2>

      <p>
        Ergens in Bantry, vlakbij Ma Murphy's bar.
      </p>

      <h2>Airport</h2>

      <p>
        Ergens in Bantry, vlakbij Ma Murphy's bar.
      </p>

      <RouterLink to="#topics">Back to topic overview ^</RouterLink>
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

    background-image: url("@/assets/roys-peak.jpeg");
    background-size: cover; 
  }
}

.durrus-bantry {
    width: 100vw;
  }

</style>
