<template>
  <div class="test">
    <template v-for="(content, index) in contents">
      <test
        :key="temp_test_list[index]"
        :content="content"
        classA=" test123 test"
        @delete-event="delete_methods(index)"
      ></test>
    </template>
    <button @click="add_methods()" v-if="is_add">追加する</button>
  </div>
</template>

<script>
import count from "@/mixins/count.js";
export default {
  mixins: [count],
  components: {
    test: () => import("./test.vue"),
  },
  props: ["contents", "classA", "is_add"],
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
    },
  },
};
</script>

<style scope>
.test {
  width: 300px;
}
</style>