<template>
  <div class="view">
    <Suspense>
      <template #default>
        <articles />
      </template>
    </Suspense>

    <button
      class="new btn btn-primary"
      @click="$router.push('/new')"
      v-if="loggedIn"
    >
      +
    </button>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import Articles from "@/components/Articles.vue";

import { loggedIn } from "@/state";

export default defineComponent({
  components: {
    Articles,
  },

  setup() {
    return {
      loggedIn,
    };
  },
});
</script>

<style lang="scss" scoped>
.new {
  border-radius: 100px;
  position: fixed;
  right: 64px;
  bottom: 64px;

  font-size: 3rem;
  width: 64px;
  height: 64px;

  padding: 0;

  display: flex;
  justify-content: center;
  align-items: center;
}

.view {
  margin-top: 24px;
}
</style>