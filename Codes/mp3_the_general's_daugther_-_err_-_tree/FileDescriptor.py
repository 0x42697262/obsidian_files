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

    def cd(self):
        pass


    def ls(self):
        pass


    def mv(self):
        pass

    def cp(self):
        pass

    def rm(self):
        pass

    def edit(self):
        pass

    def show(self):
        pass

    def whereis(self):
        pass
    




    def _resolve_path(self, path: str) -> DirectoryNode | None:
        """
            Resolve the given path to a node in the tree.
            Checks if the current directory or file exists.
        """

        if path == '/':
            return self.root

        # add .. and . traversing

        if path.startswith('/'):
            current_node    = self.root
        else:
            current_node    = self.pwd

        parts   = path.split('/')

        for part in parts:
            if not part:    # check if its an empty string
                continue

            found   = False
            for child in current_node.children:     # checks each child if current file or directory exists
                if child.name == part:
                    current_node    = child
                    found           = True
                    break
            if not found:
                return None


        return current_node

