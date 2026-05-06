n=int(input("enter Number :"))
square=n*n
if str(square).endswith(str(n)):
    print("automorphic Number")
else:
    print("not automorphic Number ")