# -*- coding: utf-8 -*-
# 12组详细数据: 当前积分 + 已踢 + 未踢场次预测
# 基于维基百科抓取 (2026-06-20 时点: 已踢完小组赛第1+2轮, 第3轮未踢)
GROUPS = [
  {
    "name":"A", "venue":"墨西哥城/瓜达拉哈拉",
    "teams":["Mexico","South Korea","Czech","South Africa"],
    "standings":[
      ("Mexico",2,2,0,0,3,0,6,"晋级"),
      ("South Korea",2,1,0,1,2,2,3,None),
      ("Czech",2,0,1,1,2,3,1,None),
      ("South Africa",2,0,1,1,1,3,1,None),
    ],
    "played":[
      ("Mexico",2,"South Africa",0,"基尼奥内斯 9', 希门尼斯 67'"),
      ("South Korea",2,"Czech",1,"黄仁范 67', 吴贤揆 80' / 克雷伊奇 59'"),
      ("Czech",1,"South Africa",1,"萨迪莱克 6' / 莫科纳 83'(点)"),
      ("Mexico",1,"South Korea",0,"罗莫 50'"),
    ],
    "remaining":[
      ("Czech","Mexico","赛事53 6/24"),
      ("South Africa","South Korea","赛事54 6/24"),
    ],
    "predictions":{
      "winner":"Mexico",
      "runner":"South Korea",
      "third":"Czech",
      "fourth":"South Africa",
    }
  },
  {
    "name":"B", "venue":"多伦多/旧金山湾区",
    "teams":["Canada","Switzerland","Bosnia","Qatar"],
    "standings":[
      ("Canada",2,1,1,0,7,1,4,"晋级"),
      ("Switzerland",2,1,1,0,5,2,4,None),
      ("Bosnia",2,0,1,1,2,5,1,None),
      ("Qatar",2,0,1,1,1,7,1,None),
    ],
    "played":[
      ("Canada",1,"Bosnia",1,"拉林 78' / 卢基奇 21'"),
      ("Qatar",1,"Switzerland",1,"穆海姆 90+4'(乌龙) / 恩博洛 17'(点)"),
      ("Switzerland",4,"Bosnia",1,"曼赞比 74',90' 巴尔加斯 84' 扎卡 90+7'(点) / 马赫米奇 90+3'"),
      ("Canada",6,"Qatar",0,"拉林 16' J·戴维 29',45+3',90+2' 萨利巴 64' 马奈 75'(乌龙)"),
    ],
    "remaining":[
      ("Switzerland","Canada","赛事51 6/24"),
      ("Bosnia","Qatar","赛事52 6/24"),
    ],
    "predictions":{
      "winner":"Canada",
      "runner":"Switzerland",
      "third":"Bosnia",
      "fourth":"Qatar",
    }
  },
  {
    "name":"C", "venue":"迈阿密/纽约",
    "teams":["Brazil","Morocco","Scotland","Haiti"],
    "standings":[
      ("Brazil",2,1,1,0,4,1,4,"晋级"),
      ("Morocco",2,1,1,0,2,1,4,None),
      ("Scotland",2,1,0,1,1,1,3,None),
      ("Haiti",2,0,0,2,0,4,0,None),
    ],
    "played":[
      ("Brazil",1,"Morocco",1,"维尼修斯 32' / 塞巴里 21'"),
      ("Haiti",0,"Scotland",1,"/ 麦金 28'"),
      ("Scotland",0,"Morocco",1,"/ 塞巴里 2'"),
      ("Brazil",3,"Haiti",0,"库尼亚 23',36' 维尼修斯 45+3'"),
    ],
    "remaining":[
      ("Scotland","Brazil","赛事49 6/24"),
      ("Morocco","Haiti","赛事50 6/24"),
    ],
    "predictions":{
      "winner":"Brazil",
      "runner":"Morocco",
      "third":"Scotland",
      "fourth":"Haiti",
    }
  },
  {
    "name":"D", "venue":"洛杉矶/达拉斯",
    "teams":["USA","Paraguay","Australia","Turkey"],
    "standings":[
      ("USA",2,2,0,0,6,1,6,"晋级"),
      ("Paraguay",2,1,0,1,1,4,3,None),
      ("Australia",2,1,0,1,2,2,3,None),
      ("Turkey",2,0,0,2,0,3,0,None),
    ],
    "played":[
      ("USA",4,"Paraguay",1,"博瓦迪利亚 7'(乌龙) 巴洛贡 31',45+5' 雷纳 90+8' / 毛里西奥 73'"),
      ("Australia",2,"Turkey",0,"伊兰昆达 27' 梅特卡夫 75'"),
      ("USA",2,"Australia",0,"伯吉斯 11'(乌龙) 弗里曼 43'"),
      ("Turkey",0,"Paraguay",1,"/ 馬迪亞斯·加拉扎 2'"),
    ],
    "remaining":[
      ("Turkey","USA","赛事59 6/25"),
      ("Paraguay","Australia","赛事60 6/25"),
    ],
    "predictions":{
      "winner":"USA",
      "runner":"Paraguay",
      "third":"Australia",
      "fourth":"Turkey",
    }
  },
  {
    "name":"E", "venue":"达拉斯/休斯敦",
    "teams":["Germany","Ivory Coast","Ecuador","Curacao"],
    "standings":[
      ("Germany",1,1,0,0,7,1,3,"晋级(少赛1)"),
      ("Ivory Coast",1,1,0,0,1,0,3,None),
      ("Ecuador",0,0,0,0,0,0,0,None),
      ("Curacao",0,0,0,0,0,0,0,None),
    ],
    "played":[
      ("Germany",7,"Curacao",1,"恩梅查 6' 施洛特贝克 38' 哈弗茨 45+5'(点),88' 穆西亚拉 47' 布朗 68' 温达夫 78' / 科梅嫩西亚 21'"),
      ("Ivory Coast",1,"Ecuador",0,"迪亚洛 90'"),
    ],
    "remaining":[
      ("Germany","Ivory Coast","赛事33 6/24"),
      ("Ecuador","Curacao","赛事34 6/24"),
      ("Curacao","Ivory Coast","赛事55 6/25"),
      ("Ecuador","Germany","赛事56 6/25"),
    ],
    "predictions":{
      "winner":"Germany",
      "runner":"Ivory Coast",
      "third":"Ecuador",
      "fourth":"Curacao",
    }
  },
  {
    "name":"F", "venue":"纽约/新泽西",
    "teams":["Netherlands","Japan","Sweden","Tunisia"],
    "standings":[
      ("Sweden",1,1,0,0,5,1,3,"晋级(少赛1)"),
      ("Netherlands",1,0,1,0,2,2,1,None),
      ("Japan",1,0,1,0,2,2,1,None),
      ("Tunisia",1,0,0,1,1,5,0,None),
    ],
    "played":[
      ("Netherlands",2,"Japan",2,"范戴克 51' 萨默维尔 64' / 中村敬斗 57' 鎌田大地 89'"),
      ("Sweden",5,"Tunisia",1,"阿亚里 7',90+6' 伊萨克 30' 哲凯赖什 59' 斯万贝里 84' / 雷基克 43'"),
    ],
    "remaining":[
      ("Netherlands","Sweden","赛事35 6/24"),
      ("Tunisia","Japan","赛事36 6/24"),
      ("Japan","Sweden","赛事57 6/25"),
      ("Tunisia","Netherlands","赛事58 6/25"),
    ],
    "predictions":{
      "winner":"Netherlands",
      "runner":"Sweden",
      "third":"Japan",
      "fourth":"Tunisia",
    }
  },
  {
    "name":"G", "venue":"亚特兰大/波士顿",
    "teams":["Belgium","Iran","Egypt","New Zealand"],
    "standings":[
      ("Iran",1,0,1,0,2,2,1,None),
      ("New Zealand",1,0,1,0,2,2,1,None),
      ("Belgium",1,0,1,0,1,1,1,None),
      ("Egypt",1,0,1,0,1,1,1,None),
    ],
    "played":[
      ("Belgium",1,"Egypt",1,"汉尼 66'(乌龙) / 阿舒尔 20'"),
      ("Iran",2,"New Zealand",2,"雷扎伊安 32' 莫赫比 64' / 贾斯特 7',54'"),
    ],
    "remaining":[
      ("Belgium","Iran","赛事39 6/24"),
      ("New Zealand","Egypt","赛事40 6/24"),
      ("Egypt","Iran","赛事63 6/25"),
      ("New Zealand","Belgium","赛事64 6/25"),
    ],
    "predictions":{
      "winner":"Belgium",
      "runner":"Iran",
      "third":"Egypt",
      "fourth":"New Zealand",
    }
  },
  {
    "name":"H", "venue":"西雅图/温哥华",
    "teams":["Spain","Uruguay","Saudi Arabia","Cabo Verde"],
    "standings":[
      ("Uruguay",1,0,1,0,1,1,1,None),
      ("Spain",1,0,1,0,0,0,1,None),
      ("Saudi Arabia",1,0,1,0,1,1,1,None),
      ("Cabo Verde",1,0,1,0,0,0,1,None),
    ],
    "played":[
      ("Spain",0,"Cabo Verde",0,"/"),
      ("Saudi Arabia",1,"Uruguay",1,"阿姆里 41' / M·阿劳霍 80'"),
    ],
    "remaining":[
      ("Spain","Saudi Arabia","赛事38 6/24"),
      ("Uruguay","Cabo Verde","赛事37 6/24"),
      ("Cabo Verde","Saudi Arabia","赛事65 6/25"),
      ("Uruguay","Spain","赛事66 6/25"),
    ],
    "predictions":{
      "winner":"Spain",
      "runner":"Uruguay",
      "third":"Saudi Arabia",
      "fourth":"Cabo Verde",
    }
  },
  {
    "name":"I", "venue":"迈阿密/费城",
    "teams":["France","Norway","Senegal","Iraq"],
    "standings":[
      ("Norway",1,1,0,0,4,1,3,"晋级(少赛1)"),
      ("France",1,1,0,0,3,1,3,None),
      ("Senegal",1,0,0,1,1,4,0,None),
      ("Iraq",1,0,0,1,1,4,0,None),
    ],
    "played":[
      ("France",3,"Senegal",1,"姆巴佩 66',90+6' 巴尔科拉 82' / 姆巴耶 90+5'"),
      ("Iraq",1,"Norway",4,"侯赛因 39' / 哈兰德 29',43' 厄斯蒂高 76' 侯赛因 90+6'(乌龙)"),
    ],
    "remaining":[
      ("France","Iraq","赛事42 6/24"),
      ("Norway","Senegal","赛事41 6/24"),
      ("Norway","France","赛事61 6/25"),
      ("Senegal","Iraq","赛事62 6/25"),
    ],
    "predictions":{
      "winner":"France",
      "runner":"Norway",
      "third":"Senegal",
      "fourth":"Iraq",
    }
  },
  {
    "name":"J", "venue":"布宜诺斯艾利斯/洛杉矶",
    "teams":["Argentina","Austria","Algeria","Jordan"],
    "standings":[
      ("Argentina",1,1,0,0,3,0,3,"晋级(少赛1)"),
      ("Austria",1,1,0,0,3,1,3,None),
      ("Algeria",1,0,0,1,0,3,0,None),
      ("Jordan",1,0,0,1,1,3,0,None),
    ],
    "played":[
      ("Argentina",3,"Algeria",0,"梅西 17',60',76'"),
      ("Austria",3,"Jordan",1,"施密德 21' 阿拉伯 76'(乌龙) 阿瑙托维奇 90+12'(点) / 奥尔万 50'"),
    ],
    "remaining":[
      ("Argentina","Austria","赛事43 6/24"),
      ("Jordan","Algeria","赛事44 6/24"),
      ("Algeria","Austria","赛事69 6/25"),
      ("Jordan","Argentina","赛事70 6/25"),
    ],
    "predictions":{
      "winner":"Argentina",
      "runner":"Austria",
      "third":"Algeria",
      "fourth":"Jordan",
    }
  },
  {
    "name":"K", "venue":"休斯敦/堪萨斯城",
    "teams":["Portugal","Colombia","Congo DR","Uzbekistan"],
    "standings":[
      ("Colombia",1,1,0,0,3,1,3,"晋级(少赛1)"),
      ("Portugal",1,0,1,0,1,1,1,None),
      ("Congo DR",1,0,1,0,1,1,1,None),
      ("Uzbekistan",1,0,0,1,1,3,0,None),
    ],
    "played":[
      ("Portugal",1,"Congo DR",1,"J·内维斯 6' / 维萨 45+5'"),
      ("Uzbekistan",1,"Colombia",3,"法伊拉祖耶夫 60' / 穆尼奥斯 41' 迪亚斯 65' 坎帕斯 90+9'"),
    ],
    "remaining":[
      ("Portugal","Uzbekistan","赛事47 6/24"),
      ("Colombia","Congo DR","赛事48 6/24"),
      ("Colombia","Portugal","赛事71 6/25"),
      ("Congo DR","Uzbekistan","赛事72 6/25"),
    ],
    "predictions":{
      "winner":"Portugal",
      "runner":"Colombia",
      "third":"Congo DR",
      "fourth":"Uzbekistan",
    }
  },
  {
    "name":"L", "venue":"多伦多/纽约/新泽西",
    "teams":["England","Croatia","Ghana","Panama"],
    "standings":[
      ("England",1,1,0,0,4,2,3,"晋级(少赛1)"),
      ("Ghana",1,1,0,0,1,0,3,None),
      ("Croatia",1,0,0,1,2,4,0,None),
      ("Panama",1,0,0,1,0,1,0,None),
    ],
    "played":[
      ("England",4,"Croatia",2,"凯恩 12'(点),42' 贝林厄姆 47' 拉什福德 85' / 巴图里纳 36' 穆萨 45+5'"),
      ("Ghana",1,"Panama",0,"伊伦基 90+5'"),
    ],
    "remaining":[
      ("England","Ghana","赛事45 6/24"),
      ("Panama","Croatia","赛事46 6/24"),
      ("Panama","England","赛事67 6/25"),
      ("Croatia","Ghana","赛事68 6/25"),
    ],
    "predictions":{
      "winner":"England",
      "runner":"Croatia",
      "third":"Ghana",
      "fourth":"Panama",
    }
  }
]
