<template>
  <a @click="test()">a</a>
</template>

<script>
// const axiosBase = require("axios");
// const axios = axiosBase.create({
//   headers: {
//     "Content-Type": "application/json",
//   },
// });
export default {
  methods: {
    async test() {
      let flag = false;
      this.$axios
        .post("axios/", { foo: "bar" })
        .then((res) => {
          flag = true;
        })
        .catch((e) => {
          flag = false;
        });
    },
  },
};
</script>

<style>
</style>
