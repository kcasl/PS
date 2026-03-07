import sys

input = sys.stdin.readline

string = str(input().rstrip())
ex_string = str(input().rstrip())

new_string = string

# front_li = []
# string_valid_li = []
# cnt = 0

while True:
    if (ex_string in new_string) == False:
        break
    
    new_string = new_string.replace(ex_string, "")
    
    # for i in string:
    #     if i == ex_string[0]:
    #         front_li.append(cnt)
    #     cnt += 1

    # for j in front_li:
    #     print(string[j: j + len(ex_string) + 1])
    #     string_valid_li.append(string[j:  j + len(ex_string) - 1])
        
    # for 
        
    # cnt = 0

if len(new_string) == 0:
    print("FRULA")
else:
    print(new_string)