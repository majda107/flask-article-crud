<template>
  <div class="view">
    <div class="view-new">
      <new-article />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import NewArticle from "@/components/NewArticle.vue";

export default defineComponent({
  components: {
    NewArticle,
  },
});
</script>

<style lang="scss" scoped>
.view {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 64px;

  &-new {
    width: 600px;
  }
}
</style>