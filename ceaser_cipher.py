'''encrypt a word using ceaser cipher'''
word=input("enter a word :")
key=int(input("enter a key :"))
result=""
for ch in word:
    if ch.isalpha():
        if ch.islower():
            new=chr(ord(ch)+key)
            result+=new
        else:
            new=chr(ord(ch)+key)
            result+=new
print(result)

