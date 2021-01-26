<template>
  <!-- <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div> -->

  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <span class="navbar-brand mb-0 h1">My-flask</span>

    <div class="navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link to="/articles" class="nav-link">Articles</router-link>
        </li>

        <li class="nav-item">
          <router-link to="/pages" class="nav-link">Pages</router-link>
        </li>

        <!-- <li class="nav-item" v-for="i in menu" :key="i.id">
          <router-link class="nav-link" :href="i.link">{{
            i.title
          }}</router-link>
        </li> -->

        <li class="nav-item">
          <div class="divider"></div>
        </li>

        <li class="nav-item" v-for="it in menu" :key="it">
          <router-link class="nav-link" :to="`/page/${it.link}`">{{
            it.title
          }}</router-link>
          <!-- <a class="nav-link" :href="it.link">
            {{ it.title }}
          </a> -->
        </li>
      </ul>
    </div>

    <div class="my-lg-0">
      <router-link to="/login" class="nav-link login">{{
        loggedIn ? "Logout" : "Login"
      }}</router-link>
    </div>
  </nav>

  <router-view />
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { loggedIn } from "@/state";
import { getJson } from "./services/fetch.service";
import { MenuItem } from "@/models/menu-item.model";

export default defineComponent({
  setup() {
    const menu = ref([] as MenuItem[]);

    async function getMenuItems() {
      menu.value = (await getJson("api/menu")) as MenuItem[];
      console.log(menu.value);
    }

    getMenuItems();

    return {
      loggedIn,
      menu,
    };
  },
});
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.navbar-brand {
  margin-left: 24px;
}

.login {
  margin-right: 18px;
}

.divider {
  width: 1px;
  height: 100%;
  background-color: gray;
  margin: 0 12px;
}
</style>
