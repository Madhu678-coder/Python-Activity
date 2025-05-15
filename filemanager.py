import os
def get_curr_working_dir():
    return os.getcwd()

def list_files_in_curr_dir():
    return os.listdir(get_curr_working_dir())

def create_file(f):
    open(f,'w').close()

def read_file(f):
    try:
        with open(f, 'r') as file:
            content = file.read()
            print(content)
            f.close()
    except FileNotFoundError:
        print("File not found.Give correct file name")

def write_to_file(f,matter):
    try:
        with open(f, 'a') as file:
            file.write(matter)
    except FileNotFoundError:
        print("File not found. Give correct file name.")

def change_dir(dir):
    try:
        os.chdir(dir)
    except FileNotFoundError:
        print("Directory not found")

while True:

    command = input("\n"+get_curr_working_dir()+">"+" Enter your command: ").split(" ",maxsplit=2)

    if command[0]=="exit":
        break

    if command[0]=="touch":
        file_name = command[1]
        if(len(command)==3):
            matter = command[2]
            write_to_file(file_name[1:len(matter)-1],matter[1:len(matter)-1])
        else:
            create_file(file_name)

    elif command[0]=="ls":
        lst = list_files_in_curr_dir()
        lst = map(lambda x: x if '.' in x else x+"\\",lst)
        for _ in lst:
            print(_,end="   ")

    elif command[0]=="cd":
        change_dir(command[1])
        print(get_curr_working_dir())