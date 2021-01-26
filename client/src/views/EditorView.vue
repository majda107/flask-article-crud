<template>
  <div id="editorjs"></div>
  <button @click="save()">Save</button>
</template>

<script>
import { defineComponent } from "vue";

import EditorJS from "@editorjs/editorjs";
import ImageTool from "@editorjs/image";

export default defineComponent({
  setup() {
    const editor = new EditorJS({
      holder: "editorjs",
      tools: {
        image: {
          class: ImageTool,
        },
      },
    });

    async function save() {
      const res = await editor.save();
      console.log(res);
    }

    return {
      editor,
      save,
    };
  },
});
</script>