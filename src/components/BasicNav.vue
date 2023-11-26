<template>
  <nav class="basic-nav">
    <slot></slot>
  </nav>
</template>

<style lang="scss">
nav.basic-nav {
  padding: 1rem;

  display: flex;
  flex-direction: column;
  align-items: stretch;

  > a {
    margin-top: 1rem;
    height: 94px;

    display: flex;
    align-items: center;
    padding: 1rem 0.5rem;

    border: 1px solid black;
    border-radius: 1rem;

    line-height: 25px;
    color: black;
    text-decoration: none;

    > .icon-relative {
      position: relative;
      align-self: stretch;

      flex: 0 0 108px;

      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;

      > .icon-absolute {
        position: absolute;
        top: -4px;

        width: 108px;
        &.flowers {
          height: 87px;
        }
        &.waving {
          height: 90px;
        }
        &.location {
          height: 87px;
        }
      }

      > p {
        color: white;
        font-size: 18px;
        line-height: 17px;
        z-index: 1;

        &.date-weekday,
        &.date-daynumber {
          font-family: 'bevietnammedium';
        }
        &.date-month {
          font-family: 'bevietnamthin';
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
