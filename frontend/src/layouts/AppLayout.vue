<script setup>
const headerActions = [
  { label: "会员专区", icon: "VIP" },
  { label: "游戏", icon: "🎮" },
  { label: "快捷访问", icon: "⌘" },
  { label: "历史", icon: "◷" },
  { label: "创作", icon: "✎" },
  { label: "下载客户端", icon: "⇩" },
];

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
          <input type="search" placeholder="这一秒过火719播" />
          <span class="app-search-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" focusable="false">
              <path d="M10.8 4.5a6.3 6.3 0 1 1 0 12.6 6.3 6.3 0 0 1 0-12.6Zm0 1.8a4.5 4.5 0 1 0 0 9 4.5 4.5 0 0 0 0-9Zm5.1 9.1 3.7 3.7-1.3 1.3-3.7-3.7 1.3-1.3Z" />
            </svg>
          </span>
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
          :key="item.label"
          class="app-action-link"
          href="/"
        >
          <span class="app-action-icon">{{ item.icon }}</span>
          <span class="app-action-label">{{ item.label }}</span>
        </a>
        <button class="app-avatar" type="button" aria-label="登录">
          <span>登</span>
        </button>
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
