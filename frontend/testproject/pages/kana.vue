<template>
  <div>
    <input v-model="test" />
    <button @click="clickNext()">カナ文字チェック</button>
    {{ message }}
    03
  </div>
</template>
<script>
export default {
  data() {
    return {
      test: "",
      message: "",
    };
  },
  methods: {
    clickNext() {
      this.message = "";
      let str = this.test == null ? "" : this.test;
      if (str.match(/^[ァ-ヶー　]+$/)) {
        this.message = "カナ文字です";
      } else {
        this.message = "カナ文字ではありません。";
      }
    },
  },
};
</script>