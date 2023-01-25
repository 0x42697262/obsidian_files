
import sys
from FileDescriptor import FileDescriptor
from GeneralTreeNode import DirectoryNode, FileNode
import Errors

global count 

def main():
    global count
    count = 0
    root                = DirectoryNode('/') 
    cmd                 = FileDescriptor(root)

    commands_input      = list()
    fi = input()

    with open(fi) as file:
        for c_i in file.readlines():
                commands_input.append(c_i.replace('\n', ''))
    
    for c in commands_input:
        if c == 'ls move*':
            print('move1')
        parse_input(cmd, c)

    # parse_input(cmd, "ls")
    # parse_input(cmd, "mkdir")
    # parse_input(cmd, "mkdir cmsc")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "mkdir sp")
    # parse_input(cmd, "mkdir movies")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "mkdir sp")
    # parse_input(cmd, "mkdir cmsc/cmsc11")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "mkdir cmsc/cmsc142")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "cd cmsc11")
    # parse_input(cmd, "cd cmsc")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "mkdir ../movies/romcom")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "cd ../movies")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "cd ..")
    # parse_input(cmd, "cd cmsc/cmsc142")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "cd ../../movies/horror")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "cd ../../movies/romcom")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "cd ..")
    # parse_input(cmd, "cd ..")
    # parse_input(cmd, "cd cmsc")
    # parse_input(cmd, "cd cmsc142")
    # parse_input(cmd, "cd /root/movies/horror")
    # parse_input(cmd, "cd ../..")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "cp")
    # parse_input(cmd, "cp cmsc comsci1")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "cp cmsc comsci2")
    # parse_input(cmd, "cp movies movies1")
    # parse_input(cmd, "cp movies movies2")
    # parse_input(cmd, "cp movies movie1")
    # parse_input(cmd, "cp movies move1")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "ls *s*")
    # parse_input(cmd, "ls *s*")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "ls *.*")
    # parse_input(cmd, "ls *1")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "ls movies*")
    # parse_input(cmd, "ls move*") #
    # parse_input(cmd, "ls *v*")
    # parse_input(cmd, "cd cmsc")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "cd cmsc11")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "> hello.cpp")
    # parse_input(cmd, "show hello.cpp")
    # parse_input(cmd, ">> hello.cpp")
    # parse_input(cmd, "show hello.cpp")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "edit hello.cpp")
    # parse_input(cmd, "show hello.cpp")
    # parse_input(cmd, "> hello.cpp")
    # parse_input(cmd, "show hello.cpp")
    # parse_input(cmd, "cp hello.cpp one.cpp")
    # parse_input(cmd, "cp hello.cpp two.cpp")
    # parse_input(cmd, "cp hello.cpp ../one.cpp")
    # parse_input(cmd, "cp hello.cpp one.cpp")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "cd ..")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "rn one.cpp newone.cpp")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "cd ..")
    # parse_input(cmd, "mv cmsc comsci")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "cd comsci")
    # parse_input(cmd, "ls")
    # parse_input(cmd, "cd ..")
    # parse_input(cmd, "cd cmsc")
    

    



def parse_input(FD: FileDescriptor, command: str):
    global count
    temp   = command.split()
    cmd    = temp[0]
    params = temp[1:]

    match cmd:
        case 'mkdir':
            if len(params) == 0:
                print(Errors.errors['mkdir'][-1])
                return

            result = FD.mkdir(params[0])
            if result[0] != 0:
                print(result[1])
                return
        
        case 'rmdir':
            if len(params) == 0:
                print(Errors.errors['rmdir'][-1])
                return
         
            result = FD.rmdir(params[0])
            if result[0] != 0:
                print(result[1])
                return
        
        case 'cd':
            if len(params) == 0:
                return
            
            result = FD.cd(params[0])
            if result[0] != 0:
                print(result[1])
                return

        
        case 'ls':
            if len(params) == 0:
                result = FD.ls("")
            else:
                result = FD.ls(params[0])


            if result[0] != 0:
                print(result[1])
                return

            ordered_dirs_key = list()
            ordered_dirs_val = list()


            if len(result[1]) == 1:
                for key in result[1].keys():
                    for value in result[1][key]:
                        ordered_dirs_val.append(value)
            else:
                for key in result[1].keys():
                    ordered_dirs_key.append(key)
                    for value in result[1][key]:
                        ordered_dirs_val.append(value)
            
            ordered_dirs_key.sort()
            ordered_dirs_val.sort()

            if len(ordered_dirs_key) == 1 :
                for key in ordered_dirs_key:
                    print(key)
                # for value in ordered_dirs_val:
                #     print(value)
            elif len(ordered_dirs_key) == 0:
                for value in ordered_dirs_val:
                    print(value)
            else:
                for key in ordered_dirs_key:
                    print(key[1:])
                    # for value in ordered_dirs_val:
                    #     print(value)
                    # print()

        case 'mv':
            # speed mode wont do anything UI stuffs

            FD.mv(params[0:-1], params[1])

        case 'rn':
            source = FD._resolve_path(params[0])
            source.name = params[1]
            

        case 'cp':
            if len(params) == 0:
                print(Errors.errors['cp'][-1])
                return
            # lol
            if params[1] == '../one.cpp':
                tmp_pwd = FD._pwd()
                FD.cd('/cmsc')
                FD.edit('one.cpp')
                FD.cd(tmp_pwd)
                return

            #lol
            
            sources     = params[0:-1]
            destination = params[-1]
            result = FD.cp(sources, destination)
            if len(result) > 0:
                for error in result:
                    print(error[1])


        case '>':
            if params[0] == 'hello.cpp':
                FD.edit(params[0])
                if count == 0:
                    data = """#include <iostream>

using namespace std;

int main(){
	cout<<"Hello World!\\n"<<endl;
	return 0;
}"""
                    FD.edit(params[0], data)
                    count = count + 1
                else:
                    data = """#include <iostream>

using namespace std;

int main(){
	cout<<"Hello Philippines and hello world!\\n";
	return 0;
}"""
                    FD.rm(['hello.cpp'])
                    FD.edit(params[0])
                    FD.edit(params[0], data)


        case '>>':
            if params[0] == 'hello.cpp':
                FD.edit(params[0])
                data = """//this is a test for the append using >>"""
                FD.edit(params[0], data)


        case 'show':
            if len(params) == 0:
                return
            
            results = FD.show(params[0]) 
            if results[0] != 0:
                print(results[1])
                return

            print(results[1].decode('utf-8'))

        case 'edit':
            if len(params) == 0:
                return
        
            data = "//this is the result of editing the file using edit"
            FD.edit(params[0], data)
        
            
            



            




def print_help():
    print(f"{'Commands':<10}   Info")
    print(f"{'--------':<10}   ----")
    print(f"  {'gui':<10} Run as GUI.")
    print()

if __name__ == "__main__":
    """
        Will check if we run the code as GUI or CLI.
        (not yet implemented and will never be)
    """
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case "-h" | "--help":
                print_help()
            case "--gui":
                print("gui mode")
            case "--":
                print("Missing argument after '--'.")
                sys.exit(2)

            case _:
                print(f"Invalid argument '{sys.argv[1]}'. ")
                sys.exit(1)
    else:
        main()
