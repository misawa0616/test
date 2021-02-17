<template>
  <div class="test">
    <template v-for="(test, index) in test_list">
      {{ test.label }}
      <test-list
        :is_root="true"
        :key="temp_test_list[index]"
        :contents="test['contents']"
        classA=" test123 test"
        @delete-event="delete_methods(index)"
      ></test-list>
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
      test_list: [
        {
          label: "",
          contents: [
            {
              type: 3,
              argument: [
                { key_label: "キー", key_value: "test1" },
                { key_label: "開始", key_value: "4" },
                { key_label: "終了", key_value: "4" },
              ],
              contents: [
                {
                  if_value: "2",
                  contents: [
                    {
                      type: 2,
                      argument: [
                        { key_label: "キー", key_value: "test3" },
                        { key_label: "x軸", key_value: "219" },
                        { key_label: "y軸", key_value: "219" },
                      ],
                      contents: [],
                    },
                    {
                      type: 2,
                      argument: [
                        { key_label: "キー", key_value: "test3" },
                        { key_label: "x軸", key_value: "419" },
                        { key_label: "y軸", key_value: "419" },
                      ],
                      contents: [],
                    },
                  ],
                },
              ],
            },
          ],
        },
        {
          label: "",
          contents: [
            {
              type: 2,
              argument: [
                { key_label: "キー", key_value: "test3" },
                { key_label: "x軸", key_value: "100" },
                { key_label: "y軸", key_value: "100" },
              ],
              contents: [],
            },
          ],
        },
        {
          label: "",
          contents: [
            {
              type: 2,
              argument: [
                { key_label: "キー", key_value: "test3" },
                { key_label: "x軸", key_value: "400" },
                { key_label: "y軸", key_value: "600" },
              ],
              contents: [],
            },
          ],
        },
      ],
      label: "",
    };
  },
  methods: {
    add_methods() {
      this.add_temp();
      this.test_list.push({
        label: this.label,
        contents: [
          {
            type: "",
            argument: [],
            contents: [],
          },
        ],
      });
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