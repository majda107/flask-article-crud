<template>
  <div>
    <form @submit="login($event)">
      <div class="from-group">
        <label>Username</label>
        <input
          type="text"
          v-model="username"
          placeholder="username"
          class="form-control"
        />
      </div>

      <div class="from-group">
        <label>Password</label>
        <input
          type="password"
          v-model="password"
          placeholder="password"
          class="form-control"
        />
      </div>

      <div class="form-group">
        <button class="btn btn-primary">Login</button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { postJson } from "@/services/fetch.service";
import { token } from "@/state";

export default defineComponent({
  setup() {
    const username = ref("");
    const password = ref("");

    async function login(e: any) {
      e.preventDefault();

      try {
        const res = await postJson("auth", {
          username: username.value,
          password: password.value,
          //   username,
          //   password,
        });

        console.log(res);
        token.value = res.access_token;
      } catch (e) {
        console.log(e);
      }
    }

    return {
      username,
      password,
      login,
    };
  },
});
</script>