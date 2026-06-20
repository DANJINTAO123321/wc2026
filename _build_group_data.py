# -*- coding: utf-8 -*-
import os, sys, re, json
sys.stdout.reconfigure(encoding="utf-8")

WIKI = r"C:\Users\Administrator\Documents\世界杯"
matches = json.load(open(os.path.join(WIKI, "_all_matches.json"), encoding="utf-8"))

# Wiki name -> our key
KEY = {
    "Mexico":"Mexico", "South Korea":"South Korea", "Czech Republic":"Czech",
    "South Africa":"South Africa", "Canada":"Canada", "Switzerland":"Switzerland",
    "Bosnia and Herzegovina":"Bosnia", "Qatar":"Qatar", "Brazil":"Brazil",
    "Morocco":"Morocco", "Scotland":"Scotland", "Haiti":"Haiti",
    "United States":"USA", "Paraguay":"Paraguay", "Australia":"Australia",
    "Turkey":"Turkey", "Germany":"Germany", "Ivory Coast":"Ivory Coast",
    "Ecuador":"Ecuador", "Curaçao":"Curacao", "Netherlands":"Netherlands",
    "Japan":"Japan", "Sweden":"Sweden", "Tunisia":"Tunisia", "Spain":"Spain",
    "Uruguay":"Uruguay", "Saudi Arabia":"Saudi Arabia", "Cape Verde":"Cabo Verde",
    "France":"France", "Norway":"Norway", "Senegal":"Senegal", "Iraq":"Iraq",
    "Argentina":"Argentina", "Austria":"Austria", "Algeria":"Algeria", "Jordan":"Jordan",
    "Portugal":"Portugal", "Colombia":"Colombia", "DR Congo":"Congo DR",
    "Uzbekistan":"Uzbekistan", "Iran":"Iran", "New Zealand":"New Zealand",
    "Belgium":"Belgium", "Egypt":"Egypt", "Ghana":"Ghana", "Panama":"Panama",
    "Croatia":"Croatia", "England":"England",
}

# Standings helper: compute from played
def compute_standings(L):
    teams = [m["home"] for m in matches[L]["played"][:1]]  # placeholder
    # Better: from played list
    stats = {}
    for m in matches[L]["played"]:
        h, a = KEY.get(m["home"], m["home"]), KEY.get(m["away"], m["away"])
        sh, sa = m["score"].split("-")
        sh, sa = int(sh), int(sa)
        for k in (h, a):
            stats.setdefault(k, {"P":0,"W":0,"D":0,"L":0,"GF":0,"GA":0,"Pts":0})
        stats[h]["P"]+=1; stats[a]["P"]+=1
        stats[h]["GF"]+=sh; stats[h]["GA"]+=sa
        stats[a]["GF"]+=sa; stats[a]["GA"]+=sh
        if sh>sa: stats[h]["W"]+=1; stats[h]["Pts"]+=3; stats[a]["L"]+=1
        elif sh<sa: stats[a]["W"]+=1; stats[a]["Pts"]+=3; stats[h]["L"]+=1
        else: stats[h]["D"]+=1; stats[a]["D"]+=1; stats[h]["Pts"]+=1; stats[a]["Pts"]+=1
    # Order by Pts desc, GD desc, GF desc
    ordered = sorted(stats.items(), key=lambda x:(-x[1]["Pts"], -(x[1]["GF"]-x[1]["GA"]), -x[1]["GF"]))
    return ordered

VENUE = {
    "A":"墨西哥城/瓜达拉哈拉", "B":"多伦多/旧金山湾区", "C":"迈阿密/纽约",
    "D":"洛杉矶/达拉斯", "E":"达拉斯/休斯敦", "F":"纽约/新泽西",
    "G":"波士顿/亚特兰大", "H":"西雅图/温哥华", "I":"迈阿密/费城",
    "J":"布宜诺斯艾利斯/洛杉矶", "K":"休斯敦/堪萨斯城", "L":"多伦多/纽约/新泽西",
}

# Date assignment for R3
DATE_R3 = {
    "A":"6/24", "B":"6/24", "C":"6/24", "D":"6/25", "E":"6/25", "F":"6/25",
    "G":"6/26", "H":"6/26", "I":"6/26", "J":"6/27", "K":"6/27", "L":"6/27",
}

out_lines = []
out_lines.append("# -*- coding: utf-8 -*-")
out_lines.append("# 12组详细数据: 当前积分 + 已踢 + R3 未踢 (数据来源: 维基百科 2026 FIFA World Cup, 抓取 2026-06-19)")
out_lines.append("GROUPS = [")
for L in "ABCDEFGHIJKL":
    out_lines.append("  {")
    out_lines.append(f"    \"name\":\"{L}\", \"venue\":\"{VENUE[L]}\",")
    # team order from first played match
    teams_in = []
    for m in matches[L]["played"]:
        h = KEY.get(m["home"], m["home"])
        a = KEY.get(m["away"], m["away"])
        if h not in teams_in: teams_in.append(h)
        if a not in teams_in: teams_in.append(a)
    out_lines.append(f"    \"teams\":{teams_in!r},")
    out_lines.append("    \"standings\":[")
    for team, st in compute_standings(L):
        out_lines.append(f"      (\"{team}\",{st['P']},{st['W']},{st['D']},{st['L']},{st['GF']},{st['GA']},{st['Pts']},None),")
    out_lines.append("    ],")
    out_lines.append("    \"played\":[")
    for m in matches[L]["played"]:
        h = KEY.get(m["home"], m["home"])
        a = KEY.get(m["away"], m["away"])
        sh, sa = m["score"].split("-")
        goals_h = m["home_goals"].strip() or ""
        goals_a = m["away_goals"].strip() or ""
        # encode as tuple (h_key, h_score, a_key, a_score, scorers)
        out_lines.append(f"      (\"{h}\",{sh},\"{a}\",{sa},\"{goals_h} / {goals_a}\"),")
    out_lines.append("    ],")
    out_lines.append("    \"remaining\":[")
    for m in matches[L]["remaining"]:
        h = KEY.get(m["home"], m["home"])
        a = KEY.get(m["away"], m["away"])
        out_lines.append(f"      (\"{h}\",\"{a}\",\"{m['match']} {DATE_R3[L]}\"),")
    out_lines.append("    ],")
    out_lines.append("    \"predictions\":{},")
    out_lines.append("  },")

out_lines.append("]")
text = "\n".join(out_lines) + "\n"
with open(os.path.join(WIKI, "group_data.py"), "w", encoding="utf-8") as f:
    f.write(text)
print("[WROTE] group_data.py  size=%d" % len(text))
print(text[:1500])