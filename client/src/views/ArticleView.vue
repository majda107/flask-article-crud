<template>
  <div class="view">
    <button class="btn btn-secondary" @click="$router.push('/articles')">
      Back
    </button>

    <template v-if="loggedIn">
      <button v-if="!edit" class="btn btn-primary edit" @click="edit = true">
        Edit
      </button>
      <button v-else class="btn btn-success edit" @click="save()">Save</button>

      <button class="btn btn-danger edit" @click="remove()">Delete</button>
    </template>

    <form v-if="edit">
      <div class="form-group">
        <label>Title</label>
        <input v-model="article.title" class="form-control" />
      </div>
      <div class="form-group">
        <label>Author</label>
        <input v-model="article.author" class="form-control" />
      </div>
      <div class="form-group">
        <label>Image</label>
        <input v-model="article.image" class="form-control" />
      </div>
      <div class="form-group">
        <label>Content</label>
        <input v-model="article.content" class="form-control" />
      </div>
      <div class="form-group">
        <label>Visible</label>
        <input v-model="article.visible" type="checkbox" />
      </div>

      <hr />

      <ul v-for="tag in article.tags" :key="tag.id">
        <input v-model="tag.name" />
      </ul>
    </form>

    <div v-else-if="article" class="article">
      <h1>{{ article.title }}</h1>
      <small class="text-muted">By: {{ article.author || "no author" }}</small>

      <img :src="article.image" class="figure-img img-fluid rounded" />

      <p>
        {{ article.content }}
      </p>
    </div>
    <div v-else>fetching...</div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useRoute } from "vue-router";
import ArticleModel from "@/models/article.model";
import { fetchJsonAuth, getJson, postJsonAuth } from "@/services/fetch.service";
import router from "@/router";
import { loggedIn } from "@/state";

export default defineComponent({
  setup(props, ctx) {
    const route = useRoute();
    const edit = ref(false);

    const article = ref(null as ArticleModel | null);

    async function init() {
      const res = await getJson(`article/${route.params.id}`);

      console.log("Fetched article", res);
      article.value = res;
    }

    async function save() {
      const res = await postJsonAuth("articles/put", article.value, "put");
      edit.value = false;
    }

    async function remove() {
      const res = await fetchJsonAuth(
        `articles/delete/${article.value?.id}`,
        "delete"
      );
      console.log(res);

      router.push("/articles");
    }

    init();

    return {
      article,
      save,
      edit,
      remove,
      loggedIn: loggedIn,
    };
  },
});
</script>

<style lang="scss" scoped>
img {
  max-width: 340px;
}

.article {
  display: flex;
  flex-flow: column;

  margin-top: 34px;

  p {
    margin-top: 24px;
  }

  img {
    margin-top: 12px;
  }
}

.view {
  padding: 30px;
}

.edit {
  margin-left: 12px;
}

form {
  display: flex;
  flex-flow: column;
}
</style>