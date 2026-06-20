# -*- coding: utf-8 -*-
# 2026世界杯48强评估数据
TEAMS = {
  # 第一档
  "Mexico":       {"zh":"墨西哥","group":"A","pot":1,"rank":14,"tier":"T1","power":74,"avg_age":28.2,"coach":"海因策(阿)","captain":"瓜尔达多","stars":["洛萨诺(前锋)","埃德松·阿尔瓦雷斯(中场)","奥乔亚(门将)"],"style":"主场作战+技术型","history":"3次8强(1970/1986已无)","key":"东道主首战气氛","weak":"锋线把握能力"},
  "South Africa": {"zh":"南非","group":"A","pot":4,"rank":60,"tier":"T4","power":52,"avg_age":27.5,"coach":"埃勒曼德","captain":"莫科纳","stars":["莫科纳(中场)","勒特罗特罗夫(前锋)"],"style":"防守反击","history":"2010东道主曾小组出线","key":"身体对抗","weak":"大赛经验不足"},
  "South Korea":  {"zh":"韩国","group":"A","pot":2,"rank":22,"tier":"T2","power":71,"avg_age":27.0,"coach":"洪明甫","captain":"孙兴慜","stars":["孙兴慜(前锋)","李刚仁(中场)","金玟哉(后卫)"],"style":"高位逼抢+快速反击","history":"2002四强","key":"孙兴慜状态","weak":"对抗欧洲球队"},
  "Czech":        {"zh":"捷克","group":"A","pot":3,"rank":44,"tier":"T3","power":63,"avg_age":27.8,"coach":"希尔绍夫斯基","captain":"达里达","stars":["希克(前锋)","曹法尔(后卫)","弗拉塞克(中场)"],"style":"传控+定位球","history":"曾获2004欧洲杯亚军","key":"希克回勇","weak":"缺少绝对核心"},

  "Canada":       {"zh":"加拿大","group":"B","pot":1,"rank":30,"tier":"T1","power":69,"avg_age":26.4,"coach":"马什","captain":"哈钦森","stars":["戴维(前锋)","拉林(中场)","阿迪尔伯特(后卫)"],"style":"身体+速度型","history":"1986/2022参赛","key":"戴维火力","weak":"大赛经验少"},
  "Bosnia":       {"zh":"波黑","group":"B","pot":4,"rank":64,"tier":"T4","power":55,"avg_age":27.6,"coach":"巴巴雷茨","captain":"哲科","stars":["哲科(前锋,39岁)","克鲁尼奇(中场)","科拉希纳茨(后卫)"],"style":"个人能力+定位球","history":"2014首次小组出线","key":"哲科经验","weak":"老化"},
  "Qatar":        {"zh":"卡塔尔","group":"B","pot":3,"rank":51,"tier":"T3","power":56,"avg_age":26.0,"coach":"洛佩兹(西)","captain":"海多斯","stars":["阿菲夫(前锋)","海多斯(中场)"],"style":"整体防守+反击","history":"2022东道主","key":"主场氛围减弱","weak":"对抗顶级队"},
  "Switzerland":  {"zh":"瑞士","group":"B","pot":2,"rank":17,"tier":"T2","power":75,"avg_age":27.5,"coach":"雅金","captain":"扎卡","stars":["扎卡(中场)","恩博洛(前锋)","阿坎吉(后卫)","索默(门将)"],"style":"整体+纪律性","history":"3届16强","key":"扎卡组织","weak":"缺少超级球星"},

  "Brazil":       {"zh":"巴西","group":"C","pot":1,"rank":5,"tier":"T1","power":92,"avg_age":27.0,"coach":"多里瓦尔","captain":"维尼修斯","stars":["维尼修斯(前锋)","罗德里戈(前锋)","库尼亚(前锋)","米利唐(后卫)","阿利森(门将)"],"style":"华丽进攻","history":"5次冠军(最近2002)","key":"锋线群","weak":"中场硬度"},
  "Morocco":      {"zh":"摩洛哥","group":"C","pot":2,"rank":11,"tier":"T2","power":80,"avg_age":27.0,"coach":"雷格拉吉","captain":"赛斯","stars":["阿什拉夫(后卫)","塞巴里(中场)","恩内斯里(前锋)","布努(门将)"],"style":"防守+反击","history":"2022四强","key":"门将+整体","weak":"锋线把握"},
  "Haiti":        {"zh":"海地","group":"C","pot":4,"rank":84,"tier":"T4","power":42,"avg_age":25.9,"coach":"扎卡尼安","captain":"杰罗姆","stars":["皮埃尔(中场)"],"style":"防守+速度","history":"1974后首次回归","key":"团结+冲击力","weak":"阵容深度"},
  "Scotland":     {"zh":"苏格兰","group":"C","pot":3,"rank":36,"tier":"T3","power":68,"avg_age":27.0,"coach":"克拉克","captain":"罗伯逊","stars":["罗伯逊(后卫)","麦克托米奈(中场)","麦金(中场)"],"style":"整体+对抗","history":"1998后首次回归","key":"团队精神","weak":"缺少明星前锋"},

  "USA":          {"zh":"美国","group":"D","pot":1,"rank":17,"tier":"T1","power":75,"avg_age":25.5,"coach":"波切蒂诺","captain":"普利西奇","stars":["普利西奇(前锋)","巴洛贡(前锋)","雷纳(中场)","亚当斯(中场)","罗宾逊(门将)"],"style":"身体+青春风暴","history":"多次16强","key":"主场+年轻","weak":"大赛经验"},
  "Paraguay":     {"zh":"巴拉圭","group":"D","pot":3,"rank":39,"tier":"T3","power":64,"avg_age":27.5,"coach":"阿尔法罗","captain":"阿尔米隆","stars":["阿尔米隆(前锋)","加马拉(中场)","阿尔德雷特(后卫)"],"style":"防守+反击","history":"2010八强","key":"整体防守","weak":"锋线乏力"},
  "Australia":    {"zh":"澳大利亚","group":"D","pot":3,"rank":26,"tier":"T3","power":64,"avg_age":26.5,"coach":"波波维奇","captain":"罗吉奇","stars":["苏塔尔(后卫)","莱基(前锋)","欧文(前锋)"],"style":"身体+冲击","history":"2006十六强","key":"定位球+身体","weak":"技术细腻度"},
  "Turkey":       {"zh":"土耳其","group":"D","pot":4,"rank":25,"tier":"T3","power":68,"avg_age":26.8,"coach":"蒙特拉","captain":"恰尔汗奥卢","stars":["恰尔汗奥卢(中场)","伊尔迪兹(前锋)","居莱尔(中场)","德米拉尔(后卫)"],"style":"技术+对抗","history":"2002/2008四强","key":"恰尔汗+伊尔迪兹","weak":"防线不稳"},

  "Germany":      {"zh":"德国","group":"E","pot":1,"rank":9,"tier":"T1","power":88,"avg_age":26.4,"coach":"纳格尔斯曼","captain":"京多安","stars":["穆西亚拉(中场)","哈弗茨(前锋)","维尔茨(中场)","吕迪格(后卫)","诺伊尔(门将)"],"style":"高位逼抢+整体","history":"4次冠军","key":"穆西亚拉+维尔茨","weak":"中锋缺乏"},
  "Curacao":      {"zh":"库拉索","group":"E","pot":4,"rank":82,"tier":"T4","power":35,"avg_age":27.0,"coach":"艾德沃卡特","captain":"巴克","stars":["巴克(中场)","马蒂纳(前锋)"],"style":"防守+反击","history":"首次参赛","key":"归化球员","weak":"实力差距"},
  "Ivory Coast":  {"zh":"科特迪瓦","group":"E","pot":3,"rank":42,"tier":"T3","power":67,"avg_age":26.0,"coach":"法耶","captain":"凯西","stars":["凯西(中场)","佩佩(前锋)","拜利(后卫)"],"style":"身体+个人","history":"2006曾参赛","key":"凯西中场","weak":"稳定性"},
  "Ecuador":      {"zh":"厄瓜多尔","group":"E","pot":2,"rank":23,"tier":"T2","power":68,"avg_age":26.0,"coach":"阿尔法罗","captain":"恩纳·瓦伦西亚","stars":["恩纳·瓦伦西亚(前锋)","普雷西亚多(中场)","埃斯皮诺萨(后卫)"],"style":"高原+速度","history":"2006十六强","key":"锋线核心","weak":"高原优势不再"},

  "Netherlands":  {"zh":"荷兰","group":"F","pot":1,"rank":7,"tier":"T1","power":86,"avg_age":27.0,"coach":"科曼","captain":"范戴克","stars":["范戴克(后卫)","德容(中场)","加克波(前锋)","邓弗里斯(后卫)","德佩(前锋)"],"style":"全攻全守","history":"3次亚军","key":"范戴克+德容","weak":"锋线老化"},
  "Japan":        {"zh":"日本","group":"F","pot":2,"rank":18,"tier":"T2","power":78,"avg_age":27.5,"coach":"森保一","captain":"远藤航","stars":["久保建英(中场)","三笘薰(前锋)","远藤航(中场)","富安健洋(后卫)"],"style":"技术+速度","history":"2002/2010/2018十六强","key":"旅欧球员群","weak":"身体对抗"},
  "Sweden":       {"zh":"瑞典","group":"F","pot":3,"rank":43,"tier":"T3","power":70,"avg_age":27.5,"coach":"托马森","captain":"埃克达尔","stars":["伊萨克(前锋)","哲凯赖什(前锋)","福斯贝里(中场)","林德洛夫(后卫)"],"style":"高大+定位球","history":"1958亚军/1994季军","key":"锋线双塔","weak":"中场创造"},
  "Tunisia":      {"zh":"突尼斯","group":"F","pot":3,"rank":40,"tier":"T3","power":60,"avg_age":27.0,"coach":"卡兹里","captain":"姆萨克尼","stars":["姆萨克尼(中场)","杰巴利(前锋)"],"style":"整体防守","history":"1978/1998/2002/2006","key":"防守组织","weak":"进攻乏力"},

  "Belgium":      {"zh":"比利时","group":"G","pot":1,"rank":8,"tier":"T1","power":83,"avg_age":28.5,"coach":"特德斯科","captain":"德布劳内","stars":["德布劳内(中场)","卢卡库(前锋)","库尔图瓦(门将)","阿扎尔(中场)","蒂勒曼斯(中场)"],"style":"反击+球星","history":"2018季军/2022小组出局","key":"德布劳内爆发","weak":"黄金一代末期"},
  "Egypt":        {"zh":"埃及","group":"G","pot":3,"rank":34,"tier":"T3","power":65,"avg_age":27.5,"coach":"胡斯因","captain":"萨拉赫","stars":["萨拉赫(前锋)","埃尔内尼(中场)","加布尔(后卫)"],"style":"防守+反击","history":"1934/1990","key":"萨拉赫一锤定音","weak":"整体深度"},
  "Iran":         {"zh":"伊朗","group":"G","pot":2,"rank":20,"tier":"T2","power":69,"avg_age":27.0,"coach":"加埃迪","captain":"阿兹蒙","stars":["阿兹蒙(前锋)","塔雷米(前锋)","贾汉巴赫什(中场)"],"style":"高位逼抢+身体","history":"连续多届参赛","key":"锋线双煞","weak":"大赛心理"},
  "New Zealand":  {"zh":"新西兰","group":"G","pot":4,"rank":86,"tier":"T4","power":45,"avg_age":27.0,"coach":"海耶斯","captain":"托马斯","stars":["伍德(前锋,28)","托马斯(中场)"],"style":"防守+定位球","history":"2010曾小组赛","key":"英联邦体系","weak":"对抗顶级强队"},

  "Spain":        {"zh":"西班牙","group":"H","pot":1,"rank":2,"tier":"T1","power":91,"avg_age":26.5,"coach":"德拉富恩特","captain":"莫拉塔","stars":["罗德里(中场)","佩德里(中场)","加维(中场)","尼科·威廉姆斯(前锋)","亚马尔(前锋,17)","乌奈·西蒙(门将)"],"style":"极致传控","history":"2010冠军","key":"中场厚度","weak":"中锋乏力"},
  "Cabo Verde":   {"zh":"佛得角","group":"H","pot":4,"rank":68,"tier":"T4","power":50,"avg_age":27.0,"coach":"佩德罗","captain":"丰特斯","stars":["罗德里格斯(中场)","丰特斯(后卫)"],"style":"整体防守+反击","history":"首次参赛","key":"归化球员","weak":"实力差距"},
  "Saudi Arabia": {"zh":"沙特阿拉伯","group":"H","pot":3,"rank":60,"tier":"T3","power":58,"avg_age":26.0,"coach":"勒纳尔(法)","captain":"法拉吉","stars":["萨利姆·多萨里(前锋)","布莱希(后卫)"],"style":"技术+速度","history":"1994十六强/2002胜多支强队","key":"主场氛围类似","weak":"整体实力"},
  "Uruguay":      {"zh":"乌拉圭","group":"H","pot":2,"rank":16,"tier":"T2","power":81,"avg_age":27.0,"coach":"比埃尔萨","captain":"戈丁","stars":["苏亚雷斯(前锋,39)","努涅斯(前锋)","巴尔韦德(中场)","阿劳霍(后卫)"],"style":"拼抢+进攻","history":"2次冠军(1930/1950)","key":"苏牙+努涅斯","weak":"苏牙老化"},

  "France":       {"zh":"法国","group":"I","pot":1,"rank":3,"tier":"T1","power":90,"avg_age":26.5,"coach":"德尚","captain":"姆巴佩","stars":["姆巴佩(前锋)","登贝莱(中场)","格列兹曼(中场)","楚阿梅尼(中场)","萨利巴(后卫)","迈尼昂(门将)"],"style":"反击+技术","history":"2018冠军/2022亚军","key":"姆巴佩冲击","weak":"锋线替补"},
  "Senegal":      {"zh":"塞内加尔","group":"I","pot":2,"rank":19,"tier":"T2","power":76,"avg_age":27.0,"coach":"西塞","captain":"库利巴利","stars":["库利巴利(后卫)","萨尔(中场)","马内(前锋)","门迪(门将)"],"style":"身体+速度","history":"2002八强/2022十六强","key":"团队精神","weak":"马内老化"},
  "Iraq":         {"zh":"伊拉克","group":"I","pot":4,"rank":58,"tier":"T4","power":48,"avg_age":26.0,"coach":"卡萨斯","captain":"侯赛因","stars":["侯赛因(前锋)","阿里(中场)"],"style":"防守+反击","history":"2007亚洲杯冠军","key":"主场球迷","weak":"绝对实力"},
  "Norway":       {"zh":"挪威","group":"I","pot":3,"rank":29,"tier":"T2","power":77,"avg_age":26.5,"coach":"索尔巴肯","captain":"厄斯蒂高","stars":["哈兰德(前锋)","厄德高(中场)","厄斯蒂高(后卫)","阿热(中场)"],"style":"反击+球星","history":"1998小组赛/2000后回归","key":"哈兰德+厄德高","weak":"大赛经验少"},

  "Argentina":    {"zh":"阿根廷","group":"J","pot":1,"rank":1,"tier":"T1","power":93,"avg_age":28.5,"coach":"斯卡洛尼","captain":"梅西","stars":["梅西(前锋)","阿尔瓦雷斯(前锋)","迪马利亚(中场)","德保罗(中场)","罗梅罗(后卫)","马丁内斯(门将)"],"style":"控制+反击","history":"3次冠军(最近2022)","key":"梅西最后一舞","weak":"后防轮换"},
  "Algeria":      {"zh":"阿尔及利亚","group":"J","pot":3,"rank":35,"tier":"T3","power":63,"avg_age":27.0,"coach":"贝勒米迪","captain":"马赫雷斯","stars":["马赫雷斯(前锋)","本纳赛尔(中场)","曼迪(后卫)"],"style":"整体+纪律","history":"2014十六强/2019非洲杯冠军","key":"马赫雷斯状态","weak":"深度有限"},
  "Austria":      {"zh":"奥地利","group":"J","pot":2,"rank":24,"tier":"T2","power":68,"avg_age":27.0,"coach":"朗尼克","captain":"阿拉巴","stars":["阿拉巴(后卫)","施拉格尔(中场)","阿瑙托维奇(前锋)"],"style":"高位逼抢+整体","history":"多次参赛","key":"整体性","weak":"缺少头牌"},
  "Jordan":       {"zh":"约旦","group":"J","pot":4,"rank":66,"tier":"T4","power":50,"avg_age":26.0,"coach":"阿姆马塔","captain":"阿卜杜勒","stars":["奥尔万(前锋)","阿卜杜勒(中场)"],"style":"防守+反击","history":"首次参赛","key":"首次大赛经验","weak":"实力差距"},

  "Portugal":     {"zh":"葡萄牙","group":"K","pot":1,"rank":5,"tier":"T1","power":88,"avg_age":27.5,"coach":"马丁内斯","captain":"C罗","stars":["C罗(前锋,41)","B费(中场)","B席(中场)","菲利克斯(前锋)","迪亚斯(后卫)","科斯塔(门将)"],"style":"反击+球星","history":"2016冠军","key":"C罗最后一战","weak":"C罗状态"},
  "Congo DR":     {"zh":"刚果(金)","group":"K","pot":4,"rank":56,"tier":"T4","power":52,"avg_age":26.5,"coach":"恩孔科","captain":"博苏","stars":["维萨(中场)","巴卡(前锋)"],"style":"身体+速度","history":"1974后回归","key":"反击速度","weak":"大赛经验"},
  "Uzbekistan":   {"zh":"乌兹别克斯坦","group":"K","pot":3,"rank":50,"tier":"T3","power":60,"avg_age":26.0,"coach":"卡西莫夫","captain":"绍伊穆罗多夫","stars":["马沙里波夫(中场)","法伊拉祖耶夫(前锋)"],"style":"整体防守","history":"首次参赛","key":"首次机会","weak":"绝对实力"},
  "Colombia":     {"zh":"哥伦比亚","group":"K","pot":2,"rank":13,"tier":"T2","power":78,"avg_age":27.5,"coach":"洛伦索","captain":"萨帕塔","stars":["路易斯·迪亚斯(前锋)","J·罗德里格斯(中场)","奥斯皮纳(门将)","米纳(后卫)"],"style":"技术+身体","history":"2014八强","key":"J罗+迪亚斯","weak":"后防老化"},

  "England":      {"zh":"英格兰","group":"L","pot":1,"rank":4,"tier":"T1","power":88,"avg_age":26.5,"coach":"图赫尔(德)","captain":"凯恩","stars":["凯恩(前锋)","贝林厄姆(中场)","萨卡(前锋)","赖斯(中场)","斯通斯(后卫)","拉姆斯代尔(门将)"],"style":"传控+反击","history":"1966冠军","key":"凯恩+贝林厄姆","weak":"中卫深度"},
  "Croatia":      {"zh":"克罗地亚","group":"L","pot":2,"rank":10,"tier":"T2","power":78,"avg_age":28.0,"coach":"达利奇","captain":"莫德里奇","stars":["莫德里奇(中场,40)","佩里西奇(中场)","科瓦西奇(中场)","格瓦迪奥尔(后卫)","利瓦科维奇(门将)"],"style":"中场控制","history":"2018亚军/2022季军","key":"魔笛最后一战","weak":"锋线换代"},
  "Ghana":        {"zh":"加纳","group":"L","pot":4,"rank":72,"tier":"T4","power":55,"avg_age":26.5,"coach":"奥托·阿多","captain":"安德烈·阿尤","stars":["库杜斯(中场)","阿尤兄弟(前锋)","萨利苏(后卫)","阿蒂·齐吉(门将)"],"style":"身体+速度","history":"2010八强/2022小组出局","key":"库杜斯+阿尤","weak":"大赛稳定性"},
  "Panama":       {"zh":"巴拿马","group":"L","pot":3,"rank":30,"tier":"T3","power":52,"avg_age":27.0,"coach":"洛萨诺","captain":"戈麦斯","stars":["戈麦斯(前锋)","戴维斯(中场)"],"style":"防守+反击","history":"2018首次参赛","key":"团结","weak":"实力差距"}
}
