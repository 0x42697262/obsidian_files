"""
    Source: https://github.com/KrulYuno/obsidian_files/tree/master/Codes/mp3_the_general's_daugther_-_err_-_tree
"""

import sys
from FileDescriptor import FileDescriptor
from GeneralTreeNode import DirectoryNode


def main():

    root    = DirectoryNode('/') 
    cmd     = FileDescriptor(root)
    dirs    = ['bin', 'dev', 'home', 'opt', 'root', 'sbin', 'sys', 'usr',
               'boot', 'etc', 'mnt', 'proc', 'run', 'srv', 'tmp', 'var']
    for name in dirs:
        cmd.mkdir(name)

    cmd.cd("home")
    cmd.mkdir("birb")
    cmd.mkdir("chicken")
    cmd.mkdir("neko")
    cmd.mkdir("naku")
    
    cmd.cd("birb")
    cmd.mkdir("/home/birb/Downloads")
    cmd.mkdir("/home/birb/.config")
    cmd.mkdir("/home/birb/.local")
    cmd.mkdir("/home/birb/.share")
    cmd.mkdir("/home/birb/.cache")

    cmd.cd("..")
    cmd.mkdir("birb/Stuffs")

    cmd.cd("birb")
    # print("contents:", cmd.ls("*"))
    cmd.mkdir("hello.docx")
    cmd.mkdir("there.docx")
    cmd.mkdir("fren.docx")
    cmd.mkdir("/home/neko/hello1.docx")
    cmd.mkdir("/home/neko/there2.docx")
    cmd.mkdir("/home/neko/fren3.docx")
    cmd.cd("../neko")
    # print(cmd.ls("*.docx"))

    cmd.cd("/home/birb/Downloads")
    cmd.mkdir("temp")
    cmd.mkdir("xampp")
    cmd.mkdir("idm")
    cmd.mkdir("net")
    # cmd.cd("..")
    # cmd.ls("/home/*/*.docx")

    # print(    cmd._resolve_path_wildcard(['/home/n*k*//*.docx', '/home/*//*.docx']))
    # cmd._resolve_path_wildcard(['/home/neko//*.docx', '/home/naku//*.docx', '/home/birb//*.docx', '/home/chicken//*.docx'])
    # print(cmd._resolve_path_wildcard(['.']))
    # print(cmd.ls("/home/*/*"))
    # print(cmd.ls('/home/b*rb'))
    # print(cmd.ls("/*/*/"))

    cmd.cd("/home/birb/Downloads")
    print(cmd._pwd(), cmd.ls(""))
    cmd.mv("temp", "xampp")
    cmd.mv("net", "xampp/.")
    cmd.mv("idm", "xampp/sdf/shit")
    print(cmd._pwd(), cmd.ls(""))
    print("xampp:", cmd.ls("xampp"))
    print(    cmd._wildcard_handler(["/home/*/", "/home", "/home/*/Downloads/*.docx", "/home/*/Downloads/*", "/home/*/Downloads/*"]))
    


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
