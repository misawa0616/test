<template>
  <div :class="test2_function + classA">
    <button @click="$emit('delete-event')">削除</button>
    <div v-if="Object.keys(content).includes('if_value')">
      <input v-model="content['if_value']" />
      <button @click="add_methods()">追加</button>
      <template v-if="content['contents']">
        <template v-if="content['contents'].length">
          <test-list
            :is_add="false"
            :contents="content['contents']"
            classA=""
            @delete-event="delete_methods(index)"
          ></test-list>
        </template>
      </template>
    </div>
    <div v-if="!Object.keys(content).includes('if_value')">
      <select name="horoscope" v-model="test1">
        <option v-for="i in ['', 2, 3]" :key="i" :value="i">{{ i }}</option>
      </select>
    </div>
    <template v-if="test1 == 2">
      <table>
        <template v-for="(test_argument, index) in content['argument']">
          <tr :key="index">
            <td>{{ test_argument.key_label }}</td>
            <td>
              <input v-model="test_argument.key_value" />
            </td>
          </tr>
        </template>
      </table>
    </template>
    <template v-if="test1 == 3">
      <table>
        <template v-for="(test_argument, index) in content['argument']">
          <tr :key="index">
            <td>{{ test_argument.key_label }}</td>
            <td>
              <input v-model="test_argument.key_value" />
            </td>
          </tr>
        </template>
      </table>
      <button @click="add_if_methods()">追加</button>
      <template v-if="content['contents']">
        <template v-if="content['contents'].length">
          <test-list
            :is_add="false"
            :contents="content['contents']"
            classA=""
            @delete-event="delete_methods(index)"
          ></test-list>
        </template>
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
  data() {
    return { test1: "" };
  },
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
      if (["", 3].includes(this.test1)) {
        return "box27";
      } else if ([2].includes(this.test1)) {
        return "box28";
      }
    },
  },
  watch: {
    test1: function (newValue) {
      if (newValue == "") {
        this.content.type = null;
        this.content.argument = [];
        this.content.contents = [];
      }
      if (newValue == 2) {
        this.content.type = 2;
        this.content.argument = [
          { key_label: "キー", key_value: "" },
          { key_label: "x軸", key_value: "" },
          { key_label: "y軸", key_value: "" },
        ];
        this.content.contents = [];
      }
      if (newValue == 3) {
        this.content.type = 3;
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