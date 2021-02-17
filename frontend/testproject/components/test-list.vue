<template>
  <div class="">
    <template v-for="(content, index) in contents">
      <test
        :key="temp_test_list[index]"
        :content="content"
        classA=""
        @delete-event="delete_methods(index)"
      ></test>
    </template>
  </div>
</template>

<script>
import count from "@/mixins/count.js";
export default {
  mixins: [count],
  components: {
    test: () => import("./test.vue"),
  },
  props: ["contents", "classA", "is_root"],
  methods: {
    add_methods() {
      this.add_temp();
      this.contents.push({
        type: "",
        argument: [],
        contents: [],
      });
    },
    delete_methods(index) {
      this.delete_temp(index);
      this.contents.splice(index, 1);
      console.log("test");
      if (this.is_root) {
        this.$emit("delete-event");
      }
    },
  },
};
</script>

<style scope>
.test {
  width: 300px;
}
</style>