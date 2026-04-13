"""program to reverse the words in a striing"""
'''words=input("enter words").split()
for word in words:
    print(word[::-1],end=" ")'''


'''program to find the smallest word iexcographical from the given list of words (dictionary order)'''
words=input("enter words").split()
min_word=words[0]
for word in words:
    if word<min_word:
        min_word=word
print('smallest word :',min_word)