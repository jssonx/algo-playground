import os
import jsonlines

# construct a provblem table
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

path = "./algorithms/java"
files =  os.listdir(path)
files.sort()
f = open(readme, 'a+')
f.write("# LeetCode Algorithm" + '\n'+ '\n')
f.write("| # | Title | Solution | Difficulty |" + '\n')
f.write("|---| ----- | -------- | -------- |" + '\n')

# files = str(files).split(".")
for file in files:
    file_original = file
    file = str(file).split(".")
    if file[2] == "java":
        
        # part1: problem name
        q_name = file[1]
        q_name = q_name.split("-")
        q_name = [s.capitalize() for s in q_name]
        q_name = str(' '.join(q_name))
        url = "https://leetcode.com/problems/" + str(file[1]) + "/"
        part1 = "[" + q_name + "]" + "(" + url + ")"

        # part2: solution path
        q_path = "./algorithms/java/" + str(file_original)
        part2 = "[Java]" + "(" + q_path + ")"

        # part3: difficulty
        part3 = getLevel(q_table, file[1])
        print(part3)

        # output
        f.write("|" + file[0] + "|" + part1 + "|" + part2 + "|" + part3 + "|" + '\n')

f.close()
