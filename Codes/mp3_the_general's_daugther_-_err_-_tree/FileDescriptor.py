from GeneralTreeNode import (DirectoryNode, FileNode)
import fnmatch, re
import itertools


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

        # Guard Clauses
        # Directory already exist 
        if not parent:
            return 2

        ## Directory not exist
        if any(child.name == name for child in parent.children):
            return 1

        # Sucess, make directory
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
        """
            Change the working directory.
        """

        to_path_node    = self._resolve_path(path)
        if to_path_node:
            self.pwd    = to_path_node
            return True
        else:
            return False






    def ls(self, path: str) -> list | int | dict | None:
        """
            List directory contents.

            Buggy, incomplete, please fix
        """

        if '*' in path:
            directories     = self._resolve_path_wildcard([path])
            # results = dict()
            # if directories:
            #     for d in directories:
            #         results[d] = list()
            #         r   = self._resolve_path(d)
            #         if type(r) is DirectoryNode:
            #             results[d].append(((self.ls(d))))
            #     
            #     if len(results) > 0:
            #         return results


            return directories

        else:
            cwd     = self._resolve_path(path)

            # Guard Clauses
            ## Directory not exist
            if not cwd:
                return 1

            ## Show contents
            contents    = [child.name for child in cwd.children] 

            # if no arguments provided
            if not path: 
                return contents 


            name        = path.split('/')[-1]
            if cwd == self.pwd:
                name    = '*'
            else:
                name    = '*'

            # print(name, cwd.name, path.split('/'), path, contents)
            return fnmatch.filter(contents, name) 



    def mv(self, source, destination):
        """
            Move (rename) files.
        """

        
        source_node         = self._resolve_path(source)
        destination_node    = self._resolve_path(destination)

        if not source_node:
            return 1    # no such file or directory

        print(source, "->", destination)

        # Check if path exists, if not simply rename the source to destination.
        if destination_node:
            # print(source_node.parent.children)
            source_node.parent.children.remove(source_node)
            source_node.parent  = destination_node
            source_node.parent.insert(source_node)
        else:
            # once this branch is executed, we know that the <destination> of
            # path/<parent>/<destination> does not exist
            # 
            # so we take its parent folder and check if that also exists, otherwise
            # return a file directory not exist error

            destination_name    = destination.split('/')[-1]                    # <destination>
            parent_path         = destination.replace(destination_name, '')     # path/<parent>
            parent_node         = self._resolve_path(parent_path)               # <parent> node


            # check if parent node exists, return error 1 file/directory not exist if not
            # set the parent of the source node to parent_node then do magic
            if parent_node:
                source_node.parent.children.remove(source_node)     # remove source node from directory
                source_node.parent  = parent_node                   # set source node parent
                source_node.parent.insert(source_node)              # add source node to parent children
                source_node.name    = destination_name              # rename
            else:
                return 1
            


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



    def _resolve_path_wildcard(self, paths: list) -> list | None:
        contents    = list()
        for path in paths:
            wildcards   = re.findall(r'[^\\^/^\s]*\*[^\\^/^\s]*', path)
            parent      = DirectoryNode
            for wc in wildcards:
                find    = path[:path.find(wc)]
                parent  = self._resolve_path(find)
                if parent:
                    matches     = fnmatch.filter(self.ls(find), wc)
                    if len(matches) > 0:
                        for p in matches:
                            tmp     = path
                            contents.append(tmp.replace(wc, p, 1))
        
        contents    = list(dict.fromkeys(contents))
        for c in contents:
            if '*' in c:
                return self._resolve_path_wildcard(contents)
        return contents
