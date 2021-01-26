<template>
  <!-- <div id="editorjs"></div> -->
  <div class="editor">
    <textarea v-model="html"></textarea>
    <div v-html="html"></div>
  </div>
  <button @click="save()">Save</button>
</template>

<script>
import { defineComponent, ref } from "vue";

// import EditorJS from "@editorjs/editorjs";
// import ImageTool from "@editorjs/image";

export default defineComponent({
  setup() {
    const html = ref("");
    return {
      html,
    };
  },
  //   setup() {
  //     const editor = new EditorJS({
  //       holder: "editorjs",
  //       tools: {
  //         image: {
  //           class: ImageTool,
  //         },
  //       },
  //     });

  //     async function save() {
  //       const res = await editor.save();
  //       console.log(res);
  //     }

  //     return {
  //       editor,
  //       save,
  //     };
  //   },
});
</script>

<style lang="scss" scoped>
.editor {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 600px;
}
</style>