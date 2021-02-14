<template>
  <div :class="test2_function + classA">
    <div v-if="Object.keys(test).includes('label')">
      {{ test["label"] }}
    </div>
    <button @click="$emit('delete-event')">削除</button>
    <div v-if="Object.keys(test).includes('if_value')">
      <input v-model="test['value']" />
    </div>
    <select name="horoscope" v-model="test1">
      <option v-for="i in ['', 2, 3]" :key="i" :value="i">{{ i }}</option>
    </select>
    <template v-if="test1 == 2">
      <table>
        <template
          v-for="(test_argument, index) in test['contents']['argument']"
        >
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
        <template
          v-for="(test_argument, index) in test['contents']['argument']"
        >
          <tr :key="index">
            <td>{{ test_argument.key_label }}</td>
            <td>
              <input v-model="test_argument.key_value" />
            </td>
          </tr>
        </template>
      </table>
      <button @click="add_methods()">追加</button>
      <template v-for="(test_temp, index) in test['contents']['contents_list']">
        <test
          :test="test_temp"
          classA=""
          :key="temp_test_list[index]"
          @delete-event="delete_methods(index)"
        ></test>
      </template>
    </template>
  </div>
</template>
<script>
import count from "@/mixins/count.js";
export default {
  mixins: [count],
  name: "test",
  props: ["test", "classA"],
  data() {
    return { test1: "" };
  },
  methods: {
    add_methods() {
      this.add_temp();
      this.test["contents"]["contents_list"].push({
        if_value: 1,
        contents: {},
      });
    },
    delete_methods(index) {
      this.delete_temp(index);
      this.test["contents"]["contents_list"].splice(index, 1);
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
        this.test["contents"] = {
          type: null,
          contents: {},
        };
      }
      if (newValue == 2) {
        this.test["contents"] = {
          type: 2,
          argument: [
            { key_label: "キー", key_value: "" },
            { key_label: "x軸", key_value: "" },
            { key_label: "y軸", key_value: "" },
          ],
        };
      }
      if (newValue == 3) {
        this.test["contents"] = {
          type: 3,
          argument: [
            { key_label: "キー", key_value: "" },
            { key_label: "開始", key_value: "" },
            { key_label: "終了", key_value: "" },
          ],
          contents_list: [],
        };
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