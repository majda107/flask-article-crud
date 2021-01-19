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
          <!-- <a class="nav-link" href="#">Articles</a> -->
          <router-link to="/articles" class="nav-link">Articles</router-link>
        </li>
        <li class="nav-item">
          <!-- <a class="nav-link" href="#">Login</a> -->
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
import { defineComponent } from "vue";
import { loggedIn } from "@/state";

export default defineComponent({
  setup() {
    return {
      loggedIn,
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
</style>
