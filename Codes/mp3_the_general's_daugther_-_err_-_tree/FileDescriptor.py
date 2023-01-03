from GeneralTreeNode import (DirectoryNode, FileNode)


class FileDescriptor:
    def __init__(self, root: DirectoryNode) -> None:
        self.root   = root
        self.pwd    = root

    def mkdir(self, path: str) -> int:
        """
            Creates a new child node.
            Sets the parent of the child node to self.
        """
        
        parent, name    = self._resolve_parent_and_name(path)
        if not parent:
            return 2

        if any(child.name == name for child in parent.children):
            return 1


        parent.insert(DirectoryNode(name, parent))
        return 0

    def rmdir(self, path: str) -> int:
        """
            Remove empty directories.
        """

        node    = self._resolve_path(path)

        # Disallow deletion of / (root).
        if node == self.root:
            return 4

        # If path is current directory
        if node == self.pwd and self.pwd.parent is not None:
            self.pwd = self.pwd.parent

        # Guard Clauses 
        ## If None
        if not node:
            return 2

        ## If not empty
        if len(node.children) > 0:
            return 1

        ## Delete Success
        self.pwd.remove(node)
        return 0


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
    

    def _pwd(self) -> str:
        directories     = list()
        cwd             = self.pwd
        while cwd != self.root:
            directories.insert(0, cwd.name)
            cwd = cwd.parent
        
        return '/' + '/'.join(directories)


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

    def _resolve_parent_and_name(self, path: str) -> tuple[DirectoryNode | None, str]:
        """
            Resolve the parent node and name for the file or directory at the given path.
        """

        parts   = path.split('/')
        name    = parts[-1]
        if not name:
            return None, ''

        if len(parts) == 1:
            return self.pwd, name

        parent_path = '/'.join(parts[:-1])
        parent = self._resolve_path(parent_path)

        return parent, name
