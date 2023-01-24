"""
    Source: https://github.com/KrulYuno/obsidian_files/tree/master/Codes/mp3_the_general's_daugther_-_err_-_tree
"""

import sys
from FileDescriptor import FileDescriptor
from GeneralTreeNode import DirectoryNode, FileNode


def main():

    root    = DirectoryNode('/') 
    cmd     = FileDescriptor(root)
    dirs    = ['bin', 'dev', 'home', 'opt', 'root', 'sbin', 'sys', 'usr',
               'boot', 'etc', 'mnt', 'proc', 'run', 'srv', 'tmp', 'var']
    for name in dirs:
        cmd.mkdir(name)


    cmd.root.insert(FileNode("hello.txt", root))
    cmd.root.insert(FileNode("hellr.txt", root))
    cmd.root.insert(FileNode("hellrar.txt", root))
    cmd.mkdir("/home/birb")
    print(cmd.edit("/home/birb/asfd"))
    print(cmd.edit("/home/birb/asfd", "sadf"))
    print(cmd.show("/home/birb/asfd/asdf"))
    # cmd.edit("test1.txt", "osijdfoisdjfo")
    # print(cmd.show("test1.txt"))
    print(cmd.ls("/home"))




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
