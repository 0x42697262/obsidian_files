"""
    Source: https://github.com/KrulYuno/obsidian_files/tree/master/Codes/mp3_the_general's_daugther_-_err_-_tree
"""

import sys
from FileDescriptor import FileDescriptor
from GeneralTreeNode import (DirectoryNode, FileNode)


def main():
    """
        Will check if we run the code as GUI or CLI.
    """

    root    = DirectoryNode('/') 
    cmd     = FileDescriptor(root)
    cmd.mkdir("etc")
    cmd.mkdir("home")
    cmd.mkdir("bin")

    for _ in cmd.pwd.children:
        print(_.name)

    cmd.pwd = cmd.pwd.children[1]
    print()
    cmd.mkdir("birb")
    cmd.mkdir("jean")
    



def print_help():
    print(f"{'Commands':<10}   Info")
    print(f"{'--------':<10}   ----")
    print(f"  {'gui':<10} Run as GUI.")
    print()

if __name__ == "__main__":
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
