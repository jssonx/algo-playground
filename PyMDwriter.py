# -*- coding: utf-8 -*-

import os
import copy
import json
import jsonlines
import time
import datetime
import shutil

# create leetcode cache
src_folder = os.path.join(os.path.expanduser("~"), ".lc/leetcode/cache")
dst_folder = './lc-cache/'

if os.path.exists(dst_folder):
    shutil.rmtree(dst_folder)
shutil.copytree(src_folder, dst_folder)

# type:directory
solution_type = {"cpp":"cpp", "rs":"rust", "java":"java", "py":"python"}

# construct a table of tags
tags_files = []
tags_path = os.path.expanduser("./lc-cache/")
tags_files = os.listdir(tags_path)
tags_files.remove('problems.json')
tags_files.remove('translationConfig.json')

# read all json files
json_data = []
for file in tags_files:
    with open(tags_path + file, 'r') as f:
        data = json.loads(f.read())
        json_data.append(data)

# store the contents of all json files side-by-side in a new json file
with open('./json/tags.json', 'w') as f_tags:
    json.dump(json_data, f_tags, indent = 4)

# get the modify time of a file
def timeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

# construct a full problem table
def json_data_read(json_file_name):
    json_list = []
    with open(json_file_name, 'r+') as f:
        for item in jsonlines.Reader(f):
            json_list.append(item)
    return  json_list

# get tags, names and levels
with open('./json/tags.json', 'r') as f_table:
    tags_table = json.load(f_table)

def get_tags(p_num, tags_table):
    for i in range(len(tags_table)):
        if tags_table[i]['fid'] == p_num:
            if 'tags' not in tags_table[i]:
                tags_table[i]['tags'] = ["no-tags"]
            return tags_table[i]['tags'], tags_table[i]['name'], tags_table[i]['level'], tags_table[i]['link']

def tagging(tags):
    tag_list = []
    for tag in tags:
        tag_list.append("`" + tag + "`")
    return " ".join(tag_list)

# construct a readme file
readme = "README.md"

if os.path.isfile(readme):
    os.remove(readme)

# get all the files in the algorithms folder
input_path = "./algorithms"
dir_list = []
for root, dirs, files in os.walk(input_path):        
    dir_list = dirs              
    break

# get sorted list of files
files = []
for i in range(len(dir_list)):
    path = "./algorithms/" + dir_list[i]
    tmp =  os.listdir(path)
    files += tmp

sorted_res = []
for i in range(len(files)):
    n = int((files[i].split("."))[0])
    sorted_res.append((n, files[i]))

sorted_tuple_list = sorted(sorted_res, key=lambda x: x[0], reverse = True)
files_sorted = []
for t in sorted_tuple_list:
    files_sorted.append(t[1])

files = files_sorted

f = open(readme, 'a+')

# main loop
full_prob_table = []
full_num = {}
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")
today = (now.split(" "))[0]
today_num = 0
full_tags = set()
for file in files:
    repeated = False
    file_original = file
    file = str(file).split(".")

    # part0: problem number
    part0 = int(file[0])
    if part0 not in full_num:
        full_num[part0] = []
        full_num[part0].append(file[2])
    else:
        full_num[part0].append(file[2])
        repeated = True
        
    # part2: solution path
    part2 = ""
    tmp_full_num_part0 = copy.deepcopy(full_num[part0])
    for _type in tmp_full_num_part0:
        if _type in solution_type:
            part2 += " " + "[" + solution_type[_type].capitalize() + "]" + "(" + "./algorithms/" + solution_type[_type] + "/" + str(part0) + "." + file[1] + "." + _type + ")"
        else:
            print("Warning: This type of solution has not been added to the dictionary.")
    
    # part4: modify time
    # part4 = get_FileModifyTime(file_original)

    # part5: tags
    tag, q_name, q_level, q_link = get_tags(part0, tags_table)
    part5 = tagging(tag)
    full_tags = full_tags.union(set(tag))

    # part1: problem name
    url = q_link.split("description/")[0]
    part1 = "[" + q_name + "]" + "(" + url + ")"

    # part3: difficulty
    part3 = q_level

    one_line = str(part0) + "$" + " | " + str(part0) + " | " + part1 + " | " + part2 + " | " + part3 + " | " + part5 + " |" + '\n'

    if today in one_line:
        today_num += 1

    if not repeated:
        full_prob_table.append(one_line)
    else:
        # update this line (since there is a new revision time and possibly a new solution)
        for i in range(len(full_prob_table)):
            num = full_prob_table[i].split("$")[0]
            if num == str(part0):
                full_prob_table[i] = one_line
                break

# save the list to the local file
with open('./json/output_table.json', 'w') as f_table:
    json.dump(full_prob_table, f_table, indent = 4)

## Part 1
f.write("## LeetCode Algorithms: By tags" + '\n'+ '\n')

# 创建一个空字典来存储题目及其标签
tag_dict = {}

# 遍历问题列表，并将每个问题及其标签添加到字典中
for problem in full_prob_table:
    parts = problem.split("|")
    tags = [tag.strip() for tag in parts[5].split("`")[1:-1]]
    # print(tags)
    for tag in tags:
        if tag == "":
            continue
        if tag not in tag_dict:
            tag_dict[tag] = []
        # print((parts[1], parts[2].strip(), parts[4].strip(), parts[3].strip()))
        tag_dict[tag].append((parts[1].strip(), parts[2].strip(), parts[4].strip(), parts[3].strip()))

# 设置快捷跳转：[跳转到我的文章](#my-article)
# Navigation
f.write("#### Navigation" + '\n'+ '\n')
f.write("| " + '\n')
for tag in sorted(tag_dict, key=lambda x: (-len(tag_dict[x]), x)):
    f.write("[" + str(tag.capitalize()) + "](#" + str(tag) + ")"+ " `" + str(len(tag_dict[tag])) + "`" + " | ")
f.write("\n")

# Add template
f.write("#### Template" + '\n'+ '\n')

# 生成每个标签的列表
for tag in sorted(tag_dict.keys()):
    # print(tag, len(tag_dict[tag]))
    f.write("#### " + tag.capitalize() + "\n")
    plist = {"Easy": [], "Medium": [], "Hard": []}  # 用字典代替列表进行分类
    for problem in tag_dict[tag]:
        plist[problem[2]].append(problem)  # 将问题添加到对应难度的列表中
    for level in ["Easy", "Medium", "Hard"]:
        for problem in plist[level]:
            f.write("- <small>[" + problem[0] + "." + problem[1] + "](" + level + ") - " + problem[3] + "</small>\n")
    f.write("\n")
    f.write("<small>[Back to Top](#navigation)</small>" + '\n')

# Part 2
# f.write("## The Full List" + '\n'+ '\n')
# f.write("| # | Title | Solution | Difficulty | Tags |" + '\n')
# f.write("| --- | ----- | -------- | -------- | -------- |" + '\n')
# for i in range(len(full_prob_table)):
#     f.write(full_prob_table[i].split("$")[1])

f.close()