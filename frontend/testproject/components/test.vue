<template>
  <div>
    <select name="horoscope" v-model="test1">
      <option v-for="i in ['', 1, 2, 3]" :key="i" :value="i">{{ i }}</option>
    </select>
    <template v-if="test1 == 1"
      ><test :test="test['contents']"></test>
    </template>
    <template v-if="test1 == 2">
      <input v-model="test['contents']['value1']" />
      <input v-model="test['contents']['value2']" />
      <input v-model="test['contents']['value3']" />
    </template>
    <template v-if="test1 == 3">
      <input v-model="test['contents']['methods']" />
      <input v-model="test['contents']['argument'][0]" />
      <input v-model="test['contents']['argument'][1]" />
      <button @click="test1_function()">追加</button>
      <template v-for="test_temp in test['contents']['content_list']">
        <div>
          <input v-model="test_temp['value1']" />
          <test :test="test_temp['contents']"></test>
        </div>
      </template>
    </template>
  </div>
</template>
<script>
export default {
  name: "test",
  props: ["test"],
  data() {
    return { test1: "" };
  },
  methods: {
    test1_function() {
      this.test["contents"]["content_list"].push({ value: 1, contents: {} });
    },
  },
  watch: {
    test1: function (newValue) {
      if (newValue == 1) {
        this.test["contents"] = {
          contents: {},
        };
      }
      if (newValue == 2) {
        this.test["contents"] = {
          value1: "",
          value2: "",
          value3: "",
        };
      }
      if (newValue == 3) {
        this.test["contents"] = {
          methods: "",
          argument: [],
          content_list: [],
        };
      }
    },
  },
};
</script>