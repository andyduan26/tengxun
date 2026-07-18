<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from "vue";

import AppLayout from "@/layouts/AppLayout.vue";


const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000/api";

const banners = ref([]);
const recommendations = ref([]);
const activeIndex = ref(0);
const isBannerFading = ref(false);
const isLoading = ref(true);
const loadError = ref("");
let timer = null;

const activeBanner = computed(() => banners.value[activeIndex.value] || null);

function normalizeVideoProject(item) {
  return {
    id: item.id,
    title: item.title,
    tag: item.category,
    subtitle: item.subtitle,
    tags: item.tags,
    image: item.cover_image,
    thumbnail: item.cover_image,
    category: item.category,
    badgeText: item.badge_text,
    statusText: item.status_text,
    isBanner: item.is_banner,
    sortWeight: item.sort_weight,
  };
}

function badgeClass(item) {
  if (item.badgeText === "VIP") {
    return "is-vip";
  }
  if (item.badgeText === "独播") {
    return "is-exclusive";
  }
  if (item.badgeText === "限免中") {
    return "is-free";
  }
  return "is-default";
}

async function fetchJson(path) {
  const response = await fetch(`${API_BASE_URL}${path}`);
  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }

  const payload = await response.json();
  if (!payload.success) {
    throw new Error(payload.message || "Request failed");
  }

  return payload.data;
}

async function loadHomeData() {
  isLoading.value = true;
  loadError.value = "";

  try {
    const [bannerData, recommendationData] = await Promise.all([
      fetchJson("/home/banners/"),
      fetchJson("/home/recommendations/?category=全部"),
    ]);

    banners.value = bannerData.map(normalizeVideoProject);
    recommendations.value = recommendationData.map(normalizeVideoProject);
    activeIndex.value = 0;

    restartTimer();
  } catch (error) {
    loadError.value = "首页数据加载失败，请确认后端服务已启动。";
    stopTimer();
  } finally {
    isLoading.value = false;
  }
}

function setActiveBanner(index) {
  if (index === activeIndex.value || isBannerFading.value || banners.value.length === 0) {
    return;
  }

  isBannerFading.value = true;
  window.setTimeout(() => {
    activeIndex.value = index;
    isBannerFading.value = false;
  }, 180);
  restartTimer();
}

function nextBanner() {
  if (banners.value.length <= 1) {
    return;
  }

  setActiveBanner((activeIndex.value + 1) % banners.value.length);
}

function startTimer() {
  stopTimer();
  if (banners.value.length > 1) {
    timer = window.setInterval(nextBanner, 5000);
  }
}

function stopTimer() {
  if (timer) {
    window.clearInterval(timer);
    timer = null;
  }
}

function restartTimer() {
  stopTimer();
  startTimer();
}

onMounted(loadHomeData);
onBeforeUnmount(stopTimer);
</script>

<template>
  <AppLayout>
    <div class="home-page">
      <section class="banner" aria-label="首页视频轮播">
        <div v-if="isLoading" class="banner-loading">
          <span>正在加载首页轮播...</span>
        </div>

        <div v-else-if="loadError" class="banner-loading is-error">
          <span>{{ loadError }}</span>
        </div>

        <template v-else-if="activeBanner">
          <div :class="['banner-stage', { 'is-fading': isBannerFading }]">
            <div
              class="banner-poster"
              :style="{ '--banner-image': `url(${activeBanner.image})` }"
            ></div>

            <div class="banner-copy">
              <span class="banner-tag">{{ activeBanner.tag }}</span>
              <h1 class="banner-title">{{ activeBanner.title }}</h1>
              <p class="banner-desc">{{ activeBanner.subtitle }}</p>
              <p class="banner-meta">{{ activeBanner.tags }} · {{ activeBanner.statusText }}</p>

              <div class="banner-actions">
                <button class="banner-play" type="button">立即播放</button>
                <button class="banner-secondary" type="button">加入片单</button>
              </div>
            </div>
          </div>

          <div class="banner-thumbs" aria-label="轮播缩略图">
            <button
              v-for="(item, index) in banners"
              :key="item.id"
              :class="['banner-thumb', { 'is-active': index === activeIndex }]"
              type="button"
              @click="setActiveBanner(index)"
              @mouseenter="setActiveBanner(index)"
            >
              <span
                class="banner-thumb-cover"
                :style="{ '--thumb-image': `url(${item.thumbnail})` }"
              ></span>
              <span>
                <span class="banner-thumb-title">{{ item.title }}</span>
                <span class="banner-thumb-desc">{{ item.subtitle }}</span>
              </span>
              <span class="banner-progress"></span>
            </button>
          </div>
        </template>
      </section>

      <section class="recommend-section" aria-label="为你推荐">
        <div class="recommend-heading">
          <h2>为你推荐</h2>
          <span>接口数据 · 分类筛选 · 动态渲染</span>
        </div>

        <div v-if="isLoading" class="recommend-grid">
          <article v-for="index in 2" :key="index" class="recommend-card is-loading">
            <div class="recommend-poster"></div>
            <div class="recommend-info">
              <h3>加载中...</h3>
              <p class="recommend-tags">正在请求后端内容</p>
              <p class="recommend-quote">“请稍候”</p>
            </div>
          </article>
        </div>

        <div v-else class="recommend-grid">
          <article
            v-for="item in recommendations"
            :key="item.id"
            class="recommend-card"
          >
            <div
              class="recommend-poster"
              :style="{ '--poster-image': `url(${item.thumbnail})` }"
            >
              <span v-if="item.badgeText" :class="['recommend-badge', badgeClass(item)]">
                {{ item.badgeText }}
              </span>
              <span class="recommend-status">{{ item.statusText }}</span>
            </div>

            <div class="recommend-info">
              <button class="recommend-follow" type="button">Ξ+追</button>
              <h3>《{{ item.title }}》</h3>
              <p class="recommend-tags">{{ item.category }} {{ item.tags }}</p>
              <p class="recommend-quote">“{{ item.subtitle }}”</p>
            </div>
          </article>
        </div>
      </section>
    </div>
  </AppLayout>
</template>
