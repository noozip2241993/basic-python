def get_copies_first_2_character(str,n):
    result = ""
    if len(str) >=2:
        for i in range(n):
            result += str[:2]
    else:
        result += str*n
    return result
print(get_copies_first_2_character('a',4))

        

