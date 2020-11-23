<template>
  <div>
    <button
      :class="addClass"
      class="js-accordion--trigger"
      type="button"
      @click="
        accordionToggle();
        $emit('click-event', addClass);
      "
    >
      <slot name="title"></slot>
    </button>
    <transition
      @before-enter="beforeEnter"
      @enter="enter"
      @before-leave="beforeLeave"
      @leave="leave"
      name="fade"
    >
      <div class="js-accordion--target open" v-show="isOpened">
        <slot name="body"></slot>
      </div>
    </transition>
    <div style="margin-bottom: 300px"></div>
  </div>
</template>

<script>
export default {
  props: ["addClass"],
  data() {
    return {
      isOpened: false,
    };
  },
  methods: {
    accordionToggle: function () {
      this.isOpened = !this.isOpened;
    },
    beforeEnter: function (el) {
      el.style.height = "0";
    },
    enter: function (el) {
      el.style.height = el.scrollHeight + "px";
    },
    beforeLeave: function (el) {
      el.style.height = el.scrollHeight + "px";
    },
    leave: function (el) {
      el.style.height = "0";
    },
  },
};
</script>
<style>
.open {
  border: 1px solid;
  padding-top: 20px;
  padding-bottom: 100px;
  overflow: hidden;
}
.fade-enter-active,
.fade-leave-active {
  transition: all 0.4s ease;
}
.fade-enter,
.fade-leave-to {
  padding-top: 0px;
  padding-bottom: 0px;
}
</style>