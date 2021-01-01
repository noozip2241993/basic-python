def adding_two_objects(n1,n2):
    if not (isinstance(n1,str) and isinstance(n2,str)):
        raise TypeError("Input must be integers")
    return n1+ n2

print(adding_two_objects('2','3'))
n3=3 
n4= 'as'
if isinstance(n4,str):
    print('True')
else:
    print('False')