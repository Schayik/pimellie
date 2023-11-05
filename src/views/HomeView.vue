<template>
  <header>
    <h1>Ellie & Pim</h1>
    <h2>12 - 7 - 24</h2>
  </header>

  <main>
    <section>
      <h2>Nijmegen, Nederland, 2017</h2>
      <p>
        An Irish and a Dutchie<br>
        Working as a chemist<br>
        They study, the measure, they graph<br>
        They like, they love, they laugh<br>
        Exactly what they've missed<br>
        A perfect chemistry<br>
      </p>
    </section>

    <section class="roys-peak">
      <h2>Roys Peak, New Zealand, 2023</h2>
      <h3>Engaged!</h3>
      <p>Sometimes it's worth waking up early</p>
    </section>

    <section>
      <h2>West Cork, Ireland, 2024</h2>
      <h3>Our wedding</h3>
      <p>Time to celebrate with our family and dearest friend</p>
    </section>

    <nav>
      <RouterLink to="/wedding">All magical moments of our wedding</RouterLink>
      <RouterLink to="/info">Everything you need and want to know abut our wedding</RouterLink>
    </nav>
  </main>
</template>

<style scoped lang="scss">
header {
  min-height: 100vh;
  padding: 20vh 10vh;

  background-image: url("@/assets/roys-peak.jpeg");
  background-size: cover;

  display: flex;
  flex-direction: column;

  > h1 {
    color: black;
    text-align: center;
  }
  > h2 {
    color: black;
    text-align: center;
  }
}

section {
  padding: 10vh;

  > h2 {
    color: black;
    text-align: center;
  }
  > h3 {
    color: black;
    text-align: center;
  }
  > p {
    color: black;
    text-align: center;
  }

  &.roys-peak {
    min-height: 80vh;

    background-image: url("@/assets/roys-peak.jpeg");
    background-size: cover; 
  }
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}


nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>

