#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2
s = input ("Please enter a string that contains one bob:")
s.lower()
number_of_bob = 0
length_of_string = len(s) 
length_of_word = 0
y = 3
cut_string = ([])
for x in range(0,len(s)):
    cut_string.append(s[length_of_word:y])
    length_of_word += 1
    y += 1
for x in cut_string:
    if x == 'bob':
        number_of_bob +=1
print (number_of_bob)
##print (cut_string)
   