import os
import copy
import json
import jsonlines
import time
import datetime

# construct a table of tags
tags_files = []
tags_path = "/home/jsson/.lc/leetcode/cache/"
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
with open('tags.json', 'w') as f:
    json.dump(json_data, f, indent = 4)

# get the modify time of a file
def timeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

def get_FileModifyTime(fileName):
    if fileName.endswith(".java"):
        filePath = "./algorithms/java/" + fileName
    elif fileName.endswith(".py"):
        filePath = "./algorithms/python/" + fileName
    elif fileName.endswith(".rs"):
        filePath = "./algorithms/rust/" + fileName
    t = os.path.getmtime(filePath)
    res = (timeStampToTime(t)).split(" ")
    return res[0]

# construct a full problem table
def json_data_read(json_file_name):
    json_list = []
    with open(json_file_name, 'r+') as f:
        for item in jsonlines.Reader(f):
            json_list.append(item)
    return  json_list

# get tags, names and levels
with open('tags.json', 'r') as f_table:
    tags_table = json.load(f_table)

def get_tags(p_num, tags_table):
    for i in range(len(tags_table)):
        if tags_table[i]['fid'] == p_num:
            return tags_table[i]['tags'], tags_table[i]['name'], tags_table[i]['level']

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
f.write("# LeetCode Algorithms" + '\n'+ '\n')
f.write("| # | Title | Solution | Difficulty | Time | Tags |" + '\n')
f.write("| --- | ----- | -------- | -------- | -------- | -------- |" + '\n')

# main loop
full_prob_table = []
full_num = {}
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")
today = (now.split(" "))[0]
today_num = 0
for file in files:
    repeated = 0 
    file_original = file
    file = str(file).split(".")

    # part0: problem number
    part0 = int(file[0])
    if part0 not in full_num:
        full_num[part0] = []
        full_num[part0].append(file[2])
    else:
        full_num[part0].append(file[2])
        
    # part2: solution path
    part2 = ""
    tmp_full_num_part0 = copy.deepcopy(full_num[part0])
    for i in range(0, len(tmp_full_num_part0)):
        if "java" in tmp_full_num_part0:
            part2 += " " + "[Java]" + "(" + "./algorithms/java/" + str(part0) + "." + file[1] + ".java" + ")"
            tmp_full_num_part0.remove("java")
        elif "py" in tmp_full_num_part0:
            part2 += " " + "[Python]" + "(" + "./algorithms/python/" + str(part0) + "." + file[1] + ".py" + ")"
            tmp_full_num_part0.remove("py")
        elif "rs" in tmp_full_num_part0:
            part2 += " " + "[Rust]" + "(" + "./algorithms/rust/" + str(part0) + "." + file[1] + ".rs" + ")"
            tmp_full_num_part0.remove("rs")
    
    # part4: modify time
    part4 = get_FileModifyTime(file_original)

    # part5: tags
    tag, q_name, q_level = get_tags(part0, tags_table)
    part5 = tagging(tag)

    # part1: problem name
    url = "https://leetcode.com/problems/" + str(file[1]) + "/"
    part1 = "[" + q_name + "]" + "(" + url + ")"

    # part3: difficulty
    part3 = q_level

    one_line = str(part0) + "$" + " | " + str(part0) + " | " + part1 + " | " + part2 + " | " + part3 + " | " + part4 + " | " + part5 + " |" + '\n'

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
with open('output_table.json', 'w') as f_table:
    json.dump(full_prob_table, f_table, indent = 4)

# output
# with open('output_table.json', 'r') as f_table:
#     full_prob_table = json.load(f_table)

for i in range(len(full_prob_table)):
    f.write(full_prob_table[i].split("$")[1])

f.write("\n")
f.write("##### ∑all = " + str(len(full_prob_table)) +  "&nbsp;&nbsp;" + "∑" + today + " = " + str(today_num))

f.close()