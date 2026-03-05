

S = str(input())

cnt = 0
string_li = []
num_dic = {}

for i in S:
    if i in string_li:
        num_dic[str(i)] += 1
        continue
    
    string_li.append(i)
    num_dic[str(i)] = 1
    
num_li = sorted(num_dic)

for j in num_li:
    if (j == "A") and (num_dic["A"] == 1):
        pass