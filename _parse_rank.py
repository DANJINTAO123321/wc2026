# -*- coding: utf-8 -*-
import os, sys, re, json
sys.stdout.reconfigure(encoding="utf-8")
from bs4 import BeautifulSoup

WIKI = r"C:\Users\Administrator\Documents\世界杯"
html = open(os.path.join(WIKI, "_wiki_FIFA_Men%27s_World_Ranking.html"), encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")
t = soup.find_all("table", class_="wikitable")[0]
rankings = {}
for tr in t.find_all("tr"):
    cells = [c.get_text(" ", strip=True) for c in tr.find_all(["th","td"])]
    if len(cells) >= 4 and cells[0].isdigit():
        rankings[cells[2]] = {"rank": int(cells[0]), "points": float(cells[3])}
print("Got %d team rankings" % len(rankings))
for k, v in sorted(rankings.items(), key=lambda x: x[1]["rank"])[:20]:
    print("  %2d  %-25s  %.2f" % (v["rank"], k, v["points"]))
# Print rest
for k, v in sorted(rankings.items(), key=lambda x: x[1]["rank"])[20:]:
    print("  %2d  %-25s  %.2f" % (v["rank"], k, v["points"]))
with open(os.path.join(WIKI, "_fifa_rank.json"), "w", encoding="utf-8") as f:
    json.dump(rankings, f, ensure_ascii=False, indent=2)