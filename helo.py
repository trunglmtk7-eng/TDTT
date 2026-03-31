lst = [
    [9,7,8,2,5],
    [4,10,3,1],]
max1= -100000
idx = ""
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if max1 < lst[i][j]:
            max1= lst[i][j]
            idx = f"{i},{j}"
print(max1,idx) 