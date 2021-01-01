def histogram(n):
    for i in n:
        output = ""
        times = i
        while times >0:
            output += "*"
            times = times -1
        print(output)
histogram([2,3,6,5])
