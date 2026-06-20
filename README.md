# 🏆 2026 世界杯追踪 · 48强战力全图

一个独立可离线打开的 HTML 网页,带您了解2026美加墨世界杯: 12个分组 · 48支球队 · 全部赛程 + 已踢战报 + 第3轮未踢场次预测 + 每支球队武力值评估。

## 📁 文件

- `index.html` — 独立网页 (130KB,所有CSS/JS内嵌,无需联网,移动端友好)
- `teams_data.py` — 48支球队评估数据(阵容/年龄/教练/武力值/优势/短板)
- `group_data.py` — 12个分组的赛程数据(已踢战报 + 第3轮预测)
- `build.py` — 生成器: 数据 -> `index.html`

## 🔄 更新数据

```bash
python build.py
```

## 🌐 部署到 GIT (GitHub Pages)

```bash
git init
git add .
git commit -m "2026世界杯追踪v1"
git branch -M main
git remote add origin https://github.com/你的用户名/wc2026.git
git push -u origin main
```

然后在 GitHub 仓库 **Settings → Pages** 选择 `main` 分支根目录,几分钟内就能得到 `https://你的用户名.github.io/wc2026/` 公开链接,手机随时点开。

## ⚔ 武力值评分逻辑

满分100,最低1。综合考虑:
- 阵容深度(归化/旅欧球员群)
- 核心球星(MVP级别)
- 平均年龄(26-28为黄金期)
- 教练战术
- 历史大赛表现
- 本届小组赛当前战绩

等级: S(88+), A(80+), B(72+), C(65+), D(55+), E(45+), F(<45)

## 📊 数据时间

数据快照: 2026-06-20 (揭幕后,各组已踢完 R1+R2, R3 未踢)
来源: 维基百科 2026年國際足協世界盃 · FIFA 官方

## ⚠️ 免责声明

本网页为爱好/预测性质,武力值为编辑综合评估,非官方数据。所有比赛结果以 FIFA 官方公告为准。
