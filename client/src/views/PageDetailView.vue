<template>
  <button class="btn btn-secondary" @click="$router.push('/pages')">
    Close
  </button>
  <page :name="$route.params.name" />
</template>

<script lang="ts">
import Page from "@/components/Page.vue";
import { defineComponent } from "vue";

export default defineComponent({
  components: { Page },
});
</script>