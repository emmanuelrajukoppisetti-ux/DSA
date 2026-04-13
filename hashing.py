'''frequency of all occurances'''
'''arr=list(map(int,input("enter numbers :").split()))
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
for key in freq:
    print(key,":",freq[key],"times")'''



"""Find the missing value"""
arr=list(map(int,input("enter numbers : ").split()))
n=int(input("enter the total number count :"))
e_sum=n*(n+1)//2
o_sum=sum(arr)
print("missing number :" ,e_sum-o_sum)