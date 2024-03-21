string1 = "Espresssif"
stringlist = list(string1)
string2 = ' '.join(stringlist)
print(string2)

def replace_vowels_with_star(s):
    vowels = 'aeiouAEIOU'
    for vowel in vowels:
        s = s.replace(vowel, '*')
    return s

# 示例
original_string = "Hello, World!"
new_string = replace_vowels_with_star(string2)
print(new_string)  # 输出: H*ll*, W*rld!

