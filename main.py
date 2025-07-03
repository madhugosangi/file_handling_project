from pathlib import Path
import os

def reading_folder():
    path=Path(' ')
    items=list(path.rglob("*"))
    
    for i,items in enumerate(items):
        print(f"{i+1} : {items} ")


def create_file():
    try:
        reading_folder()
        name=input("enter the file name:-")
        p=Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data=input("enter data to create a file:-")
                fs.write(data)
            print("file created sucessfully")
        else:
            print("file already exist")   
    except Exception as err:
        print(f"exception occur in the name of {err}")
    

def Read_file():
    try:
        reading_folder()
        name=input("enter file name:-")
        p=Path(name)
        if not p.exists():
            print("file doesn't exist")
        else:
            with open(p,"r") as fs:
                data=fs.read()
                print(data)
            print("file readed successfully")
    except Exception as err:
        print(f"exception occur in the name of {err}")



def update_file():
    try:
        reading_folder()
        name=input("enter the file name:-")
        p=Path(name)
        if p.exists and p.is_file():
            print("enter 1 for updating the file name")
            print("enter 2 for over writing the data of a file")
            print("enter 3 for appending the data into the file")
            res=int(input("enter your response:-"))
            if res==1:
                name2=input("tell your new file name:-")
                p2=Path(name2)
                p.rename(p2)
        
            elif res==2:
                with open(p,"w") as fs:
                    data=input("enter new data to over write:-")
                    fs.write(data)

            elif res==3:
                with open(p,"a") as fs:
                    data=input("enter data to append in to a file:-")
                    fs.write(" "+data)
            print("file updated sucessfully")

        else:
            print("file not exist")   
    except Exception as err:
        print(f"exception occur in the name of {err}")

def delete_file():
    try:
        reading_folder()
        name=input("enter the file name which you want to delete:-")
        p=Path(name)
        if p.exists and p.is_file():
            os.remove(p)
        else:
            print("file doesn't exist")
    except Exception as err:
        print(f"exception occur in the name of {err}")


print("press 1 for creating a file \n press 2 for reading a file \n press 3 for updating a file \n press 4 for deleting a file")
option=int(input("enter your choice:-"))
if option==1:
    create_file()
elif option==2:
    Read_file()
elif option==3:
    update_file()
elif option==4:
    delete_file()
else:
    print("choose the correct option")
