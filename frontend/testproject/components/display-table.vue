<template>
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
<script>
export default {
  props: ["content"],
};
</script>