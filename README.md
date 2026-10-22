# 门店经营 · 碰一碰营销工作台

面向门店经营场景的响应式交互 Demo，展示门店配置、顾客页面装修、共用素材库和经营数据。

[在线体验](https://store-operations-demo.pages.dev/) · [单文件源码](门店经营.html)

## 功能

- 首页：门店与素材汇总、打开碰一碰趋势、按时间和门店筛选的数据。
- 门店管理：搜索、启停、新建、编辑、门店二维码及链接。
- 门店设置：基础信息、Logo、Wi-Fi、个人/企业微信、平台与团购链接。
- 页面装修：活动页面名称、顶部封面、页面背景，各类别的平台入口独立开关和实时预览。
- 素材库：共用视频、图片与文案，支持上传、编辑、下载及批量管理；已内置演示素材。
- AI 对话：以本地规则模拟配置与文案工作流，便于体验产品交互。

## 本地预览

无需安装运行依赖。所有样式、脚本和演示媒体都包含在 `门店经营.html` 中。

```sh
git clone https://github.com/geyaovip/store-operations-demo.git
cd store-operations-demo
python3 -m http.server 8798 --bind 127.0.0.1
```

访问 `http://127.0.0.1:8798/门店经营.html`，也可以单独转发 HTML 文件。

## 构建与发布

```sh
python3 工具/构建静态站.py
python3 工具/部署Cloudflare.py
```

构建仅把原始 HTML 复制为 `dist/index.html`，并附加 `_headers`。Cloudflare Pages 项目为 `store-operations-demo`，生产分支为 `main`，采用 Pages Direct Upload（脚本用 `--force` 保持 Pages 部署路径）。GitHub 推送与站点发布分别执行；发布需本机已有 Wrangler 授权。

Git 仅提交源码、说明和部署工具；不提交本机授权、浏览器记录、验收截图及生成的 `dist`。

## 演示范围

此项目是静态前端 Demo，使用预置数据和当前浏览器的本地存储；不同域名、端口和设备的数据相互独立。本地预览中的编辑数据不会随部署上传。

未接入生产登录、服务端数据同步、真实 AI 模型、正式 NFC/二维码服务或平台投稿接口。素材下载、入口点击和本地模拟流程不代表已在外部平台发布成功。
