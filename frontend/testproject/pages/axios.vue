<template></template>

<script>
const axiosBase = require("axios");
const axios = axiosBase.create({
  headers: {
    "Content-Type": "application/json",
  },
});
export default {
  async fetch({ redirect }) {
    let flag = false;
    await axios
      .get("http://192.168.0.7:8000/axios/")
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
</style>
