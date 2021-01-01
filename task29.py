def color_sets(color1,color2):
    new_color_set = []
    for i in color1:
        if i not in color2:
            new_color_set.append(i)
    return new_color_set
color1 = set(['White','Black','Red'])
color2 = set(['Red','Green'])

print(color_sets(color1,color2))
