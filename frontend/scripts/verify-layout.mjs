import { readFileSync } from "node:fs";
import { resolve } from "node:path";


const root = process.cwd();

const files = {
  layout: readFileSync(resolve(root, "src/layouts/AppLayout.vue"), "utf8"),
  css: readFileSync(resolve(root, "src/assets/main.css"), "utf8"),
};

const assertions = [
  ["layout contains fixed header", files.layout.includes("app-header")],
  ["header contains quick access", files.layout.includes("快捷访问")],
  ["header contains avatar placeholder", files.layout.includes("app-avatar")],
  ["search placeholder is exact", files.layout.includes('placeholder="这一秒过火719播"')],
  ["search icon is on the right", files.layout.indexOf("<input type=\"search\"") < files.layout.indexOf("app-search-icon")],
  ["layout contains fixed sidebar", files.layout.includes("app-sidebar")],
  ["layout contains scrollable main", files.layout.includes("app-main")],
  ["layout uses Tencent green", files.css.includes("#00cc4c")],
  ["layout uses dark background", files.css.includes("#0f0f0f") || files.css.includes("#121212")],
  ["header is fixed", files.css.includes(".app-header") && files.css.includes("position: fixed")],
  ["search expands by 50px on focus", files.css.includes("width: min(100%, 470px)") && files.css.includes("width: min(100%, 520px)")],
  ["search transition is smooth", files.css.includes("transition: width 180ms ease") || files.css.includes("transition: width 200ms ease")],
  ["avatar is circular", files.css.includes(".app-avatar") && files.css.includes("border-radius: 50%")],
  ["sidebar is fixed", files.css.includes(".app-sidebar") && files.css.includes("position: fixed")],
  ["main scrolls", files.css.includes(".app-main") && files.css.includes("overflow-y: auto")],
];

const failures = assertions.filter(([, passed]) => !passed);

if (failures.length > 0) {
  for (const [label] of failures) {
    console.error(`FAIL: ${label}`);
  }
  process.exit(1);
}

console.log("Layout structure verified.");
