# -*- coding: utf-8 -*-
import os, sys, re, json
sys.stdout.reconfigure(encoding="utf-8")
from bs4 import BeautifulSoup

WIKI = r"C:\Users\Administrator\Documents\世界杯"

def parse_group(L):
    html = open(os.path.join(WIKI, "_wiki_Group_%s.html" % L), encoding="utf-8").read()
    soup = BeautifulSoup(html, "html.parser")
    mid = soup.find(id="Matches")
    out = {"played": [], "remaining": []}
    n = mid.find_next()
    sib = mid.find_next("h2")
    # Patterns
    SCORE_RE = re.compile(r"^\d+\s*[-–—]\s*\d+$")
    MATCH_RE = re.compile(r"^Match\s*\d+$")
    while n and n != sib:
        if n.name == "table":
            rows = n.find_all("tr")
            if len(rows) >= 2:
                c0 = [c.get_text(" ", strip=True).replace("\xa0"," ").replace("\u2212","-").replace("\u2013","-").replace("\u2014","-") for c in rows[0].find_all(["th","td"])]
                c1 = [c.get_text(" ", strip=True).replace("\xa0"," ").replace("\u2212","-").replace("\u2013","-").replace("\u2014","-") for c in rows[1].find_all(["th","td"])]
                if len(c0) >= 3 and SCORE_RE.match(c0[1]):
                    out["played"].append({
                        "home": c0[0],
                        "score": c0[1].replace(" ", ""),
                        "away": c0[2],
                        "home_goals": c1[0] if len(c1) > 0 else "",
                        "away_goals": c1[-1] if len(c1) > 2 else "",
                    })
                elif len(c0) >= 3 and MATCH_RE.match(c0[1]):
                    out["remaining"].append({"home": c0[0], "match": c0[1], "away": c0[2]})
        n = n.find_next()
    return out

all_data = {}
for L in "ABCDEFGHIJKL":
    g = parse_group(L)
    all_data[L] = g
    print("\n== Group %s == played=%d remaining=%d" % (L, len(g["played"]), len(g["remaining"])))
    for m in g["played"]:
        print("  %s  %s  %s  | H:[%s] | A:[%s]" % (m["home"][:18], m["score"], m["away"][:18], m["home_goals"][:35], m["away_goals"][:25]))
    for m in g["remaining"]:
        print("  [待踢] %s vs %s  (%s)" % (m["home"][:18], m["away"][:18], m["match"]))

with open(os.path.join(WIKI, "_all_matches.json"), "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)
print("\n[SAVED] _all_matches.json  total played=%d remaining=%d" % (sum(len(g["played"]) for g in all_data.values()), sum(len(g["remaining"]) for g in all_data.values())))