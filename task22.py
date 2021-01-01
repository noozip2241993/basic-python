def count_number(n2):
    count = 0
    for i in n2:
        if i == 4:
            count +=1
    return count
a = [1,4,6,7,4]
print(count_number(a))