import { defineStore } from "pinia";


export const useAppStore = defineStore("app", {
  state: () => ({
    brandName: "Tencent Video",
  }),
});
