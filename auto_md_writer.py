import os
import jsonlines
import time

# get the modify time of a file
def timeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

def get_FileModifyTime(fileName):
    if fileName.endswith(".java"):
        filePath = "./algorithms/java/" + fileName
    elif fileName.endswith(".py"):
        filePath = "./algorithms/python/" + fileName
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

all_problems_path = "/home/jsson/.lc/leetcode/cache/problems.json"
q_table = json_data_read(all_problems_path)
q_table = q_table[0]

# get the level of a problem
def getLevel(q_table, problem):
    for i in range(len(q_table)):
        if problem in q_table[i]["link"]:
            return str(q_table[i]["level"])

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

files = []
for i in range(len(dir_list)):
    path = "./algorithms/" + dir_list[i]
    tmp =  os.listdir(path)
    files += tmp

files.sort()

f = open(readme, 'a+')
f.write("# LeetCode Algorithms" + '\n'+ '\n')
f.write("| # | Title | Solution | Difficulty | Time |" + '\n')
f.write("|---| ----- | -------- | -------- | -------- |" + '\n')

# main loop
full_prob_table = []
full_num = {}
for file in files:
    repeated = False 
    file_original = file
    file = str(file).split(".")

    # part0: problem number
    part0 = int(file[0])
    if part0 not in full_num:
        full_num[part0] = file[2]  
    else:
        repeated = True
        
    # part1: problem name
    q_name = file[1]
    q_name = q_name.split("-")
    q_name = [s.capitalize() for s in q_name]
    q_name = str(' '.join(q_name))
    url = "https://leetcode.com/problems/" + str(file[1]) + "/"
    part1 = "[" + q_name + "]" + "(" + url + ")"

    # part2: solution path
    if file_original.endswith(".java"):
        q_path = "./algorithms/java/" + str(file_original)
        part2 = "[Java]" + "(" + q_path + ")"
    elif file_original.endswith(".py"):
        q_path = "./algorithms/python/" + str(file_original)
        part2 = "[Python]" + "(" + q_path + ")"
    
    if repeated:
        if full_num[part0] == "java":
            part2 +=" " + "[Java]" + "(" + "./algorithms/java/" + str(part0) + "." + file[1] + ".java" + ")"
        elif full_num[part0] == "py":
            part2 += " " + "[Python]" + "(" + "./algorithms/python/" + str(part0) + "." + file[1] + ".py" + ")"

    # part3: difficulty
    part3 = getLevel(q_table, file[1])

    # part4: modify time
    part4 = get_FileModifyTime(file_original)

    one_line = str(part0) + "$" + " | " + str(part0) + " | " + part1 + " | " + part2 + " | " + part3 + " | " + part4 + " |" + '\n'
    
    if not repeated:
        full_prob_table.append(one_line)
    else:
        for i in range(len(full_prob_table)):
            num = full_prob_table[i].split("$")[0]
            if num == str(part0):
                full_prob_table[i] = one_line
                break

# output
for i in range(len(full_prob_table)):
    f.write(full_prob_table[i].split("$")[1])

f.close()