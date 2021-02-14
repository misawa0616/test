<template>
  <div class="test">
    <template v-for="(test, index) in test_list">
      <test
        :key="temp_test_list[index]"
        :test="test"
        classA=" test123 test"
        @delete-event="delete_methods(index)"
      ></test>
    </template>
    <button @click="add_methods()">追加する</button>
    <input v-model="label" />
    <button @click="send_methods()">送信する</button>
  </div>
</template>

<script>
import count from "@/mixins/count.js";
export default {
  mixins: [count],
  data() {
    return {
      test_list: [],
      label: "",
    };
  },
  methods: {
    add_methods() {
      this.add_temp();
      this.test_list.push({ label: this.label, key: [], contents: {} });
    },
    delete_methods(index) {
      this.delete_temp(index);
      this.test_list.splice(index, 1);
    },
    send_methods() {
      this.$axios.$post("http://127.0.0.1:8000/axios/pdf/", {
        test_list: this.test_list,
      });
    },
  },
};
</script>

<style scope>
.test {
  width: 300px;
}
</style>