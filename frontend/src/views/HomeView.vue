<script setup>
import { onMounted, ref } from "vue";

import apiClient from "@/api/client";
import AppLayout from "@/layouts/AppLayout.vue";


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
  <AppLayout>
    <section class="home-hero">
      <div class="home-hero-content">
        <p class="home-kicker">Tencent Video Clone</p>
        <h1>暗黑极简视频首页骨架</h1>
        <p>
          当前步骤完成顶部固定导航栏、左侧固定边栏和右侧主体滚动区。
          API 状态：{{ healthStatus }}。
        </p>
      </div>

      <div class="home-hero-panel">
        <span>Featured</span>
        <strong>固定布局验证区</strong>
      </div>
    </section>

    <section class="home-section">
      <div class="home-section-heading">
        <h2>精选内容</h2>
        <a href="/">查看全部</a>
      </div>

      <div class="home-card-grid">
        <div v-for="index in 8" :key="index" class="home-video-card">
          <div class="home-video-cover"></div>
          <p>视频卡片 {{ index }}</p>
        </div>
      </div>
    </section>
  </AppLayout>
</template>
