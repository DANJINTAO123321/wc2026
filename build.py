# -*- coding: utf-8 -*-
# 玲珑Codex世界杯预测 网页生成器 v3
import sys, os
sys.path.insert(0, '.')
from teams_data import TEAMS
from group_data import GROUPS
from predictions import PREDICTIONS

def power_color(p):
    if p >= 88: return "#ff3a3a"
    if p >= 80: return "#ff8a00"
    if p >= 72: return "#ffb700"
    if p >= 65: return "#3ec46d"
    if p >= 55: return "#2bbfd3"
    if p >= 45: return "#7a8b99"
    return "#4a5158"

def power_label(p):
    if p >= 88: return "S"
    if p >= 80: return "A"
    if p >= 72: return "B"
    if p >= 65: return "C"
    if p >= 55: return "D"
    if p >= 45: return "E"
    return "F"

HTML_HEAD = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=2.0">
<meta name="theme-color" content="#0a1929">
<title>玲珑Codex世界杯预测</title>
<style>
* { margin:0; padding:0; box-sizing:border-box; -webkit-tap-highlight-color:transparent; }
html, body { font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", "Segoe UI", sans-serif; background:#0a1929; color:#dde6ef; line-height:1.6; min-height:100vh; padding-bottom:40px; -webkit-font-smoothing:antialiased; }
a { color:inherit; text-decoration:none; }

/* === 顶部品牌 === */
.brand { background: linear-gradient(135deg, #0a1929 0%, #1a3a5c 50%, #0a1929 100%); padding: 28px 16px 22px; text-align:center; position:relative; overflow:hidden; }
.brand::before { content:""; position:absolute; inset:0; background: radial-gradient(circle at 20% 30%, rgba(255,180,0,0.12), transparent 50%), radial-gradient(circle at 80% 70%, rgba(0,150,255,0.12), transparent 50%); }
.brand h1 { font-size:26px; font-weight:800; position:relative; background: linear-gradient(90deg, #ffd966, #ff6a00); -webkit-background-clip:text; background-clip:text; color:transparent; letter-spacing:2px; }
.brand .sub { margin-top:6px; font-size:13px; color:#9ab; position:relative; }
.brand .meta { margin-top:12px; display:flex; flex-wrap:wrap; gap:6px; justify-content:center; position:relative; }
.brand .meta span { background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.08); padding:3px 10px; border-radius:14px; font-size:11px; color:#a8b9c9; }

/* === 导航 === */
.nav { position:sticky; top:0; z-index:50; background:rgba(10,25,41,0.95); backdrop-filter: blur(8px); border-bottom:1px solid rgba(255,255,255,0.06); padding:8px 12px; display:flex; gap:6px; overflow-x:auto; }
.nav button { background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); color:#a8b9c9; padding:6px 12px; border-radius:14px; font-size:12px; cursor:pointer; white-space:nowrap; transition:all 0.2s; }
.nav button:hover, .nav button.active { background:#ffb700; color:#0a1929; border-color:#ffb700; font-weight:600; }

.container { max-width:1400px; margin:0 auto; padding:0 12px; }
.section { margin-top:22px; }
.section-title { font-size:16px; font-weight:700; margin-bottom:12px; padding-left:10px; border-left:3px solid #ffb700; color:#e6eef7; }

/* === 总览 === */
.overview { display:grid; grid-template-columns:repeat(2,1fr); gap:8px; margin-top:8px; }
@media(min-width:600px){ .overview { grid-template-columns:repeat(4,1fr); } }
.stat { background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:10px; text-align:center; }
.stat .v { font-size:18px; font-weight:700; color:#ffb700; }
.stat .l { font-size:11px; color:#8aa3bd; margin-top:2px; }

/* === 比分预测 网格(2-3列) === */
.matches-grid { display:grid; grid-template-columns:1fr; gap:12px; }
@media(min-width:720px){ .matches-grid { grid-template-columns:repeat(2,1fr); } }
@media(min-width:1100px){ .matches-grid { grid-template-columns:repeat(2,1fr); } }
.match-card { background:linear-gradient(180deg, rgba(255,180,0,0.04), rgba(255,180,0,0.01)); border:1px solid rgba(255,180,0,0.2); border-radius:14px; padding:14px; display:flex; flex-direction:column; }
.match-card .m-head { display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; padding-bottom:8px; border-bottom:1px solid rgba(255,180,0,0.12); }
.match-card .m-id { font-size:11px; color:#8aa3bd; background:rgba(0,0,0,0.25); padding:2px 8px; border-radius:10px; }
.match-card .m-time { font-size:12px; color:#ffd966; font-weight:600; }
.match-card .m-title { font-size:16px; font-weight:700; color:#e6eef7; margin-bottom:10px; }
.match-card .m-teams { display:flex; align-items:center; justify-content:space-around; margin:8px 0 12px; padding:12px 8px; background:rgba(0,0,0,0.25); border-radius:10px; }
.match-card .m-team { flex:1; text-align:center; }
.match-card .m-team .nm { font-size:15px; font-weight:700; margin-bottom:4px; }
.match-card .m-team .pwr { display:inline-block; padding:2px 8px; border-radius:10px; font-size:11px; font-weight:700; }
.match-card .m-vs { font-size:22px; color:#ffb700; font-weight:800; padding:0 8px; }
.match-card .m-info { font-size:12px; color:#a8b9c9; line-height:1.6; padding:8px 10px; background:rgba(0,0,0,0.2); border-radius:8px; margin-bottom:10px; }
.match-card .m-form { font-size:11px; color:#8aa3bd; padding:4px 10px; border-left:2px solid #2bbfd3; margin-bottom:10px; }
.match-card .m-factors { font-size:12px; color:#a8b9c9; margin-bottom:10px; }
.match-card .m-factors li { padding:2px 0 2px 16px; position:relative; line-height:1.5; }
.match-card .m-factors li::before { content:"·"; position:absolute; left:0; color:#ffb700; font-weight:800; top:-1px; }
.match-card .m-scores { display:grid; grid-template-columns:repeat(3,1fr); gap:6px; margin-bottom:10px; }
.match-card .m-score { background:rgba(0,0,0,0.3); border:1px solid rgba(255,180,0,0.18); border-radius:8px; padding:6px 4px; text-align:center; position:relative; }
.match-card .m-score .sc { font-size:18px; font-weight:800; color:#ffd966; }
.match-card .m-score .pc { font-size:9px; color:#3ec46d; margin-top:1px; }
.match-card .m-score .desc { font-size:9px; color:#8aa3bd; margin-top:3px; line-height:1.3; }
.match-card .m-score.top { background:linear-gradient(180deg, rgba(255,180,0,0.2), rgba(255,180,0,0.05)); border:1.5px solid #ffb700; }
.match-card .m-score.top .sc { font-size:20px; color:#ffb700; }
.match-card .m-score.top .pc { color:#ffb700; font-weight:700; }
.match-card .m-advice { background:linear-gradient(90deg, rgba(255,180,0,0.18), rgba(255,180,0,0.05)); padding:8px 10px; border-radius:8px; font-size:13px; font-weight:700; text-align:center; color:#ffd966; border:1px solid rgba(255,180,0,0.25); }

/* === 球队卡片网格(2-6列) === */
.teams { display:grid; grid-template-columns:repeat(2,1fr); gap:10px; }
@media(min-width:600px){ .teams { grid-template-columns:repeat(3,1fr); } }
@media(min-width:900px){ .teams { grid-template-columns:repeat(4,1fr); } }
@media(min-width:1200px){ .teams { grid-template-columns:repeat(5,1fr); } }
.team-card { background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:10px; position:relative; cursor:pointer; transition:transform 0.2s, border-color 0.2s; }
.team-card:hover, .team-card:active { transform:translateY(-2px); border-color:#ffb700; }
.team-card .rank { position:absolute; top:6px; right:8px; font-size:10px; color:#8aa3bd; background:rgba(0,0,0,0.3); padding:1px 5px; border-radius:6px; }
.team-card .name { font-size:14px; font-weight:700; }
.team-card .name-en { font-size:9px; color:#8aa3bd; margin-top:1px; }
.team-card .power-bar { margin-top:6px; height:6px; background:rgba(255,255,255,0.08); border-radius:3px; overflow:hidden; }
.team-card .power-fill { height:100%; border-radius:3px; }
.team-card .power-meta { display:flex; justify-content:space-between; align-items:center; margin-top:4px; }
.team-card .tier { padding:1px 5px; border-radius:5px; font-size:9px; font-weight:700; }
.team-card .power-v { font-weight:800; font-size:16px; }

/* === 详情弹层(全宽优化) === */
.modal { display:none; position:fixed; inset:0; z-index:100; background:rgba(0,0,0,0.85); overflow-y:auto; }
.modal.active { display:flex; align-items:flex-start; justify-content:center; padding:14px; }
.modal-content { background:#0f2740; border:1px solid rgba(255,255,255,0.1); border-radius:16px; max-width:560px; width:100%; margin-top:14px; padding:20px; position:relative; animation:slideUp 0.25s; }
@keyframes slideUp { from { transform:translateY(20px); opacity:0; } to { transform:translateY(0); opacity:1; } }
.modal-close { position:absolute; top:10px; right:14px; background:rgba(255,255,255,0.08); border:none; color:#fff; font-size:18px; width:32px; height:32px; border-radius:50%; cursor:pointer; }
.modal h2 { font-size:20px; margin-bottom:2px; }
.modal h2 small { font-size:11px; color:#8aa3bd; font-weight:400; margin-left:6px; }
.modal .power-big { font-size:38px; font-weight:800; text-align:center; margin:12px 0; }
.modal .row { display:flex; justify-content:space-between; padding:6px 0; border-bottom:1px solid rgba(255,255,255,0.06); font-size:13px; }
.modal .row b { color:#ffb700; }
.modal .stars-list { background:rgba(0,0,0,0.25); border-radius:10px; padding:10px; margin-top:8px; }
.modal .stars-list .item { padding:3px 0; font-size:13px; }
.modal .stars-list .item b { color:#ffd966; }
.modal .section-mini { margin-top:10px; }
.modal .section-mini h4 { font-size:13px; color:#ffb700; margin-bottom:3px; }
.modal .section-mini p { font-size:13px; color:#c8d6e2; }
.modal .matches-mini { background:rgba(0,0,0,0.25); border-radius:10px; padding:10px; margin-top:8px; }
.modal .matches-mini .item { padding:5px 0; border-bottom:1px dashed rgba(255,255,255,0.06); font-size:12px; }
.modal .matches-mini .item:last-child { border-bottom:none; }
.modal .matches-mini .item .sc { color:#ffd966; font-weight:700; }

/* === 分组赛 === */
.groups { display:grid; grid-template-columns:1fr; gap:12px; }
@media(min-width:900px){ .groups { grid-template-columns:repeat(2,1fr); } }
@media(min-width:1200px){ .groups { grid-template-columns:repeat(3,1fr); } }
.group { background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:12px; }
.group h3 { font-size:16px; color:#ffb700; margin-bottom:4px; }
.group .venue { font-size:10px; color:#8aa3bd; margin-bottom:8px; }
table.stand { width:100%; border-collapse:collapse; font-size:11px; }
table.stand th, table.stand td { padding:4px 3px; text-align:center; border-bottom:1px solid rgba(255,255,255,0.06); }
table.stand th { color:#8aa3bd; font-weight:500; font-size:9px; }
table.stand td.t { text-align:left; }
table.stand .rank1 { color:#ffb700; font-weight:700; }
table.stand .adv { color:#3ec46d; font-size:9px; }
.match-row { display:flex; align-items:center; justify-content:space-between; padding:3px 0; font-size:11px; gap:4px; }
.match-row .score { font-weight:800; color:#ffb700; min-width:34px; text-align:center; }
.match-row .team { flex:1; }
.match-row .team.left { text-align:right; }
.match-row .meta { font-size:9px; color:#8aa3bd; padding:1px 0 4px; line-height:1.3; }
.match-row.future { color:#a8b9c9; }
.match-row.future .score { color:#2bbfd3; }
.group-pred { margin-top:8px; padding:6px 8px; background:rgba(255,180,0,0.06); border-radius:6px; border-left:2px solid #ffb700; font-size:11px; }
.group-pred b { color:#ffb700; }

/* === 武力榜 === */
.power-rank { display:grid; grid-template-columns:1fr; gap:5px; }
@media(min-width:600px){ .power-rank { grid-template-columns:repeat(2,1fr); } }
@media(min-width:1100px){ .power-rank { grid-template-columns:repeat(3,1fr); } }
.pr-row { display:flex; align-items:center; gap:8px; padding:5px 8px; background:rgba(255,255,255,0.03); border-radius:6px; }
.pr-row .pos { font-weight:700; min-width:22px; text-align:center; font-size:12px; }
.pr-row .nm { flex:1; font-size:12px; }
.pr-row .pwr { font-weight:700; font-size:13px; }
.pr-row .bar { flex:2; height:5px; background:rgba(255,255,255,0.06); border-radius:3px; overflow:hidden; }
.pr-row .fill { height:100%; }

footer { text-align:center; padding:24px 16px 12px; color:#5a6e84; font-size:10px; }
footer a { color:#ffb700; }

/* === 比赛日空状态 === */
.empty-state { background:rgba(255,255,255,0.03); border:1px dashed rgba(255,180,0,0.2); border-radius:14px; padding:30px 16px; text-align:center; color:#8aa3bd; }
.empty-state .ic { font-size:36px; margin-bottom:8px; }
.empty-state .t1 { font-size:14px; color:#dde6ef; font-weight:600; margin-bottom:4px; }
.empty-state .t2 { font-size:12px; }
</style>
</head>
<body>
<div class="brand">
  <h1>玲珑Codex世界杯预测</h1>
  <div class="sub">2026 美加墨世界杯 · 48强战力 + 每日比分预测</div>
  <div class="meta">
    <span>揭幕 6/11</span>
    <span>决赛 7/19</span>
    <span>16城 104场</span>
    <span style="background:rgba(255,180,0,0.12);border-color:#ffb700;color:#ffd966">北京时间</span>
  </div>
</div>
<div class="nav">
  <button class="active" onclick="goTo('mpred')">今日预测</button>
  <button onclick="goTo('overview')">总览</button>
  <button onclick="goTo('power')">武力榜</button>
  <button onclick="goTo('groups')">分组赛况</button>
  <button onclick="goTo('teams')">48强详情</button>
</div>
"""

def team_card_html(en):
    t = TEAMS[en]
    p = t["power"]
    color = power_color(p)
    tier = power_label(p)
    stars = " · ".join(t["stars"][:2])
    return f'''<div class="team-card" onclick="showTeam('{en}')" style="border-top:3px solid {color}">
  <div class="rank">#{t["rank"]}</div>
  <div class="name">{t["zh"]}</div>
  <div class="name-en">{en}</div>
  <div class="power-bar"><div class="power-fill" style="width:{p}%;background:{color}"></div></div>
  <div class="power-meta">
    <span class="tier" style="background:{color}33;color:{color}">{tier}</span>
    <span class="power-v" style="color:{color}">{p}</span>
  </div>
  <div class="power-meta" style="margin-top:6px">
    <span style="font-size:10px;color:#8aa3bd">⭐ <span style="color:#ffd966">{t["stars"][0].split('(')[0]}</span></span>
  </div>
</div>'''

def modal_html(en):
    """详情弹层: 球队分析 + 世界杯历史战绩"""
    t = TEAMS[en]
    p = t["power"]
    color = power_color(p)
    stars_html = "".join(f'<div class="item">★ <b>{s}</b></div>' for s in t["stars"])
    # 查找该球队在本届世界杯已踢的比赛
    matches_html = ""
    for g in GROUPS:
        for (h, hs, a, asg, info) in g["played"]:
            if h == en or a == en:
                if h == en:
                    opp = TEAMS[a]["zh"]
                    score = f"{hs}-{asg}"
                else:
                    opp = TEAMS[h]["zh"]
                    score = f"{asg}-{hs}"
                matches_html += f'<div class="item">{t["zh"]} <span class="sc">{score}</span> {opp}<br><span style="color:#8aa3bd">{info[:80]}</span></div>'
        for (h, a, info) in g["remaining"]:
            if h == en or a == en:
                opp = TEAMS[a if h==en else h]["zh"]
                matches_html += f'<div class="item" style="color:#a8b9c9">⏳ {t["zh"]} <span class="sc" style="color:#2bbfd3">VS</span> {opp} <span style="color:#8aa3bd">{info}</span></div>'
    if not matches_html:
        matches_html = '<div class="item" style="color:#8aa3bd">尚未开赛</div>'
    return f'''<div class="modal" id="m-{en}">
  <div class="modal-content">
    <button class="modal-close" onclick="hideTeam('{en}')">×</button>
    <h2>{t["zh"]} <small>{en} · FIFA #{t["rank"]} · {t["tier"]}档</small></h2>
    <div class="power-big" style="color:{color}">{p} <span style="font-size:13px;color:#8aa3bd">/ 100 · {power_label(p)}级</span></div>
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
    <div class="section-mini"><h4>优势</h4><p>{t["key"]}</p></div>
    <div class="section-mini"><h4>短板</h4><p>{t["weak"]}</p></div>
    <div class="matches-mini">
      <div style="font-size:12px;color:#ffb700;margin-bottom:6px">本届世界杯战绩</div>
      {matches_html}
    </div>
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
            played_html += f'<div class="match-row"><span class="team left">{zh_h}</span><span class="score">{hs}-{asg}</span><span class="team">{zh_a}</span></div>'
            played_html += f'<div class="meta" style="padding-left:6px;padding-right:6px">⚽ {info}</div>'
    remain_html = ""
    for (h, a, info) in g["remaining"]:
        zh_h = TEAMS[h]["zh"]; zh_a = TEAMS[a]["zh"]
        remain_html += f'<div class="match-row future"><span class="team left">{zh_h}</span><span class="score">VS</span><span class="team">{zh_a}</span></div>'
        remain_html += f'<div class="meta" style="padding-left:6px;padding-right:6px">🕒 {info}</div>'
    p = g["predictions"]
    pred = f'晋级: <b>{TEAMS[p["winner"]]["zh"]}</b> · 次席: <b>{TEAMS[p["runner"]]["zh"]}</b> · 附加: <b>{TEAMS[p["third"]]["zh"]}</b>'
    return f'''<div class="group">
  <h3>第 {name} 组</h3>
  <div class="venue">📍 {venue}</div>
  <table class="stand">
    <thead><tr><th>#</th><th style="text-align:left">球队</th><th>赛</th><th>胜</th><th>平</th><th>负</th><th>进</th><th>失</th><th>分</th><th>晋级</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <div style="margin-top:8px;padding-top:6px;border-top:1px dashed rgba(255,255,255,0.1)">
    <div style="font-size:10px;color:#8aa3bd;margin-bottom:4px">已结束</div>
    {played_html}
    <div style="font-size:10px;color:#8aa3bd;margin:6px 0 4px">未踢</div>
    {remain_html}
  </div>
  <div class="group-pred">💡 {pred}</div>
</div>'''

def power_rank_html():
    items = sorted(TEAMS.items(), key=lambda x: -x[1]["power"])
    rows = ""
    for i, (en, t) in enumerate(items):
        p = t["power"]
        c = power_color(p)
        medal = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else f"{i+1}"
        rows += f'<div class="pr-row"><span class="pos">{medal}</span><span class="nm">{t["zh"]} <span style="color:#8aa3bd;font-size:10px">({t["group"]})</span></span><div class="bar"><div class="fill" style="width:{p}%;background:{c}"></div></div><span class="pwr" style="color:{c}">{p}</span></div>'
    return rows

def match_card_html(key, p):
    """单场比赛预测卡片(网格项目)"""
    h_en, a_en = p["teams"]
    h = TEAMS[h_en]
    a = TEAMS[a_en]
    ph, pa = p["powers"]
    ch, ca = power_color(ph), power_color(pa)
    lh, la = power_label(ph), power_label(pa)
    factors = "".join(f'<li>{f}</li>' for f in p["key_factors"])
    scores_html = ""
    for i, s in enumerate(p["scores"]):
        sc, pc = s[0], s[1]
        desc = s[2] if len(s) > 2 else ""
        top_class = " top" if i == 0 else ""
        scores_html += f'<div class="m-score{top_class}"><div class="sc">{sc}</div><div class="pc">{int(pc*100)}%</div><div class="desc">{desc}</div></div>'
    # key 提取 M33 等
    mid = key.split("_")[0]
    return f'''<div class="match-card">
  <div class="m-head">
    <span class="m-id">⚽ {mid}</span>
    <span class="m-time">🕒 {p["time"]}</span>
  </div>
  <div class="m-title">{p["title"]}</div>
  <div class="m-teams">
    <div class="m-team">
      <div class="nm">{h["zh"]}</div>
      <div class="pwr" style="background:{ch}33;color:{ch}">武力 {ph} · {lh}级</div>
    </div>
    <div class="m-vs">VS</div>
    <div class="m-team">
      <div class="nm">{a["zh"]}</div>
      <div class="pwr" style="background:{ca}33;color:{ca}">武力 {pa} · {la}级</div>
    </div>
  </div>
  <div class="m-info">📋 {p["context"]}</div>
  <div class="m-form">📊 {p["form"]}</div>
  <ul class="m-factors">{factors}</ul>
  <div class="m-scores">{scores_html}</div>
  <div class="m-advice">💎 {p["advice"]}</div>
</div>'''

def overview_stats():
    avg = round(sum(t["power"] for t in TEAMS.values()) / 48)
    top3 = sorted(TEAMS.values(), key=lambda x:-x["power"])[:3]
    return f'''
    <div class="overview">
      <div class="stat"><div class="v">48</div><div class="l">参赛球队</div></div>
      <div class="stat"><div class="v">12</div><div class="l">分组</div></div>
      <div class="stat"><div class="v">{len(PREDICTIONS)}</div><div class="l">今日预测</div></div>
      <div class="stat"><div class="v">{avg}</div><div class="l">平均武力</div></div>
    </div>'''

out = HTML_HEAD
out += '<div class="container">'

# 1. 今日预测(顶部, 网格布局)
out += '<div class="section" id="mpred">'
out += '<div class="section-title">⭐ 今日预测 (北京时间 6/21 凌晨-上午)</div>'
if PREDICTIONS:
    out += '<div class="matches-grid">'
    for key in ["M35_6/20","M33_6/20","M34_6/20","M36_6/20"]:
        if key in PREDICTIONS:
            out += match_card_html(key, PREDICTIONS[key])
    out += '</div>'
else:
    out += '<div class="empty-state"><div class="ic">⚽</div><div class="t1">今日暂无比赛</div><div class="t2">所有比赛日均会出预测</div></div>'
out += '</div>'

# 2. 总览
out += '<div class="section" id="overview"><div class="section-title">📊 总览</div>'
out += overview_stats()
out += '</div>'

# 3. 武力榜
out += '<div class="section" id="power"><div class="section-title">⚔ 武力榜</div>'
out += '<div class="power-rank">' + power_rank_html() + '</div></div>'

# 4. 分组赛况
out += '<div class="section" id="groups"><div class="section-title">⚽ 分组赛战况</div>'
out += '<div class="groups">'
for g in GROUPS: out += group_html(g)
out += '</div></div>'

# 5. 48强详情
out += '<div class="section" id="teams"><div class="section-title">🏟 48强 · 点击查看分析</div>'
out += '<div class="teams">'
for en in TEAMS: out += team_card_html(en)
out += '</div></div>'

out += '</div>'

# 弹层
for en in TEAMS: out += modal_html(en)

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
数据来源: 维基百科 2026 FIFA World Cup · FIFA官方 · 各大球队主页<br>
武力值为综合评估(阵容/球星/年龄/状态/历史), 仅供娱乐参考<br>
Made with love by Codex · 推到 GitHub 随时查看
</footer>
</body></html>'''

with open("index.html","w",encoding="utf-8") as f:
    f.write(out)
print("generated index.html:", len(out), "bytes")
