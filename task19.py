def get_a_new_string(str):
    if len(str) >=2 and str[:2] =='Is':
        return str
    else: return 'Is' + str
print(get_a_new_string('Is1231'))