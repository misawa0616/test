<template>
  <div :class="test2_function + classA">
    <template v-if="Object.keys(content).includes('if_value')">
      <div>
        条件:
        <input v-model="content['if_value']" />
        <button @click="add_methods()">追加</button>
      </div>
    </template>
    <template v-else>
      <select name="horoscope" v-model="content['type']">
        <option v-for="i in ['', 2, 3]" :key="i" :value="i">{{ i }}</option>
      </select>
    </template>
    <button @click="$emit('delete-event')">削除</button>

    <template v-if="content['type'] == 2">
      <display-table :content="content"></display-table>
    </template>

    <template v-if="content['type'] == 3">
      <display-table :content="content"></display-table>
      <button @click="add_if_methods()">追加</button>
    </template>

    <template v-if="content['contents']">
      <template v-if="content['contents'].length">
        <test-list
          :contents="content['contents']"
          classA=""
          @delete-event="delete_methods(index)"
        ></test-list>
      </template>
    </template>
  </div>
</template>
<script>
import count from "@/mixins/count.js";
export default {
  mixins: [count],
  components: {
    testList: () => import("./test-list.vue"),
  },
  props: ["content", "classA"],
  methods: {
    add_methods() {
      this.add_temp();
      this.content["contents"].push({
        type: "",
        argument: [],
        contents: [],
      });
    },
    add_if_methods() {
      this.add_temp();
      this.content["contents"].push({
        if_value: "",
        contents: [],
      });
    },
    delete_methods(index) {
      this.delete_temp(index);
      this.content["contents"].splice(index, 1);
    },
  },
  computed: {
    test2_function() {
      if (["", 3].includes(this.content["type"])) {
        return "box27";
      } else if ([2].includes(this.content["type"])) {
        return "box28";
      }
    },
  },
  watch: {
    "content.type": function (newValue) {
      if (newValue == "") {
        this.content.argument = [];
        this.content.contents = [];
      }
      if (newValue == 2) {
        this.content.argument = [
          { key_label: "キー", key_value: "" },
          { key_label: "x軸", key_value: "" },
          { key_label: "y軸", key_value: "" },
        ];
        this.content.contents = [];
      }
      if (newValue == 3) {
        this.content.argument = [
          { key_label: "キー", key_value: "" },
          { key_label: "開始", key_value: "" },
          { key_label: "終了", key_value: "" },
        ];
        this.content.contents = [];
      }
    },
  },
};
</script>
<style scoped>
.test123.test {
  margin-bottom: 2rem;
  padding-bottom: 0.5rem;
}
.box26 {
  position: relative;
  margin: 2rem 0;
  padding: 0.3em 0.2rem;
  border: solid 3px #95ccff;
  border-radius: 8px;
}
.box27 {
  position: relative;
  margin: 0.3rem 0 0.1rem 0;
  padding: 0.3em 0.2em 0.3rem 0.2rem;
  border: solid 3px #95ccff;
  border-radius: 8px;
}
.box28 {
  position: relative;
  margin: 0.3rem 0 0.1rem 0;
  padding: 0.3em 0.2em 0.3rem 0.2rem;
  border: solid 3px #65db92;
  border-radius: 8px;
}
</style>