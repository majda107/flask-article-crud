<template>
  <div>
    <form v-if="loggedIn">
      <div class="form-group">
        <input type="checkbox" v-model="filter" class="form-check-input" />
        <label class="form-check-label">Filter</label>
      </div>

      <div class="form-group">
        <input
          type="checkbox"
          v-model="favorite"
          :disabled="!filter"
          class="form-check-input"
        />
        <label class="form-check-label">Favorite</label>
      </div>
    </form>
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

          <span style="float: right" v-if="a.favorite">⭐</span>
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
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch } from "vue";
import { fetchJsonAuth, getJson } from "@/services/fetch.service";
import { loggedIn } from "@/state";
import ArticleFavoriteModel from "@/models/article-favorite.model";

export default defineComponent({
  async setup() {
    const articles = ref([] as ArticleFavoriteModel[]);
    const filter = ref(false);
    const favorite = ref(false);

    async function fetch() {
      console.log("fetching auth..");

      let url = "articles/all";
      if (filter.value) url += `?favorite=${favorite.value}`;
      const res = await fetchJsonAuth(url);

      console.log(res);
      articles.value = res.articles;
      console.log(articles.value);
    }

    watch(filter, async () => await fetch());
    watch(favorite, async () => await fetch());

    if (loggedIn.value) {
      await fetch();
    } else {
      articles.value = (await getJson("articles")).articles;
    }

    return {
      articles,
      filter,
      favorite,
      loggedIn: loggedIn,
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

form {
  margin: 32px;
}

ul {
  list-style-type: none;
  margin: 0;

  display: flex;
  flex-flow: row;
  flex-wrap: wrap;
}
</style>