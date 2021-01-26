<template>
  <div>
    <ul>
      <li v-for="item in items" :key="item.id">
        <h2>{{ item.title }}</h2>
        <input v-model="item.link" />
        <button class="btn btn-success" @click="saveItem(item)">
          Save item
        </button>
      </li>
    </ul>

    <div class="form-group">
      <input
        class="form-control"
        v-model="itemName"
        placeholder="Menu item name"
      />
      <button class="btn btn-success" @click="addMenuItem()">Add</button>
    </div>

    <hr />

    <ul>
      <li v-for="page in pages" :key="page.id">
        <!-- <page :name="page.name" /> -->
        <h2 @click="$router.push(`/pages/${page.name}`)">{{ page.name }}</h2>
      </li>
    </ul>

    <div class="form-group">
      <input class="form-control" v-model="pageName" placeholder="Page name" />
      <button class="btn btn-success" @click="addPage()">Add</button>
    </div>

    <hr />

    <router-view></router-view>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { PageModel } from "@/models/page.model";
import { getJson, postJsonAuth } from "@/services/fetch.service";
import Page from "@/components/Page.vue";
import { MenuItem } from "@/models/menu-item.model";

export default defineComponent({
  //   components: { Page },
  setup() {
    const pages = ref([] as PageModel[]);
    const items = ref([] as MenuItem[]);

    const pageName = ref("");
    const itemName = ref("");

    async function init() {
      pages.value = await getJson("api/page");
      items.value = await getJson("api/menu");
    }

    async function saveItem(i: MenuItem) {
      const res = await postJsonAuth(`api/menu/${i.id}`, i, "put");
      console.log(res);
    }

    async function addPage() {
      const res = await postJsonAuth(`api/page/create`, {
        name: pageName.value,
        content: "",
      });

      pages.value.push(res);
    }

    async function addMenuItem() {
      const res = await postJsonAuth(`api/menu/create`, {
        title: itemName.value,
        link: "",
      });

      items.value.push(res);
    }

    init();

    return {
      pages,
      saveItem,
      items,
      pageName,
      itemName,
      addPage,
      addMenuItem,
    };
  },
});
</script>