<template>
  <div class="view">
    <div v-if="page == null">loading...</div>
    <div v-else v-html="page.content"></div>
  </div>
</template>

<script lang="ts">
import { getJson } from "@/services/fetch.service";
import { defineComponent, ref, watch } from "vue";
import { useRoute } from "vue-router";

export default defineComponent({
  setup() {
    const route = useRoute();
    const page = ref(null);

    async function update() {
      const res = await getJson(`api/page/${route.params.name}`);
      page.value = res;
    }

    // watch(route, () => {
    //   //   console.log("UPDATE");
    //   update();
    // });

    update();

    return {
      page,
    };
  },
});
</script>

<style lang="scss" scoped>
.view {
  padding: 36px;
}
</style>