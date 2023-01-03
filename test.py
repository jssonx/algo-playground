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

res = getLevel(q_table, "tenth-line")
print(res)