import { readFileSync } from "node:fs";
import { resolve } from "node:path";


const root = process.cwd();

const files = {
  layout: readFileSync(resolve(root, "src/layouts/AppLayout.vue"), "utf8"),
  home: readFileSync(resolve(root, "src/views/HomeView.vue"), "utf8"),
  css: readFileSync(resolve(root, "src/assets/main.css"), "utf8"),
};

const assertions = [
  ["layout contains fixed header", files.layout.includes("app-header")],
  ["header contains quick access", files.layout.includes("快捷访问")],
  ["header contains avatar placeholder", files.layout.includes("app-avatar")],
  ["header action icons are rendered", files.layout.includes("app-action-icon")],
  ["search placeholder is exact", files.layout.includes('placeholder="这一秒过火719播"')],
  ["search icon is on the right", files.layout.indexOf("<input type=\"search\"") < files.layout.indexOf("app-search-icon")],
  ["layout contains fixed sidebar", files.layout.includes("app-sidebar")],
  ["layout contains scrollable main", files.layout.includes("app-main")],
  ["layout uses Tencent green", files.css.includes("#00cc4c")],
  ["layout uses dark background", files.css.includes("#0f0f0f") || files.css.includes("#121212")],
  ["header is fixed", files.css.includes(".app-header") && files.css.includes("position: fixed")],
  ["search expands by 50px on focus", files.css.includes("width: min(100%, 470px)") && files.css.includes("width: min(100%, 520px)")],
  ["search transition is smooth", files.css.includes("transition: width 180ms ease") || files.css.includes("transition: width 200ms ease")],
  ["search focus border is Tencent green", files.css.includes(".app-search-wrap:focus-within .app-search") && files.css.includes("border-color: #00cc4c")],
  ["avatar is circular", files.css.includes(".app-avatar") && files.css.includes("border-radius: 50%")],
  ["sidebar is fixed", files.css.includes(".app-sidebar") && files.css.includes("position: fixed")],
  ["main scrolls", files.css.includes(".app-main") && files.css.includes("overflow-y: auto")],
  ["recommendation data contains Xian Ni", files.home.includes("《仙逆》")],
  ["recommendation data contains Shen Teng", files.home.includes("《沈腾小品YYDS：笑到停不下来~》")],
  ["recommendation grid is two columns", files.css.includes(".recommend-grid") && files.css.includes("grid-template-columns: repeat(2, minmax(0, 1fr))")],
  ["recommendation cards lift on hover", files.css.includes(".recommend-card:hover") && files.css.includes("translateY(-4px)")],
  ["follow button turns green on hover", files.css.includes(".recommend-follow:hover") && files.css.includes("background: #00cc4c")],
  ["banner has hover switching", files.home.includes("@mouseenter=\"setActiveBanner(index)\"")],
  ["banner has fade state", files.home.includes("isBannerFading") && files.home.includes("is-fading")],
  ["banner auto plays every five seconds", files.home.includes("window.setInterval(nextBanner, 5000)")],
  ["banner has dark-to-transparent overlay", files.css.includes("linear-gradient(0deg, #121212 0%, rgba(18, 18, 18, 0) 70%)")],
  ["banner fades poster and copy", files.css.includes(".banner-poster") && files.css.includes("transition: opacity 260ms ease") && files.css.includes(".banner-copy")],
  ["banner is full-width stage", files.css.includes(".banner") && files.css.includes("grid-template-columns: 1fr")],
  ["banner has explicit large height", files.css.includes("height: clamp(560px, 64vh, 760px)")],
  ["banner thumbs overlay the poster", files.css.includes(".banner-thumbs") && files.css.includes("position: absolute")],
];

const failures = assertions.filter(([, passed]) => !passed);

if (failures.length > 0) {
  for (const [label] of failures) {
    console.error(`FAIL: ${label}`);
  }
  process.exit(1);
}

console.log("Layout structure verified.");
