s = input ("Please enter a string:")
number_of_vowels = 0
s = s.lower()
for char in s:
    if char in list(['a','e','i','o','u']):
        number_of_vowels += 1
print ('Number of Vowels:' + str(number_of_vowels))
