<template>
  <div>
    {{ keyword }}
    <label>
      <input
        list="keywords"
        type="text"
        @change="keyword = $event.target.value"
        :value="keyword"
      />
      <div></div>
      <datalist id="keywords">
        <option v-for="(user, index) in users" :key="index" id="2">
          {{ user.number }}:{{ user.name }}
        </option>
      </datalist>
    </label>
    <input type="text" v-model="selected_user.name" />
    <input type="text" v-model="selected_user.number" />
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
      selected: null,
      simpleSuggestionList: [
        "Canada",
        "China",
        "Cameroon",
        "Italy",
        "Iraq",
        "Iceland",
      ],
      focus_flag: "",
      keyword: "",
      selected_user: {
        name: "",
        number: "",
      },
    };
  },
  computed: {},
  methods: {
    test(a) {
      console.dir(a);
    },
  },
  asyncData({ redirect }) {
    return {
      users: [
        { name: "リンゴ", number: "11111" },
        { name: "ゴリラ", number: "22222" },
        { name: "ラッパ", number: "33333" },
        { name: "リンゴ", number: "44444" },
        { name: "ゴリラ", number: "55555" },
        { name: "ラッパ", number: "66666" },
        { name: "リンゴ", number: "77777" },
        { name: "ゴリラ", number: "88888" },
        { name: "ラッパ", number: "99999" },
        { name: "リンゴ", number: "11111" },
        { name: "ゴリラ", number: "22222" },
        { name: "ラッパ", number: "33333" },
        { name: "リンゴ", number: "11111" },
        { name: "ゴリラ", number: "22222" },
        { name: "ラッパ", number: "33333" },
      ],
    };
  },
};
</script>

<style>
</style>
