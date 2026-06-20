# -*- coding: utf-8 -*-
# 2026世界杯独立网页生成器
import sys, os
sys.path.insert(0, '.')
from teams_data import TEAMS
from group_data import GROUPS

# 等级颜色(武力值越高色越深)
def power_color(p):
    if p >= 88: return "#ff3a3a"   # S级
    if p >= 80: return "#ff8a00"   # A级
    if p >= 72: return "#ffb700"   # B级
    if p >= 65: return "#3ec46d"   # C级
    if p >= 55: return "#2bbfd3"   # D级
    if p >= 45: return "#7a8b99"   # E级
    return "#4a5158"               # F级

def power_label(p):
    if p >= 88: return "S"
    if p >= 80: return "A"
    if p >= 72: return "B"
    if p >= 65: return "C"
    if p >= 55: return "D"
    if p >= 45: return "E"
    return "F"

# HTML 模板
HTML_HEAD = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=2.0">
<meta name="theme-color" content="#0a1929">
<title>2026世界杯追踪 · 48强战力全图</title>
<style>
* { margin:0; padding:0; box-sizing:border-box; -webkit-tap-highlight-color:transparent; }
body { font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", "Segoe UI", sans-serif; background:#0a1929; color:#e6eef7; line-height:1.55; min-height:100vh; padding-bottom:60px; }
a { color:inherit; text-decoration:none; }
.hero { background: linear-gradient(135deg, #0a1929 0%, #1a3a5c 50%, #0a1929 100%); padding: 30px 16px 24px; text-align:center; position:relative; overflow:hidden; }
.hero::before { content:""; position:absolute; inset:0; background: radial-gradient(circle at 20% 30%, rgba(255,180,0,0.15), transparent 50%), radial-gradient(circle at 80% 70%, rgba(0,150,255,0.15), transparent 50%); }
.hero h1 { font-size:28px; font-weight:800; position:relative; background: linear-gradient(90deg, #ffb700, #ff6a00); -webkit-background-clip:text; background-clip:text; color:transparent; letter-spacing:1px; }
.hero .sub { margin-top:8px; font-size:14px; color:#8aa3bd; position:relative; }
.hero .meta { margin-top:14px; display:flex; flex-wrap:wrap; gap:8px; justify-content:center; position:relative; }
.hero .meta span { background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); padding:4px 12px; border-radius:20px; font-size:12px; color:#b8c9d9; }
.nav { position:sticky; top:0; z-index:50; background:rgba(10,25,41,0.95); backdrop-filter: blur(8px); border-bottom:1px solid rgba(255,255,255,0.08); padding:10px 12px; display:flex; gap:8px; overflow-x:auto; }
.nav button { background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); color:#b8c9d9; padding:8px 14px; border-radius:18px; font-size:13px; cursor:pointer; white-space:nowrap; transition:all 0.2s; }
.nav button:hover, .nav button.active { background:#ffb700; color:#0a1929; border-color:#ffb700; font-weight:600; }
.container { max-width:1400px; margin:0 auto; padding:0 14px; }
.section { margin-top:24px; }
.section-title { font-size:20px; font-weight:700; margin-bottom:14px; padding-left:10px; border-left:4px solid #ffb700; }
.overview { display:grid; grid-template-columns:repeat(2,1fr); gap:10px; margin-top:14px; }
@media(min-width:600px){ .overview { grid-template-columns:repeat(4,1fr); } }
.stat { background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:12px; text-align:center; }
.stat .v { font-size:22px; font-weight:800; color:#ffb700; }
.stat .l { font-size:11px; color:#8aa3bd; margin-top:2px; }

/* 球队卡片 */
.teams { display:grid; grid-template-columns:repeat(2,1fr); gap:10px; }
@media(min-width:600px){ .teams { grid-template-columns:repeat(3,1fr); } }
@media(min-width:900px){ .teams { grid-template-columns:repeat(4,1fr); } }
@media(min-width:1200px){ .teams { grid-template-columns:repeat(6,1fr); } }
.team-card { background:linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.01)); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:12px; position:relative; overflow:hidden; cursor:pointer; transition:transform 0.2s; }
.team-card:active { transform:scale(0.97); }
.team-card .rank { position:absolute; top:8px; right:10px; font-size:11px; color:#8aa3bd; background:rgba(0,0,0,0.3); padding:2px 6px; border-radius:8px; }
.team-card .name { font-size:15px; font-weight:700; }
.team-card .name-en { font-size:10px; color:#8aa3bd; margin-top:2px; }
.team-card .power-bar { margin-top:8px; height:8px; background:rgba(255,255,255,0.08); border-radius:4px; overflow:hidden; position:relative; }
.team-card .power-fill { height:100%; border-radius:4px; transition:width 0.6s; }
.team-card .power-meta { display:flex; justify-content:space-between; align-items:center; margin-top:6px; font-size:11px; }
.team-card .power-v { font-weight:800; font-size:18px; }
.team-card .tier { padding:1px 6px; border-radius:6px; font-size:10px; font-weight:700; }
.team-card .stars { margin-top:8px; font-size:11px; color:#b8c9d9; line-height:1.4; max-height:42px; overflow:hidden; }
.team-card .stars b { color:#ffd966; }

/* 详情弹层 */
.modal { display:none; position:fixed; inset:0; z-index:100; background:rgba(0,0,0,0.85); overflow-y:auto; }
.modal.active { display:flex; align-items:flex-start; justify-content:center; padding:14px; }
.modal-content { background:#0f2740; border:1px solid rgba(255,255,255,0.1); border-radius:18px; max-width:560px; width:100%; margin-top:14px; padding:18px; position:relative; animation:slideUp 0.25s; }
@keyframes slideUp { from { transform:translateY(20px); opacity:0; } to { transform:translateY(0); opacity:1; } }
.modal-close { position:absolute; top:10px; right:14px; background:rgba(255,255,255,0.08); border:none; color:#fff; font-size:18px; width:32px; height:32px; border-radius:50%; cursor:pointer; }
.modal h2 { font-size:22px; margin-bottom:4px; }
.modal h2 small { font-size:12px; color:#8aa3bd; font-weight:400; margin-left:6px; }
.modal .row { display:flex; justify-content:space-between; padding:6px 0; border-bottom:1px solid rgba(255,255,255,0.06); font-size:13px; }
.modal .row b { color:#ffb700; }
.modal .power-big { font-size:42px; font-weight:800; text-align:center; margin:14px 0; }
.modal .stars-list { background:rgba(0,0,0,0.25); border-radius:10px; padding:10px; margin-top:8px; }
.modal .stars-list .item { padding:3px 0; font-size:13px; }
.modal .stars-list .item b { color:#ffd966; }
.modal .section-mini { margin-top:12px; }
.modal .section-mini h4 { font-size:13px; color:#ffb700; margin-bottom:4px; }
.modal .section-mini p { font-size:13px; color:#c8d6e2; }

/* 分组赛 */
.groups { display:grid; grid-template-columns:1fr; gap:14px; }
@media(min-width:900px){ .groups { grid-template-columns:repeat(2,1fr); } }
@media(min-width:1200px){ .groups { grid-template-columns:repeat(3,1fr); } }
.group { background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:14px; }
.group h3 { font-size:18px; color:#ffb700; margin-bottom:6px; }
.group .venue { font-size:11px; color:#8aa3bd; margin-bottom:10px; }
table.stand { width:100%; border-collapse:collapse; font-size:12px; }
table.stand th, table.stand td { padding:5px 4px; text-align:center; border-bottom:1px solid rgba(255,255,255,0.06); }
table.stand th { color:#8aa3bd; font-weight:500; font-size:10px; }
table.stand td.t { text-align:left; }
table.stand .rank1 { color:#ffb700; font-weight:700; }
table.stand .adv { color:#3ec46d; font-size:10px; }
.matches { margin-top:10px; padding-top:10px; border-top:1px dashed rgba(255,255,255,0.1); }
.matches h4 { font-size:12px; color:#8aa3bd; margin-bottom:6px; }
.match { display:flex; align-items:center; justify-content:space-between; padding:5px 0; font-size:12px; gap:6px; }
.match .score { font-weight:800; color:#ffb700; min-width:42px; text-align:center; }
.match .team { flex:1; }
.match .team.left { text-align:right; }
.match .meta { font-size:10px; color:#8aa3bd; padding:2px 0 6px 0; line-height:1.3; }
.match.future { color:#b8c9d9; }
.match.future .score { color:#2bbfd3; }
.prediction { margin-top:10px; padding:8px; background:rgba(255,180,0,0.06); border-radius:8px; border-left:3px solid #ffb700; font-size:12px; }
.prediction b { color:#ffb700; }

/* 武力榜 */
.power-rank { display:grid; grid-template-columns:1fr; gap:6px; }
@media(min-width:600px){ .power-rank { grid-template-columns:repeat(2,1fr); } }
@media(min-width:1100px){ .power-rank { grid-template-columns:repeat(3,1fr); } }
.pr-row { display:flex; align-items:center; gap:10px; padding:6px 10px; background:rgba(255,255,255,0.03); border-radius:8px; }
.pr-row .pos { font-weight:800; min-width:24px; text-align:center; }
.pr-row .nm { flex:1; font-size:13px; }
.pr-row .pwr { font-weight:800; }
.pr-row .bar { flex:2; height:6px; background:rgba(255,255,255,0.06); border-radius:3px; overflow:hidden; }
.pr-row .fill { height:100%; }

footer { text-align:center; padding:30px 16px 14px; color:#5a6e84; font-size:11px; }
footer a { color:#ffb700; }
</style>
</head>
<body>
<div class="hero">
  <h1>🏆 2026 世界杯追踪</h1>
  <div class="sub">美加墨48强战力全图 · 含赛程预测与已踢战报</div>
  <div class="meta">
    <span>📅 揭幕 6/11</span>
    <span>🏁 决赛 7/19</span>
    <span>🏟 16城市</span>
    <span>⚽ 104场</span>
    <span>⏱ 数据: 6/20</span>
  </div>
</div>
<div class="nav">
  <button class="active" onclick="goTo('overview')">总览</button>
  <button onclick="goTo('power')">武力榜</button>
  <button onclick="goTo('groups')">分组赛</button>
  <button onclick="goTo('teams')">48强详情</button>
  <button onclick="goTo('preview')">淘汰赛预测</button>
</div>
"""

def team_card_html(en):
    t = TEAMS[en]
    p = t["power"]
    color = power_color(p)
    tier = power_label(p)
    stars = " · ".join(t["stars"][:2])
    return f'''<div class="team-card" onclick="showTeam('{en}')" style="border-top:3px solid {color}">
  <div class="rank">FIFA #{t["rank"]}</div>
  <div class="name">{t["zh"]}</div>
  <div class="name-en">{en}</div>
  <div class="power-bar"><div class="power-fill" style="width:{p}%;background:linear-gradient(90deg,{color},#fff8)"></div></div>
  <div class="power-meta">
    <span class="tier" style="background:{color}33;color:{color}">{tier}级</span>
    <span class="power-v" style="color:{color}">{p}</span>
  </div>
  <div class="stars">⭐ <b>{stars}</b></div>
</div>'''

def modal_html(en):
    t = TEAMS[en]
    p = t["power"]
    color = power_color(p)
    stars_html = "".join(f'<div class="item">★ <b>{s}</b></div>' for s in t["stars"])
    return f'''<div class="modal" id="m-{en}">
  <div class="modal-content">
    <button class="modal-close" onclick="hideTeam('{en}')">×</button>
    <h2>{t["zh"]} <small>{en} · FIFA #{t["rank"]} · {t["tier"]}档</small></h2>
    <div class="power-big" style="color:{color}">武力值 {p} <span style="font-size:14px;color:#8aa3bd">/ 100 · {power_label(p)}级</span></div>
    <div class="row"><span>所属分组</span><b>{t["group"]}组</b></div>
    <div class="row"><span>分档</span><b>第{t["pot"]}档</b></div>
    <div class="row"><span>主教练</span><b>{t["coach"]}</b></div>
    <div class="row"><span>队长</span><b>{t["captain"]}</b></div>
    <div class="row"><span>平均年龄</span><b>{t["avg_age"]} 岁</b></div>
    <div class="row"><span>战术风格</span><b>{t["style"]}</b></div>
    <div class="row"><span>历史最佳</span><b>{t["history"]}</b></div>
    <div class="stars-list">
      <div style="font-size:12px;color:#8aa3bd;margin-bottom:6px">核心球员</div>
      {stars_html}
    </div>
    <div class="section-mini"><h4>🟢 优势</h4><p>{t["key"]}</p></div>
    <div class="section-mini"><h4>🔴 短板</h4><p>{t["weak"]}</p></div>
  </div>
</div>'''

def group_html(g):
    name = g["name"]
    venue = g["venue"]
    rows = ""
    for i, (tm, p, w, d, l, gf, ga, pts, adv) in enumerate(g["standings"]):
        t = TEAMS[tm]
        cls = "rank1" if i == 0 else ""
        adv_html = f'<span class="adv">{adv}</span>' if adv else ""
        rows += f'<tr><td class="{cls}">{i+1}</td><td class="t">{t["zh"]}</td><td>{p}</td><td>{w}</td><td>{d}</td><td>{l}</td><td>{gf}</td><td>{ga}</td><td>{pts}</td><td>{adv_html}</td></tr>'
    played_html = ""
    for (h, hs, a, asg, info) in g["played"]:
        if h and a:
            zh_h = TEAMS[h]["zh"]; zh_a = TEAMS[a]["zh"]
            played_html += f'<div class="match"><span class="team left">{zh_h}</span><span class="score">{hs}-{asg}</span><span class="team">{zh_a}</span></div>'
            played_html += f'<div class="meta">⚽ {info}</div>'
    remain_html = ""
    for (h, a, info) in g["remaining"]:
        zh_h = TEAMS[h]["zh"]; zh_a = TEAMS[a]["zh"]
        remain_html += f'<div class="match future"><span class="team left">{zh_h}</span><span class="score">VS</span><span class="team">{zh_a}</span></div>'
        remain_html += f'<div class="meta">🕒 {info} (未踢)</div>'
    p = g["predictions"]
    pred = f'晋级: <b>{TEAMS[p["winner"]]["zh"]}</b> · 次席: <b>{TEAMS[p["runner"]]["zh"]}</b> · 附加: <b>{TEAMS[p["third"]]["zh"]}</b>'
    return f'''<div class="group">
  <h3>第 {name} 组</h3>
  <div class="venue">📍 {venue}</div>
  <table class="stand">
    <thead><tr><th>#</th><th style="text-align:left">球队</th><th>赛</th><th>胜</th><th>平</th><th>负</th><th>进</th><th>失</th><th>分</th><th>晋级</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <div class="matches">
    <h4>✅ 已结束 (R1-R2)</h4>
    {played_html}
    <h4 style="margin-top:10px">⏳ 未踢 (R3 · 6/24-25)</h4>
    {remain_html}
  </div>
  <div class="prediction">💡 预测: {pred}</div>
</div>'''

def power_rank_html():
    items = sorted(TEAMS.items(), key=lambda x: -x[1]["power"])
    rows = ""
    for i, (en, t) in enumerate(items):
        p = t["power"]
        c = power_color(p)
        medal = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else f"{i+1}"
        rows += f'<div class="pr-row"><span class="pos">{medal}</span><span class="nm">{t["zh"]} <span style="color:#8aa3bd;font-size:11px">({t["group"]}组)</span></span><div class="bar"><div class="fill" style="width:{p}%;background:{c}"></div></div><span class="pwr" style="color:{c}">{p}</span></div>'
    return rows

# 淘汰赛预测
def knockout_pred():
    # 假设A1..L1 + 8个最佳第3晋级
    g_winners = [TEAMS[g["predictions"]["winner"]]["zh"] for g in GROUPS]
    g_runners = [TEAMS[g["predictions"]["runner"]]["zh"] for g in GROUPS]
    g_thirds = [TEAMS[g["predictions"]["third"]]["zh"] for g in GROUPS]
    # 32强对阵(简版)
    r32 = [
        ("A1 vs B/C/D 3rd", g_winners[0]),
        ("C1 vs F2/I3/J3", g_winners[2]),
        ("E1 vs A/B/C/D 3rd", g_winners[4]),
        ("G1 vs H/J/K 3rd", g_winners[6]),
        ("I1 vs D2/E3/F3", g_winners[8]),
        ("K1 vs B3/H3/L3", g_winners[10]),
        ("B1 vs A/C/D/F 3rd", g_winners[1]),
        ("D1 vs B/E/H 3rd", g_winners[3]),
        ("F1 vs C/E/I 3rd", g_winners[5]),
        ("H1 vs G2/K3/L3", g_winners[7]),
        ("J1 vs D3/F3/L3", g_winners[9]),
        ("L1 vs H2/I3/K3", g_winners[11]),
    ]
    rows = ""
    for desc, team in r32:
        rows += f'<div class="pr-row"><span class="nm">{desc}</span><span class="pwr" style="color:#ffb700">→ {team}</span></div>'
    return rows

# 总览统计
def overview_stats():
    avg = round(sum(t["power"] for t in TEAMS.values()) / 48)
    top3 = sorted(TEAMS.values(), key=lambda x:-x["power"])[:3]
    return f'''
    <div class="overview">
      <div class="stat"><div class="v">48</div><div class="l">参赛球队</div></div>
      <div class="stat"><div class="v">12</div><div class="l">分组 (A-L)</div></div>
      <div class="stat"><div class="v">104</div><div class="l">总场次</div></div>
      <div class="stat"><div class="v">{avg}</div><div class="l">平均武力</div></div>
    </div>
    <div class="overview" style="margin-top:10px">
      <div class="stat"><div class="v">🥇 {top3[0]["zh"]}</div><div class="l">武力王者 · {top3[0]["power"]}</div></div>
      <div class="stat"><div class="v">🥈 {top3[1]["zh"]}</div><div class="l">第二把交椅 · {top3[1]["power"]}</div></div>
      <div class="stat"><div class="v">🥉 {top3[2]["zh"]}</div><div class="l">第三极 · {top3[2]["power"]}</div></div>
      <div class="stat"><div class="v">⚽ 72</div><div class="l">已进球 (R1+R2)</div></div>
    </div>'''

# 拼装
out = HTML_HEAD
out += '<div class="container">'
out += '<div class="section" id="overview"><div class="section-title">📊 总览</div>'
out += overview_stats()
out += '</div>'

out += '<div class="section" id="power"><div class="section-title">⚔ 武力榜 (48强排名)</div>'
out += '<div class="power-rank">' + power_rank_html() + '</div></div>'

out += '<div class="section" id="groups"><div class="section-title">⚽ 小组赛战况 (A-L)</div>'
out += '<div class="groups">'
for g in GROUPS: out += group_html(g)
out += '</div></div>'

out += '<div class="section" id="teams"><div class="section-title">🏟 48强卡片 · 点击查看详情</div>'
out += '<div class="teams">'
for en in TEAMS: out += team_card_html(en)
out += '</div></div>'

out += '<div class="section" id="preview"><div class="section-title">🔮 淘汰赛预测 (32强晋级)</div>'
out += '<div class="power-rank">' + knockout_pred() + '</div>'
out += '<div class="prediction" style="margin-top:14px">💡 注: 基于各组前2名+8个最佳第3名晋级; 预测由小组赛表现+武力值综合得出,实际对阵将随抽签而定。</div></div>'

out += '</div>'

# 弹层
for en in TEAMS: out += modal_html(en)

# 脚本
out += '''<script>
function goTo(id){
  const el=document.getElementById(id);
  if(el) el.scrollIntoView({behavior:"smooth",block:"start"});
  document.querySelectorAll(".nav button").forEach(b=>b.classList.remove("active"));
  event.target.classList.add("active");
}
function showTeam(en){document.getElementById("m-"+en).classList.add("active");document.body.style.overflow="hidden";}
function hideTeam(en){document.getElementById("m-"+en).classList.remove("active");document.body.style.overflow="";}
document.querySelectorAll(".modal").forEach(m=>m.addEventListener("click",e=>{if(e.target===m){m.classList.remove("active");document.body.style.overflow="";}}));
</script>
<footer>
📚 数据来源: 维基百科 2026年國際足協世界盃 · FIFA官方 · 各大球队主页<br>
⚔ 武力值为综合评估(阵容深度/球星/年龄/状态/历史),非官方 · 仅供娱乐参考<br>
🏆 Made with ❤️ by Codex · 离线可用 · 推到GIT随时查看
</footer>
</body></html>'''

with open("index.html","w",encoding="utf-8") as f:
    f.write(out)
print("generated index.html:", len(out), "bytes")
