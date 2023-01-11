a = "a.java"
b = "b.py"
a_suffix = a.split(".")[1]

solution_type = {"rs":"rust", "java":"java", "py":"python"}
for s_type in solution_type:
    if s_type == a_suffix:
        print(solution_type[s_type])

