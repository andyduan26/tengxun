<script setup>
import { onMounted, ref } from "vue";

import apiClient from "@/api/client";


const healthStatus = ref("checking");

onMounted(async () => {
  try {
    const response = await apiClient.get("/health/");
    healthStatus.value = response.data?.data?.status || "unknown";
  } catch (error) {
    healthStatus.value = "offline";
  }
});
</script>

<template>
  <main class="min-h-screen bg-white text-black">
    <header class="mx-auto flex max-w-7xl items-center justify-between px-6 py-8 lg:px-10">
      <a class="text-lg font-semibold tracking-normal" href="/">Tencent Video</a>
      <nav class="hidden items-center gap-10 text-sm text-neutral-700 md:flex">
        <a href="/">精选</a>
        <a href="/">电视剧</a>
        <a href="/">电影</a>
        <a href="/">纪录片</a>
      </nav>
      <div class="text-xs uppercase tracking-normal text-neutral-500">
        API {{ healthStatus }}
      </div>
    </header>

    <section class="mx-auto grid max-w-7xl gap-12 px-6 pb-20 pt-10 lg:grid-cols-[1.1fr_0.9fr] lg:px-10 lg:pt-20">
      <div class="flex flex-col justify-center">
        <p class="mb-6 text-sm text-neutral-500">Premium Streaming Platform</p>
        <h1 class="max-w-3xl text-5xl font-semibold leading-tight tracking-normal md:text-7xl">
          为高品质影像内容建立长期增长平台
        </h1>
        <p class="mt-8 max-w-2xl text-base leading-8 text-neutral-700">
          当前阶段完成 Vue3 与 Django REST Framework 的项目初始化。后续将逐步加入首页频道、视频内容、后台管理和推荐数据。
        </p>
      </div>

      <div class="aspect-[4/5] bg-neutral-100">
        <div class="flex h-full items-end p-8">
          <div>
            <p class="text-sm text-neutral-500">Stage 1</p>
            <p class="mt-3 text-3xl font-semibold">Application Shell</p>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>
