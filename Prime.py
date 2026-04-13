#program to check if a number is prime or not using brute fource method

'''num=int(input("enter a number:"))
is_prime=True
for i in range(2,num):
    if num%i==0:
        is_prime=False
        break
if is_prime:
    print(num,"ia a prime number")
else:
    print(num,"is not a prime number")'''


'''math apporch of prime number'''

num=int(input("enter a number:"))
is_prime=True
i=2
while i*i<=num:
    if num%i==0:
        is_prime=False
        break
    i+=1
if is_prime:
    print(num,"ia a prime number")
else:
    print(num,"is not a prime number")