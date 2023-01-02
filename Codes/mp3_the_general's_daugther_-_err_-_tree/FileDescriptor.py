from GeneralTreeNode import (DirectoryNode, FileNode)


class FileDescriptor:
    def __init__(self, root: DirectoryNode) -> None:
        self.root   = root
        self.pwd    = root

    def mkdir(self, name: str):
        """
            Creates a new child node.
            Sets the parent of the child node to self.
        """

        self.pwd.insert(DirectoryNode(name, self.pwd))

    def rmdir(self, name: str) -> bool:
        """
            Searches for the node, removes if found and returns True, otherwise False.
        """

        node = self.pwd.search(name)
        if node:
            self.pwd.remove(node)
            return True
        
        return False

