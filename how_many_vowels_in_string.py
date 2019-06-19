s = input ("Please enter a string:")
number_of_vowels = 0
number_of_consonants = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' :
        number_of_vowels += 1
    else:
        number_of_consonants += 1

print ('Number of Vowels:' + str(number_of_vowels))
