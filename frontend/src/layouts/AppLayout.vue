<script setup>
const headerActions = ["会员专区", "游戏", "历史", "创作", "下载客户端", "登录"];

const sidebarItems = [
  "首页",
  "VIP会员",
  "电视剧",
  "电影",
  "综艺",
  "动漫",
  "少儿",
  "NBA",
  "短剧",
  "纪录片",
];

const hotSearches = [
  "仙逆 王林化神",
  "百花杀 今日开播",
  "这一秒过火719播",
  "庆余年第二季",
  "长相思 名场面",
];
</script>

<template>
  <div class="app-shell">
    <header class="app-header">
      <a class="app-logo" href="/" aria-label="腾讯视频首页">
        <span class="app-logo-mark"></span>
        <span>腾讯视频</span>
      </a>

      <div class="app-search-wrap">
        <label class="app-search">
          <span class="app-search-icon">⌕</span>
          <input type="search" placeholder="这一秒过火719播" />
        </label>

        <div class="app-search-panel">
          <p class="app-search-panel-title">热门搜索</p>
          <ol class="app-hot-list">
            <li v-for="(item, index) in hotSearches" :key="item">
              <span class="app-hot-rank">{{ index + 1 }}</span>
              <span>{{ item }}</span>
            </li>
          </ol>
        </div>
      </div>

      <nav class="app-header-actions" aria-label="用户功能">
        <a
          v-for="item in headerActions"
          :key="item"
          :class="['app-action-link', { 'is-primary': item === '登录' }]"
          href="/"
        >
          {{ item }}
        </a>
      </nav>
    </header>

    <aside class="app-sidebar">
      <nav class="app-side-nav" aria-label="频道导航">
        <a
          v-for="item in sidebarItems"
          :key="item"
          :class="['app-side-link', { 'is-active': item === '首页' }]"
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
