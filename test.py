full_num = {}
if 1 not in full_num:
    full_num[1] = []
full_num[1].append("a.java")

if 2 not in full_num:
    full_num[2] = []
full_num[2].append("b.java")

full_num[1].append("a.rs")
print(full_num)