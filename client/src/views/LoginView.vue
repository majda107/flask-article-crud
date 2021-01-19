<template>
  <div class="view">
    <login v-if="!loggedIn" />
    <button v-else class="btn btn-danger" @click="token = ''">Logout</button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Login from "@/components/Login.vue";
import { loggedIn, token } from "@/state";

export default defineComponent({
  components: {
    Login,
  },

  setup() {
    return {
      loggedIn,
      token,
    };
  },
});
</script>

<style lang="scss" scoped>
.view {
  display: flex;
  justify-content: center;
  align-items: center;

  margin-top: 64px;
}
</style>