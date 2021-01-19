<template>
  <form @submit="addArticle($event)">
    <div class="form-group">
      <label>Title</label>
      <input
        type="text"
        v-model="title"
        placeholder="title"
        class="form-control"
      />
    </div>

    <div class="form-group">
      <label>Author</label>
      <input
        type="text"
        v-model="author"
        placeholder="author"
        class="form-control"
      />
    </div>

    <div class="form-group">
      <label>Image url</label>
      <input
        type="text"
        v-model="image"
        placeholder="image"
        class="form-control"
      />
    </div>

    <div class="form-group">
      <label>Content</label>
      <input
        type="text"
        v-model="content"
        placeholder="content"
        class="form-control"
      />
    </div>

    <button class="btn btn-success">Add</button>
  </form>
</template>

<script lang="ts">
import { postJson, postJsonAuth } from "@/services/fetch.service";
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  setup() {
    const title = ref("");
    const content = ref("");
    const image = ref("");
    const author = ref("");

    const router = useRouter();

    async function addArticle(e: any) {
      e.preventDefault();

      console.log(title.value);

      await postJsonAuth("articles/create", {
        title: title.value,
        content: content.value,
        image: image.value,
        author: author.value,
      });

      router.push("/articles");
    }

    return {
      title,
      content,
      image,
      ref,
      addArticle,
    };
  },
});
</script>