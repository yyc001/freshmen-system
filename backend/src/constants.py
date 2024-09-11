
def label2value(list, label):
    for x in list: 
        if x["label"] == label: 
            return x["value"]
    return False

def value2label(list, value):
    for x in list: 
        if x["value"] == value:
            return x["label"]
    return False

def list2map(list):
    return {x["label"]:x["value"] for x in list}

YN = [
    { "label": "否", "value": 0 },
    { "label": "是", "value": 1 },
]

GENDERS = [
    { "label": "男", "value": 1 },
    { "label": "女", "value": 2 },
    { "label": "不愿透露", "value": 3 },
]

CAMPUSES = [
    { "label": "中心校区", "value": 1 },
    { "label": "洪家楼校区", "value": 2 },
    { "label": "软件园校区", "value": 3 },
    { "label": "兴隆山校区", "value": 4 },
    { "label": "千佛山校区", "value": 5 },
    { "label": "趵突泉校区", "value": 6 },
    { "label": "青岛校区", "value": 7 },
    { "label": "威海校区", "value": 8
    }
]

MAJORS = [
    { "label": "数学", "value": 1 },
    { "label": "物理", "value": 2 },
    { "label": "化学", "value": 3 },
    { "label": "生物", "value": 4 },
    { "label": "计算机", "value": 5 },
]

GK_LANGUAGES = [
    { "label": "英语", "value": 1 },
    { "label": "日语", "value": 2 },
    { "label": "德语", "value": 3 },
    { "label": "法语", "value": 4 },
    { "label": "俄语", "value": 5 },
    { "label": "西班牙语", "value": 6 },
]

EXEMPTIONS = [
    { "label": "无免试资格", "value": 0 },
    { "label": "自动获取面试资格，但参加笔试", "value": 1 },
    { "label": "自动获取面试资格，不参加笔试", "value": 2 },
    { "label": "报名后直接进入学堂相关学科", "value": 3 },
]

PROVINCES = [
    { "label": "北京市", "value": 11 },
    { "label": "天津市", "value": 12 },
    { "label": "河北省", "value": 13 },
    { "label": "山西省", "value": 14 },
    { "label": "内蒙古自治区", "value": 15 },
    { "label": "辽宁省", "value": 21 },
    { "label": "吉林省", "value": 22 },
    { "label": "黑龙江省", "value": 23 },
    { "label": "上海市", "value": 31 },
    { "label": "江苏省", "value": 32 },
    { "label": "浙江省", "value": 33 },
    { "label": "安徽省", "value": 34 },
    { "label": "福建省", "value": 35 },
    { "label": "江西省", "value": 36 },
    { "label": "山东省", "value": 37 },
    { "label": "河南省", "value": 41 },
    { "label": "湖北省", "value": 42 },
    { "label": "湖南省", "value": 43 },
    { "label": "广东省", "value": 44 },
    { "label": "广西壮族自治区", "value": 45 },
    { "label": "海南省", "value": 46 },
    { "label": "重庆市", "value": 50 },
    { "label": "四川省", "value": 51 },
    { "label": "贵州省", "value": 52 },
    { "label": "云南省", "value": 53 },
    { "label": "西藏自治区", "value": 54 },
    { "label": "陕西省", "value": 61 },
    { "label": "甘肃省", "value": 62 },
    { "label": "青海省", "value": 63 },
    { "label": "宁夏回族自治区", "value": 64 },
    { "label": "新疆维吾尔自治区", "value": 65 }
]

AWARDS = [
    { "label": "没有列表中的竞赛奖项", "value": 0 },
    { "label": "国际数学奥林匹克竞赛国家集训队", "value": 10 },
    { "label": "全国中学生数学奥林匹克竞赛（决赛）【一等奖】", "value": 11 },
    { "label": "全国中学生数学奥林匹克竞赛（决赛）【二等奖】", "value": 12 },
    { "label": "全国中学生数学奥林匹克竞赛（决赛）【三等奖】", "value": 13 },
    { "label": "全国中学生数学奥林匹克竞赛（预赛）【一等奖】", "value": 14 },
    { "label": "全国中学生数学奥林匹克竞赛（预赛）【二等奖】", "value": 15 },
    { "label": "全国中学生数学奥林匹克竞赛（预赛）【三等奖】", "value": 16 },
    { "label": "国际物理奥林匹克竞赛国家集训队", "value": 20 },
    { "label": "全国中学生物理竞赛（决赛）【一等奖】", "value": 21 },
    { "label": "全国中学生物理竞赛（决赛）【二等奖】", "value": 22 },
    { "label": "全国中学生物理竞赛（决赛）【三等奖】", "value": 23 },
    { "label": "全国中学生物理竞赛（省级赛区）【一等奖】", "value": 24 },
    { "label": "全国中学生物理竞赛（省级赛区）【二等奖】", "value": 25 },
    { "label": "全国中学生物理竞赛（省级赛区）【三等奖】", "value": 26 },
    { "label": "国际化学奥林匹克竞赛国家集训队", "value": 30 },
    { "label": "中国化学奥林匹克（决赛）【一等奖】", "value": 31 },
    { "label": "中国化学奥林匹克（决赛）【二等奖】", "value": 32 },
    { "label": "中国化学奥林匹克（决赛）【三等奖】", "value": 33 },
    { "label": "中国化学奥林匹克（初赛）【一等奖】", "value": 34 },
    { "label": "中国化学奥林匹克（初赛）【二等奖】", "value": 35 },
    { "label": "中国化学奥林匹克（初赛）【三等奖】", "value": 36 },
    { "label": "国际生物学奥林匹克竞赛国家集训队", "value": 40 },
    { "label": "全国中学生生物学竞赛【一等奖】", "value": 41 },
    { "label": "全国中学生生物学竞赛【二等奖】", "value": 42 },
    { "label": "全国中学生生物学竞赛【三等奖】", "value": 43 },
    { "label": "全国中学生生物学联赛【一等奖】", "value": 44 },
    { "label": "全国中学生生物学联赛【二等奖】", "value": 45 },
    { "label": "全国中学生生物学联赛【三等奖】", "value": 46 },
    { "label": "国际信息学奥林匹克竞赛国家集训队", "value": 50 },
    { "label": "全国青少年信息学奥林匹克竞赛（决赛）【金牌】", "value": 51 },
    { "label": "全国青少年信息学奥林匹克竞赛（决赛）【银牌】", "value": 52 },
    { "label": "全国青少年信息学奥林匹克竞赛（决赛）【铜牌】", "value": 53 },
    { "label": "全国青少年信息学奥林匹克联赛（复赛）【一等奖】", "value": 54 },
    { "label": "全国青少年信息学奥林匹克联赛（复赛）【二等奖】", "value": 55 },
    { "label": "全国青少年信息学奥林匹克联赛（复赛）【三等奖】", "value": 56 }
]

