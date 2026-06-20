# -*- coding: utf-8 -*-
# 12组详细数据: 维基百科 2026 FIFA World Cup 抓取 (2026-06-20)
#   - played: R1+R2 真实比分+进球者
#   - remaining: R3 待踢 (M33-M72, 6/24-6/27)
#   - predictions: ELO 模型 R3 推算 + 最终排名 (winner/runner/third/fourth)
GROUPS = [
  {
    "name":"A", "venue":"墨西哥城/瓜达拉哈拉",
    "teams":['Mexico', 'South Korea', 'Czech', 'South Africa'],
    "standings":[
      ("Mexico",3,3,0,0,4,0,9,None),
      ("South Korea",3,2,0,1,3,2,6,None),
      ("Czech",3,0,1,2,2,4,1,None),
      ("South Africa",3,0,1,2,1,4,1,None),
    ],
    "played":[
      ("Mexico",2,"South Africa",0,"Quiñones 9' Jiménez 67' / "),
      ("South Korea",2,"Czech",1,"Hwang In-beom 67' Oh Hyeon-gyu 80' / Krejčí 59'"),
      ("Czech",1,"South Africa",1,"Sadílek 6' / Mokoena 83' ( pen. )"),
      ("Mexico",1,"South Korea",0,"Romo 50' / "),
    ],
    "remaining":[
      ("Czech","Mexico","Match 53 6/24"),
      ("South Africa","South Korea","Match 54 6/24"),
    ],
    "predictions":{
      "winner":"Mexico",
      "runner":"South Korea",
      "third":"Czech",
      "fourth":"South Africa",
      "r3_pred":"South Africa 0-1 Mexico, South Korea 1-0 Czech"
    },
  },
  {
    "name":"B", "venue":"多伦多/旧金山湾区",
    "teams":['Canada', 'Bosnia', 'Qatar', 'Switzerland'],
    "standings":[
      ("Switzerland",3,2,1,0,6,2,7,None),
      ("Canada",3,1,1,1,7,2,4,None),
      ("Qatar",3,1,1,1,2,7,4,None),
      ("Bosnia",3,0,1,2,2,6,1,None),
    ],
    "played":[
      ("Canada",1,"Bosnia",1,"Larin 78' / Lukić 21'"),
      ("Qatar",1,"Switzerland",1,"Muheim 90+4' ( o.g. ) / Embolo 17' ( pen. )"),
      ("Switzerland",4,"Bosnia",1,"Manzambi 74' , 90' Vargas 84' Xhaka 90+7' ( pen. ) / Mahmić 90+3'"),
      ("Canada",6,"Qatar",0,"Larin 16' J. David 29' , 45+3' , 90+2' Saliba 64' Manai 75' ( o.g. ) / "),
    ],
    "remaining":[
      ("Switzerland","Canada","Match 51 6/24"),
      ("Bosnia","Qatar","Match 52 6/24"),
    ],
    "predictions":{
      "winner":"Switzerland",
      "runner":"Canada",
      "third":"Qatar",
      "fourth":"Bosnia",
      "r3_pred":"Switzerland 1-0 Canada, Bosnia 0-1 Qatar"
    },
  },
  {
    "name":"C", "venue":"迈阿密/纽约",
    "teams":['Brazil', 'Morocco', 'Scotland', 'Haiti'],
    "standings":[
      ("Brazil",3,2,1,0,5,1,7,None),
      ("Morocco",3,2,1,0,3,1,7,None),
      ("Scotland",3,1,0,2,1,2,3,None),
      ("Haiti",3,0,0,3,0,5,0,None),
    ],
    "played":[
      ("Brazil",1,"Morocco",1,"Vinícius 32' / Saibari 21'"),
      ("Haiti",0,"Scotland",1," / McGinn 28'"),
      ("Scotland",0,"Morocco",1," / Saibari 2'"),
      ("Brazil",3,"Haiti",0,"Cunha 23' , 36' Vinícius 45+3' / "),
    ],
    "remaining":[
      ("Scotland","Brazil","Match 49 6/24"),
      ("Morocco","Haiti","Match 50 6/24"),
    ],
    "predictions":{
      "winner":"Brazil",
      "runner":"Morocco",
      "third":"Scotland",
      "fourth":"Haiti",
      "r3_pred":"Haiti 0-1 Brazil, Morocco 1-0 Scotland"
    },
  },
  {
    "name":"D", "venue":"洛杉矶/达拉斯",
    "teams":['USA', 'Paraguay', 'Australia', 'Turkey'],
    "standings":[
      ("USA",3,3,0,0,7,1,9,None),
      ("Paraguay",3,2,0,1,3,4,6,None),
      ("Australia",3,1,0,2,2,3,3,None),
      ("Turkey",3,0,0,3,0,4,0,None),
    ],
    "played":[
      ("USA",4,"Paraguay",1,"Bobadilla 7' ( o.g. ) Balogun 31' , 45+5' Reyna 90+8' / Maurício 73'"),
      ("Australia",2,"Turkey",0,"Irankunda 27' Metcalfe 75' / "),
      ("USA",2,"Australia",0,"Burgess 11' ( o.g. ) Freeman 43' / "),
      ("Turkey",0,"Paraguay",1," / Galarza 2'"),
    ],
    "remaining":[
      ("Turkey","USA","Match 59 6/25"),
      ("Paraguay","Australia","Match 60 6/25"),
    ],
    "predictions":{
      "winner":"USA",
      "runner":"Paraguay",
      "third":"Australia",
      "fourth":"Turkey",
      "r3_pred":"Turkey 0-1 USA, Paraguay 1-0 Australia"
    },
  },
  {
    "name":"E", "venue":"达拉斯/休斯敦",
    "teams":['Germany', 'Curacao', 'Ivory Coast', 'Ecuador'],
    "standings":[
      ("Germany",2,2,0,0,8,1,6,None),
      ("Ivory Coast",2,2,0,0,2,0,6,None),
      ("Ecuador",2,0,0,2,0,2,0,None),
      ("Curacao",2,0,0,2,1,8,0,None),
    ],
    "played":[
      ("Germany",7,"Curacao",1,"Nmecha 6' Schlotterbeck 38' Havertz 45+5' ( pen. ) , 88' Musiala 47' Brown 68' Undav 78' / Comenencia 21'"),
      ("Ivory Coast",1,"Ecuador",0,"Diallo 90' / "),
    ],
    "remaining":[
      ("Germany","Ivory Coast","Match 33 6/25"),
      ("Ecuador","Curacao","Match 34 6/25"),
      ("Curacao","Ivory Coast","Match 55 6/25"),
      ("Ecuador","Germany","Match 56 6/25"),
    ],
    "predictions":{
      "winner":"Germany",
      "runner":"Ivory Coast",
      "third":"Ecuador",
      "fourth":"Curacao",
      "r3_pred":"Ecuador 0-1 Germany, Curacao 0-1 Ivory Coast"
    },
  },
  {
    "name":"F", "venue":"纽约/新泽西",
    "teams":['Netherlands', 'Japan', 'Sweden', 'Tunisia'],
    "standings":[
      ("Netherlands",2,1,1,0,3,2,4,None),
      ("Japan",2,1,1,0,3,2,4,None),
      ("Sweden",2,1,0,1,5,2,3,None),
      ("Tunisia",2,0,0,2,1,6,0,None),
    ],
    "played":[
      ("Netherlands",2,"Japan",2,"Van Dijk 50' Summerville 64' / Nakamura 57' Kamada 88'"),
      ("Sweden",5,"Tunisia",1,"Ayari 7' , 90+6' Isak 30' Gyökeres 59' Svanberg 84' / Rekik 43'"),
    ],
    "remaining":[
      ("Netherlands","Sweden","Match 35 6/25"),
      ("Tunisia","Japan","Match 36 6/25"),
      ("Japan","Sweden","Match 57 6/25"),
      ("Tunisia","Netherlands","Match 58 6/25"),
    ],
    "predictions":{
      "winner":"Netherlands",
      "runner":"Japan",
      "third":"Sweden",
      "fourth":"Tunisia",
      "r3_pred":"Tunisia 0-1 Netherlands, Japan 1-0 Sweden"
    },
  },
  {
    "name":"G", "venue":"波士顿/亚特兰大",
    "teams":['Belgium', 'Egypt', 'Iran', 'New Zealand'],
    "standings":[
      ("Belgium",2,1,1,0,2,1,4,None),
      ("Egypt",2,1,1,0,2,1,4,None),
      ("Iran",2,0,1,1,2,3,1,None),
      ("New Zealand",2,0,1,1,2,3,1,None),
    ],
    "played":[
      ("Belgium",1,"Egypt",1,"Hany 66' ( o.g. ) / Ashour 19'"),
      ("Iran",2,"New Zealand",2,"Rezaeian 32' Mohebi 64' / Just 7' , 54'"),
    ],
    "remaining":[
      ("Belgium","Iran","Match 39 6/26"),
      ("New Zealand","Egypt","Match 40 6/26"),
      ("Egypt","Iran","Match 63 6/26"),
      ("New Zealand","Belgium","Match 64 6/26"),
    ],
    "predictions":{
      "winner":"Belgium",
      "runner":"Egypt",
      "third":"Iran",
      "fourth":"New Zealand",
      "r3_pred":"New Zealand 0-1 Belgium, Egypt 1-0 Iran"
    },
  },
  {
    "name":"H", "venue":"西雅图/温哥华",
    "teams":['Spain', 'Uruguay', 'Saudi Arabia', 'Cabo Verde'],
    "standings":[
      ("Uruguay",2,1,1,0,2,1,4,None),
      ("Spain",2,1,1,0,1,0,4,None),
      ("Saudi Arabia",2,0,1,1,1,2,1,None),
      ("Cabo Verde",2,0,1,1,0,1,1,None),
    ],
    "played":[
      ("Spain",0,"Cabo Verde",0," / "),
      ("Saudi Arabia",1,"Uruguay",1,"Al-Amri 41' / M. Araújo 80'"),
    ],
    "remaining":[
      ("Spain","Saudi Arabia","Match 38 6/26"),
      ("Uruguay","Cabo Verde","Match 37 6/26"),
      ("Cabo Verde","Saudi Arabia","Match 65 6/26"),
      ("Uruguay","Spain","Match 66 6/26"),
    ],
    "predictions":{
      "winner":"Uruguay",
      "runner":"Spain",
      "third":"Saudi Arabia",
      "fourth":"Cabo Verde",
      "r3_pred":"Cabo Verde 0-1 Spain, Uruguay 1-0 Saudi Arabia"
    },
  },
  {
    "name":"I", "venue":"迈阿密/费城",
    "teams":['France', 'Norway', 'Senegal', 'Iraq'],
    "standings":[
      ("France",2,2,0,0,4,1,6,None),
      ("Norway",2,1,0,1,4,2,3,None),
      ("Senegal",2,1,0,1,2,3,3,None),
      ("Iraq",2,0,0,2,1,5,0,None),
    ],
    "played":[
      ("France",3,"Senegal",1,"Mbappé 66' , 90+6' Barcola 82' / Mbaye 90+5'"),
      ("Iraq",1,"Norway",4,"Hussein 39' / Haaland 29' , 43' Østigård 76' Hussein 90+6' ( o.g. )"),
    ],
    "remaining":[
      ("France","Iraq","Match 42 6/26"),
      ("Norway","Senegal","Match 41 6/26"),
      ("Norway","France","Match 61 6/26"),
      ("Senegal","Iraq","Match 62 6/26"),
    ],
    "predictions":{
      "winner":"France",
      "runner":"Norway",
      "third":"Senegal",
      "fourth":"Iraq",
      "r3_pred":"Iraq 0-1 France, Norway 0-1 Senegal"
    },
  },
  {
    "name":"J", "venue":"布宜诺斯艾利斯/洛杉矶",
    "teams":['Argentina', 'Austria', 'Algeria', 'Jordan'],
    "standings":[
      ("Argentina",2,2,0,0,4,0,6,None),
      ("Austria",2,2,0,0,4,1,6,None),
      ("Jordan",2,0,0,2,1,4,0,None),
      ("Algeria",2,0,0,2,0,4,0,None),
    ],
    "played":[
      ("Argentina",3,"Algeria",0,"Messi 17' , 60' , 76' / "),
      ("Austria",3,"Jordan",1,"Schmid 20' Al-Arab 76' ( o.g. ) Arnautović 90+12' ( pen. ) / Olwan 50'"),
    ],
    "remaining":[
      ("Argentina","Austria","Match 43 6/27"),
      ("Jordan","Algeria","Match 44 6/27"),
      ("Algeria","Austria","Match 69 6/27"),
      ("Jordan","Argentina","Match 70 6/27"),
    ],
    "predictions":{
      "winner":"Argentina",
      "runner":"Austria",
      "third":"Jordan",
      "fourth":"Algeria",
      "r3_pred":"Jordan 0-1 Argentina, Austria 1-0 Algeria"
    },
  },
  {
    "name":"K", "venue":"休斯敦/堮萨斯城",
    "teams":['Portugal', 'Colombia', 'Congo DR', 'Uzbekistan'],
    "standings":[
      ("Colombia",2,2,0,0,4,1,6,None),
      ("Portugal",2,1,1,0,2,1,4,None),
      ("Congo DR",2,0,1,1,1,2,1,None),
      ("Uzbekistan",2,0,0,2,1,4,0,None),
    ],
    "played":[
      ("Portugal",1,"Congo DR",1,"J. Neves 6' / Wissa 45+5'"),
      ("Uzbekistan",1,"Colombia",3,"Fayzullaev 60' / Muñoz 40' Díaz 65' Campaz 90+9'"),
    ],
    "remaining":[
      ("Portugal","Uzbekistan","Match 47 6/27"),
      ("Colombia","Congo DR","Match 48 6/27"),
      ("Colombia","Portugal","Match 71 6/27"),
      ("Congo DR","Uzbekistan","Match 72 6/27"),
    ],
    "predictions":{
      "winner":"Colombia",
      "runner":"Portugal",
      "third":"Congo DR",
      "fourth":"Uzbekistan",
      "r3_pred":"Uzbekistan 0-1 Portugal, Colombia 1-0 Congo DR"
    },
  },
  {
    "name":"L", "venue":"多伦多/纽约/新泽西",
    "teams":['England', 'Croatia', 'Ghana', 'Panama'],
    "standings":[
      ("England",2,2,0,0,5,2,6,None),
      ("Ghana",2,1,0,1,1,1,3,None),
      ("Croatia",2,1,0,1,3,4,3,None),
      ("Panama",2,0,0,2,0,2,0,None),
    ],
    "played":[
      ("England",4,"Croatia",2,"Kane 12' ( pen. ) , 42' Bellingham 47' Rashford 85' / Baturina 36' Musa 45+5'"),
      ("Ghana",1,"Panama",0,"Yirenkyi 90+5' / "),
    ],
    "remaining":[
      ("England","Ghana","Match 45 6/27"),
      ("Panama","Croatia","Match 46 6/27"),
      ("Panama","England","Match 67 6/27"),
      ("Croatia","Ghana","Match 68 6/27"),
    ],
    "predictions":{
      "winner":"England",
      "runner":"Ghana",
      "third":"Croatia",
      "fourth":"Panama",
      "r3_pred":"Panama 0-1 England, Croatia 1-0 Ghana"
    },
  },
]
