import os
readme = "README.md"

if os.path.isfile(readme):
    os.remove(readme)

path = "./algorithms/java"
files =  os.listdir(path)
files.sort()
f = open(readme, 'a+')
f.write("# LeetCode Algorithm" + '\n'+ '\n')
f.write("| # | Title | Solution |" + '\n')
f.write("|---| ----- | -------- |" + '\n')
    
# |1|[Two Sum]()| [Java](./algorithms/java/1.twoSum.java)|

# files = str(files).split(".")
for file in files:
    file_original = file
    file = str(file).split(".")
    if file[2] == "java":
        
        # part1
        q_name = file[1]
        q_name = q_name.split("-")
        q_name = [s.capitalize() for s in q_name]
        q_name = str(' '.join(q_name))
        url = "https://leetcode.com/problems/" + str(file[1]) + "/"
        part1 = "[" + q_name + "]" + "(" + url + ")"

        # part2
        q_path = "./algorithms/java/" + str(file_original)
        part2 = "[Java]" + "(" + q_path + ")"

        # output
        f.write("|" + file[0] + "|" + part1 + "|" + part2 + "|" + '\n')


f.close()
