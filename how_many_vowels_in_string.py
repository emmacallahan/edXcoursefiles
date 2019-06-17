number_of_vowels = 0
number_of_consonants = 0
s = 'azcbobobegghakl'
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        number_of_vowels += 1
    else:
        number_of_consonants += 1

print ('Number of Vowels:' + str(number_of_vowels))
