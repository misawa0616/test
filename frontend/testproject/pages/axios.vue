<template>
  <div class="container">
    <js-accordion addClass="1" @click-event="scrollClass($event)">
      <div slot="title">アコーディオン1</div>
      <div class="js-accordion--body" slot="body">
        <input name="1" type="radio" />
        <input name="1" type="radio" />
        <input name="1" type="radio" />
      </div>
    </js-accordion>
    <js-accordion addClass="2" @click-event="scrollClass($event)">
      <div slot="title">アコーディオン2</div>
      <div class="js-accordion--body" slot="body">
        <div>
          <input name="1" type="radio" />
          <input name="1" type="radio" />
          <input name="1" type="radio" />
        </div>
        <div style="margin-bottom: 10px"></div>
        <div>
          <input name="1" type="radio" />
          <input name="1" type="radio" />
          <input name="1" type="radio" />
        </div>
      </div>
    </js-accordion>
    <js-accordion addClass="3" @click-event="scrollClass($event)">
      <div slot="title">アコーディオン3</div>
      <div class="js-accordion--body" slot="body">
        <input name="1" type="radio" />
        <input name="1" type="radio" />
        <input name="1" type="radio" />
      </div>
    </js-accordion>
    <js-accordion addClass="4" @click-event="scrollClass($event)">
      <div slot="title">アコーディオン3</div>
      <div class="js-accordion--body" slot="body">
        <input name="1" type="radio" />
        <input name="1" type="radio" />
        <input name="1" type="radio" />
      </div>
    </js-accordion>
    <js-accordion addClass="5" @click-event="scrollClass($event)">
      <div slot="title">アコーディオン3</div>
      <div class="js-accordion--body" slot="body">
        <input name="1" type="radio" />
        <input name="1" type="radio" />
        <input name="1" type="radio" />
      </div>
    </js-accordion>
  </div>
</template>

<script>
const axiosBase = require("axios");
const axios = axiosBase.create({
  headers: {
    "Content-Type": "application/json",
  },
});
export default {
  data() {
    return {
      toggle: null,
    };
  },
  methods: {
    scrollClass(event) {
      const element = document.getElementsByClassName(event)[0];
      console.log(element);
      element.scrollIntoView({
        behavior: "smooth",
      });
    },
  },
  async fetch({ redirect }) {
    let flag = false;
    await axios
      .get("http://127.0.0.1:8000/axios/")
      .then((res) => {
        flag = true;
      })
      .catch((e) => {
        flag = false;
      });
    if (!flag) {
      return redirect("/");
    }
  },
};
</script>

<style>
.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}

.test {
  height: 300px;
  background-color: aqua;
}
</style>
