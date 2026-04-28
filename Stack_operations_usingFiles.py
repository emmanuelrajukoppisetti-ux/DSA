#application of stack for menu diriven operations using files
import os 
import sys
undo_stack =[]
redo_stack =[]
filename="sample.txt"
try :
    with open(filename,"r") as f:
        text=f.read()
except:
    text=""
while True:
    print("\n. Perform action")
    print("2. Undo")
    print("3. Redo")
    print("4. Display")
    print("5. Exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        newtext=input("enter action :")
        undo_stack.append(text)
        text+=newtext
        redo_stack.clear()
        with open(filename,"a") as f:
            f.write(text)
        print("Written in file..... check sample.txt")
    elif choice==2:
        if len(undo_stack)==0:
            print("Nothing to perform !!!!")
        else:
            redo_stack.append(text)
            text=undo_stack.pop()
            with open(filename,"w") as f:
                write(text)
            print("undo Performed")
    elif choice==3:
        if len(redo_stack)==0:
            print(" Nothing to perform Redo  !!!!")
        else:
            undo_stack.append(text)
            text=redo_stack.pop()
            with open(filename,"w") as f:
                write(text)
            print("Redo Performed")
    elif choice==4:
        with open(filename,"r") as f:
            print("file content:",f.read())
    elif choice==5:
        break
    else:
        print("Invalid Choice.....Try again ")