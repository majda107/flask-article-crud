<template>
  <div v-if="page == null">Loading...</div>
  <div v-else>
    <h2>{{ page.name }} | {{ page.id }}</h2>
    <button class="btn btn-primary" @click="save()">Save</button>

    <div class="editor">
      <textarea v-model="page.content"></textarea>
      <div v-html="page.content"></div>
    </div>
  </div>
</template>

<script lang="ts">
import { PageModel } from "@/models/page.model";
import { getJson, postJsonAuth } from "@/services/fetch.service";
import { defineComponent, ref, watch } from "vue";

export default defineComponent({
  props: {
    name: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const page = ref(null as PageModel | null);

    async function getPage() {
      page.value = await getJson(`api/page/${props.name}`);
    }

    watch(
      () => props.name,
      () => {
        getPage();
      }
    );

    async function save() {
      const res = await postJsonAuth(
        `api/page/${page.value?.id}`,
        page.value,
        "put"
      );
      page.value = res;
    }

    getPage();

    return {
      page,
      save,
    };
  },
});
</script>

<style lang="scss" scoped>
.editor {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 320px;
}
</style>