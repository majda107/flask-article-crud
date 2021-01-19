import { computed, ref } from "vue";

const token = ref("");
const loggedIn = computed(() => {
    return token.value?.length > 0;
});

export { token, loggedIn };