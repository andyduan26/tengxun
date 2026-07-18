<script setup>
const navItems = ["首页", "电视剧", "电影", "综艺", "动漫", "纪录片"];

const sideItems = [
  "精选",
  "正在热播",
  "会员专区",
  "腾讯出品",
  "排行榜",
  "观看历史",
];
</script>

<template>
  <div class="app-shell">
    <header class="app-header">
      <a class="app-logo" href="/">
        <span class="app-logo-mark"></span>
        <span>腾讯视频</span>
      </a>

      <nav class="app-top-nav" aria-label="主频道">
        <a
          v-for="item in navItems"
          :key="item"
          :class="['app-top-nav-link', { 'is-active': item === '首页' }]"
          href="/"
        >
          {{ item }}
        </a>
      </nav>

      <div class="app-header-actions">
        <label class="app-search">
          <span class="sr-only">搜索</span>
          <input type="search" placeholder="搜索电影、电视剧、综艺" />
        </label>
        <button class="app-login-button" type="button">登录</button>
      </div>
    </header>

    <aside class="app-sidebar" aria-label="内容导航">
      <nav class="app-side-nav">
        <a
          v-for="item in sideItems"
          :key="item"
          :class="['app-side-nav-link', { 'is-active': item === '精选' }]"
          href="/"
        >
          {{ item }}
        </a>
      </nav>
    </aside>

    <main class="app-main">
      <slot />
    </main>
  </div>
</template>
