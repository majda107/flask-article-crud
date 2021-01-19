<template>
  <ul>
    <li
      v-for="(a, i, k) in articles"
      :key="k"
      class="card"
      :disabled="a.visible != true"
      @click="$router.push(`/article/${a.id}`)"
    >
      <!-- <h2 @click="$router.push(`/article/${a.id}`)">{{ a.title }}</h2> -->
      <!-- <button @click="remove(a)">remove</button> -->

      <div class="card-header">
        {{ a.author || "No author" }}
      </div>

      <img :src="a.image" class="card-img-top" />
      <div class="card-body">
        <h4 class="card-title">{{ a.title }}</h4>
        <p class="card-text">
          {{ a.content }}
        </p>
      </div>
    </li>
  </ul>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { fetchJsonAuth, getJson } from "@/services/fetch.service";
import ArticleModel from "@/models/article.model";
import { loggedIn } from "@/state";

export default defineComponent({
  async setup() {
    const articles = ref([] as ArticleModel[]);

    if (loggedIn.value) {
      console.log("fetching auth..");
      articles.value = (await fetchJsonAuth("articles/all")).articles;
      console.log(articles.value);
    } else {
      articles.value = (await getJson("articles")).articles;
    }

    return {
      articles,
    };
  },
});
</script>

<style lang="scss" scoped>
.card {
  width: 340px;

  img {
    width: 100%;
    height: 180px;

    object-fit: cover;
  }

  p {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  margin: 8px;

  &:hover {
    cursor: pointer;
  }
}

.card[disabled="true"] {
  opacity: 0.4;
}

ul {
  list-style-type: none;
  margin: 0;

  display: flex;
  flex-flow: row;
  flex-wrap: wrap;
}
</style>