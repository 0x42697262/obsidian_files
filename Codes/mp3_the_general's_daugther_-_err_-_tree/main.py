"""


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
