<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from "vue";

import AppLayout from "@/layouts/AppLayout.vue";


const banners = [
  {
    title: "仙逆",
    tag: "腾讯视频 全网独播",
    highlight: "青宜：只此一次，却真香！",
    meta: "热血修仙 / 国漫高燃 / 每周更新",
    image:
      "https://images.unsplash.com/photo-1518709268805-4e9042af2176?auto=format&fit=crop&w=1800&q=85",
  },
  {
    title: "百花杀",
    tag: "今日上新",
    highlight: "乱世花影，一念成局",
    meta: "古装悬疑 / 情感博弈 / 高清臻彩",
    image:
      "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=1800&q=85",
  },
  {
    title: "庆余年",
    tag: "热播推荐",
    highlight: "风云再起，少年入局",
    meta: "古装权谋 / 爽感剧情 / 会员抢先看",
    image:
      "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1800&q=85",
  },
  {
    title: "长相思",
    tag: "高分剧集",
    highlight: "山海有期，相思无尽",
    meta: "东方幻想 / 情感名场面 / 沉浸观看",
    image:
      "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1800&q=85",
  },
];

const recommendations = [
  {
    title: "《仙逆》",
    tags: "动漫 东方玄幻 东方仙侠 逆袭",
    quote: "青宜：只此一次，却真香！",
    image:
      "https://images.unsplash.com/photo-1546182990-dffeafbe841d?auto=format&fit=crop&w=900&q=85",
  },
  {
    title: "《沈腾小品YYDS：笑到停不下来~》",
    tags: "综艺 沈腾 晚会 喜剧表演",
    quote: "沈腾小品YYDS：笑到停不下来~",
    image:
      "https://images.unsplash.com/photo-1527224538127-2104bb71c51b?auto=format&fit=crop&w=900&q=85",
  },
];

const activeIndex = ref(0);
let timer = null;

const activeBanner = computed(() => banners[activeIndex.value]);

function setActiveBanner(index) {
  activeIndex.value = index;
  restartTimer();
}

function nextBanner() {
  activeIndex.value = (activeIndex.value + 1) % banners.length;
}

function startTimer() {
  timer = window.setInterval(nextBanner, 5000);
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

onMounted(startTimer);
onBeforeUnmount(stopTimer);
</script>

<template>
  <AppLayout>
    <div class="home-page">
      <section class="banner" aria-label="首页视频轮播">
        <div class="banner-stage">
          <div
            class="banner-poster"
            :style="{ '--banner-image': `url(${activeBanner.image})` }"
          ></div>

          <div class="banner-copy">
            <span class="banner-tag">{{ activeBanner.tag }}</span>
            <h1 class="banner-title">{{ activeBanner.title }}</h1>
            <p class="banner-desc">{{ activeBanner.highlight }}</p>
            <p class="banner-meta">{{ activeBanner.meta }}</p>

            <div class="banner-actions">
              <button class="banner-play" type="button">立即播放</button>
              <button class="banner-secondary" type="button">加入片单</button>
            </div>
          </div>
        </div>

        <div class="banner-thumbs" aria-label="轮播缩略图">
          <button
            v-for="(item, index) in banners"
            :key="item.title"
            :class="['banner-thumb', { 'is-active': index === activeIndex }]"
            type="button"
            @click="setActiveBanner(index)"
          >
            <span
              class="banner-thumb-cover"
              :style="{ '--thumb-image': `url(${item.image})` }"
            ></span>
            <span>
              <span class="banner-thumb-title">{{ item.title }}</span>
              <span class="banner-thumb-desc">{{ item.highlight }}</span>
            </span>
            <span class="banner-progress"></span>
          </button>
        </div>
      </section>

      <section class="recommend-section" aria-label="为你推荐">
        <div class="recommend-heading">
          <h2>为你推荐</h2>
          <span>正在热播 · 高分内容 · 会员精选</span>
        </div>

        <div class="recommend-grid">
          <article
            v-for="item in recommendations"
            :key="item.title"
            class="recommend-card"
          >
            <div
              class="recommend-poster"
              :style="{ '--poster-image': `url(${item.image})` }"
            ></div>

            <div class="recommend-info">
              <button class="recommend-follow" type="button">Ξ+追</button>
              <h3>{{ item.title }}</h3>
              <p class="recommend-tags">{{ item.tags }}</p>
              <p class="recommend-quote">“{{ item.quote }}”</p>
            </div>
          </article>
        </div>
      </section>
    </div>
  </AppLayout>
</template>
