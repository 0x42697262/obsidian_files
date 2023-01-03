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

    def cd(self, path: str) -> bool:
        to_path_node    = self._resolve_path(path)
        if to_path_node:
            self.pwd    = to_path_node
            return True
        else:
            return False


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

        match path:
            case '/':
                return self.root
            case '.':
                return self.pwd
            case '..':
                return self.pwd.parent if self.pwd != self.root else self.root


        if path.startswith('/'):
            current_node    = self.root
        else:
            current_node    = self.pwd

        parts   = path.split('/')

        for part in parts:
            if not part:    # check if its an empty string
                continue
            
            match part:
                case '..':
                    current_node     = current_node.parent if current_node != self.root else self.root
                case '.':
                    continue
                case _:
                    found   = False
                    for child in current_node.children:     # checks each child if current file or directory exists
                        if child.name == part:
                            current_node    = child
                            found           = True
                            break
                    if not found:
                        return None


        return current_node

