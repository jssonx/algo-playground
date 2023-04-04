import json
import random
# python .\leetcode-random.py
# 要查询的标签名，指定数量的题目级别
tag_name, easy_count, medium_count, hard_count = "two-pointers", 1, 3, 0

# 从本地 JSON 文件加载数据
with open("tags.json", "r") as f:
    data = json.load(f)

# 筛选符合标签的问题
problems = []
for problem in data:
    if "tags" in problem and tag_name in problem["tags"]:
        problems.append(problem)

def get_tags(p_num, tags_table):
    for i in range(len(tags_table)):
        if tags_table[i]['fid'] == p_num:
            if 'tags' not in tags_table[i]:
                tags_table[i]['tags'] = ["no-tags"]
            return tags_table[i]['tags'], tags_table[i]['name'], tags_table[i]['level']

# 根据指定数量选择问题
selected_problems = []
for count, level in [(easy_count, "Easy"), (medium_count, "Medium"), (hard_count, "Hard")]:
    level_problems = [problem for problem in problems if get_tags(problem["fid"], data)[2] == level]
    if len(level_problems) < count:
        raise ValueError(f"Not enough problems with level {level}")
    selected_problems += random.sample(level_problems, count)

# 输出选中的问题
random.shuffle(selected_problems)
for problem in selected_problems:
    p_tags, p_name, p_level = get_tags(problem["fid"], data)
    print(f"{problem['id']}. {problem['name']} ({p_level}) - {p_tags}")
