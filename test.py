
import json
import jsonlines
import os

def json_data_read(json_file_name):
    json_list = []
    with open(json_file_name, 'r+') as f:
        for item in jsonlines.Reader(f):
            json_list.append(item)
    return  json_list

tags_files = []
tags_path = "/home/jsson/.lc/leetcode/cache/"
tags_files = os.listdir(tags_path)
tags_files.remove('problems.json')
tags_files.remove('translationConfig.json')

# 读取所有json文件
json_data = []
for file in tags_files:
    with open(tags_path + file, 'r') as f:
        data = json.loads(f.read())
        json_data.append(data)

# 将所有json文件内容并列存放在新的json文件中
with open('tags.json', 'w') as f:
    json.dump(json_data, f, indent = 4)

##################################################

def tagging(tags):
    tag_list = []
    for tag in tags:
        tag_list.append("`" + tag + "`")
    return " ".join(tag_list)


with open('tags.json', 'r') as f_table:
    tags_table = json.load(f_table)
def get_tags(p_num, table):
    for i in range(len(table)):
        if table[i]['fid'] == p_num:
            print(table[i]['fid'], p_num)
            print(table[i]['tags'])
            return table[i]['tags']

tags = get_tags(707, tags_table)
print(tagging(tags))