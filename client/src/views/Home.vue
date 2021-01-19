<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />

    <br />
    <span class="font-sans">Token: {{ token }}</span>

    <Login />
    <hr />

    <Suspense>
      <template #default>
        <articles />
      </template>
    </Suspense>

    <hr />

    <new-article />
  </div>
</template>

<script lang="ts">
import { defineComponent, Suspense } from "vue";
// import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src
import Login from "@/components/Login.vue";
import Articles from "@/components/Articles.vue";
import NewArticle from "@/components/NewArticle.vue";
import { token } from "@/state";

export default defineComponent({
  name: "Home",
  components: {
    // HelloWorld,
    Login,
    Articles,
    NewArticle,
  },

  setup() {
    return {
      token,
    };
  },
});
</script>
