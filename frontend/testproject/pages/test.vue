<template>
  <div>
    <template v-for="(test, key) in test_list">
      <test :key="key" :test="test"></test>
    </template>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // test_list: [{ key: [], contents: {} }],
      test_list: [
        {
          key: [],
          contents: {
            actions: [
              {
                type: 1,
                argument: [3, "last"],
                position: [40, 40, 40, 9],
              },
            ],
          },
        },
        {
          key: [],
          contents: {
            methods: 1,
            argument: [0, 3],
            content_list: [
              {
                value: 1,
                contents: {
                  actions: [
                    {
                      type: 1,
                      argument: [3, "last"],
                      position: [40, 40, 40, 9],
                    },
                    {
                      type: 2,
                      argument: [3, "last"],
                      position: [40, 40, 40, 9],
                    },
                  ],
                },
              },
              {
                value: 2,
                contents: {
                  actions: [
                    {
                      type: 1,
                      argument: [3, "last"],
                      position: [40, 40, 40, 9],
                    },
                  ],
                },
              },
            ],
          },
        },
      ],
    };
  },
  methods: {},
};
</script>

<style>
</style>
