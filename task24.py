def check_vowvel(str):
    vowels = ['a','e','i','o','u']
    for i in (str):
        if i in vowels:
            print(f'this {str} is a vowel')
        else:
            print(f'this {str} is not a vowel')
check_vowvel('passed')