COLLEGES = [
    { "label": "计算机科学与技术学院", "value": 1 },
    { "label": "物理学院", "value": 2 },
    { "label": "数学学院", "value": 3 },
    { "label": "软件学院", "value": 4 },
    { "label": "化学与化工学院", "value": 5 },
    { "label": "生命科学学院", "value": 6 },
    { "label": "土建与水利学院", "value": 7 },
    { "label": "控制科学与工程学院", "value": 8 },
    { "label": "材料科学与工程学院", "value": 9 },
    { "label": "能源与动力工程学院", "value": 10 },
    { "label": "机械工程学院", "value": 11 },
    { "label": "齐鲁交通学院", "value": 12 },
    { "label": "信息科学与工程学院", "value": 13 },
    { "label": "网络空间安全学院", "value": 14 },
    { "label": "环境科学与工程学院", "value": 15 },
    { "label": "管理学院", "value": 16 },
    { "label": "集成电路学院", "value": 17 },
    { "label": "人工智能学院", "value": 18 },
    { "label": "药学院", "value": 19 },
    { "label": "公共卫生学院", "value": 20 },
    { "label": "经济学院", "value": 21 },
    { "label": "电气工程学院", "value": 22 },
    { "label": "政治学与公共管理学院", "value": 23 },
    { "label": "法学院", "value": 24 },
    { "label": "文学院", "value": 25 },
    { "label": "基础医学院", "value": 26 },
    { "label": "哲学与社会发展学院", "value": 27 },
    { "label": "考古学院", "value": 28 },
    { "label": "国际教育学院", "value": 29 },
    { "label": "艺术学院", "value": 30 },
    { "label": "新闻传播学院", "value": 31 },
    { "label": "历史学院", "value": 32 },
    { "label": "马克思主义学院", "value": 33 },
    { "label": "外国语学院", "value": 34 },
    { "label": "口腔医学院", "value": 35 },
    { "label": "护理与康复学院", "value": 36 },
    { "label": "体育学院", "value": 37 },

    { "label": "儒学高等研究院(文史哲研究院)", "value": 50 },
    { "label": "晶体材料研究院", "value": 51 },
    { "label": "经济研究院", "value": 52 },
    { "label": "外国语学院(大学外语教学部)", "value": 53 },
    { "label": "中泰证券金融研究院", "value": 54 },
    { "label": "新一代半导体材料研究院", "value": 55 },
    { "label": "第一临床学院", "value": 56 },
    { "label": "第二临床学院", "value": 57 },
    { "label": "医学融合与实践中心", "value": 58 },
    { "label": "未来技术学院", "value": 59 },
    { "label": "国际创新转化学院", "value": 60 },
    { "label": "前沿交叉科学青岛研究院", "value": 61 },
    { "label": "微生物技术研究院", "value": 62 },
    { "label": "海洋研究院", "value": 63 },
    { "label": "人文社会科学青岛研究院", "value": 64 },
    { "label": "环境研究院", "value": 65 },
    { "label": "数学与交叉科学研究中心", "value": 66 },
    { "label": "中加合作办学项目", "value": 67 },
    { "label": "智能创新研究院", "value": 79 },
    { "label": "人工智能国际联合研究院", "value": 68 },
    { "label": "泰山学堂", "value": 99 },
    
    { "label": "东北亚学院（威海）", "value": 100 },
    { "label": "艺术学院（威海）", "value": 101 },
    { "label": "马克思主义学院（威海）", "value": 102 },
    { "label": "体育教学部（威海）", "value": 103 },
    { "label": "翻译学院（威海）", "value": 104 },
    { "label": "山东大学澳国立联合理学院（威海）", "value": 105 },
    { "label": "文化传播学院（威海）", "value": 106 },
    { "label": "法学院（威海）", "value": 108 },
    { "label": "商学院（威海）", "value": 108 },
    { "label": "海洋学院（威海）", "value": 109 },
    { "label": "空间科学与物理学院（威海）", "value": 110 },
    { "label": "数学与统计学院（威海）", "value": 111 },
    { "label": "机电与信息工程学院（威海）", "value": 112 }
]

