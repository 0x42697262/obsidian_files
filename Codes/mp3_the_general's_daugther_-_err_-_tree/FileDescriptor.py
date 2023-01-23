"""
    mkdir: does not support multiple arguments for directory creation
    rmdir: does not support multiple arguments for directory deletion

    these can easily be added tho, but not a priority
"""

from GeneralTreeNode import (DirectoryNode, FileNode)
import fnmatch, re
import Errors

class FileDescriptor:
    def __init__(self, root: DirectoryNode) -> None:
        self.root   = root
        self.pwd    = root





    def mkdir(self, path: str) -> tuple:
        """
            Creates a new child node.
            Sets the parent of the child node to self.
        """
        
        parent, name    = self._resolve_parent_and_name(path)

        if not parent:
            return 2,Errors.errors['mkdir'][2].replace('{}', path)

        if any(child.name == name for child in parent.children):
            return 1,Errors.errors['mkdir'][1].replace('{}', name)



        parent.insert(DirectoryNode(name, parent))

        return 0, Errors.errors['mkdir'][0]





    def rmdir(self, path: str) -> tuple:
        """
            Remove empty directories.
        """

        node    = self._resolve_path(path)

        if type(node) is FileNode:
            return 5, Errors.errors['rmdir'][5].replace('{}', path)

        if node == self.root:
            return 4, Errors.errors['rmdir'][4]

        if not node:
            return 2, Errors.errors['rmdir'][2].replace('{}', path)

        if len(node.children) > 0:
            return 1, Errors.errors['rmdir'][1].replace('{}', path)



        # If path is current directory
        if node == self.pwd and self.pwd.parent is not None:
            self.pwd = self.pwd.parent

        ## Delete Success
        self.pwd.remove(node)

        return 0, Errors.errors['rmdir'][0]






    def cd(self, path: str) -> tuple:
        """
            Change the working directory.
        """

        to_path_node    = self._resolve_path(path)

        if not to_path_node:
            return 1, Errors.errors['cd'][1].replace('{}', path)

        if type(to_path_node) is FileNode:
            return 2, Errors.errors['cd'][2].replace('{}', path)



        self.pwd    = to_path_node

        return 0, Errors.errors['cd'][0]






    def ls(self, path: str) -> dict | tuple | None:
        """
            List directory contents.
        """

        # make sure the path is free from any wildcards
        paths   = self._wildcard_handler([path])
        # we get its nodes
        cwds    = [self._resolve_path(p) for p in paths]

        # path does not exist
        if len(cwds) == 1 and cwds[0] == None:
            return 1, Errors.errors['ls'][1].replace('{}', path)

        results     = dict()

        for cwd in cwds:
            if type(cwd) is DirectoryNode:
                results[self._pwd(cwd)]  = list()

        for cwd in cwds:
            if type(cwd) is DirectoryNode:
                for child in cwd.children:
                    results[self._pwd(cwd)].append(child.name)

        return results






    def mv(self, sources: list, destination: str) -> list | tuple:
        """
            Move (rename) files.
        """

        errors = list()
        
        # note that `mv` command can take multiple files and directories as argument as sources
        # then its very last argument is the destination 
        destination_node    = self._resolve_path(destination)
        if not destination_node and len(sources) > 1:
            return 1, Errors.errors['mv'][1].replace('{}', destination)

        for source_wildcard in sources:
            source_paths    = self._wildcard_handler([source_wildcard])
            source_nodes    = [self._resolve_path(s) for s in source_paths]
            
            if len(source_paths) == 0:
                errors.append((1, Errors.errors['mv'][1].replace('{}', source_wildcard)))
                continue

            if source_wildcard == destination:
                errors.append((2, Errors.errors['mv'][2].replace('{}', source_wildcard)))
                continue

            if type(destination_node) is FileNode:
                errors.append((3, Errors.errors['mv'][3].replace('{destination}', destination).replace('{source}', source_wildcard)))
                continue

            # there is one nefty case where we should avoid and that is a wildstar in destination directory
            # will not take care of it

            # move file or directory
            # else, rename
            if destination_node:
                for clean_source in source_nodes:
                    clean_source.parent.children.remove(clean_source)
                    clean_source.parent  = destination_node
                    clean_source.parent.insert(clean_source)
            else:
                if len(source_nodes) > 1:
                    errors.append((1, Errors.errors['mv'][1].replace('{}', destination)))
                    continue

                # once this branch is executed, we know that the <destination> of
                # path/<parent>/<destination> does not exist
                # 
                # so we take its parent folder and check if that also exists, otherwise
                # return a file directory not exist error

                for clean_source in source_nodes:
                    destination_name    = destination.split('/')[-1]                    # <destination>
                    parent_path         = destination.replace(destination_name, '')     # path/<parent>
                    parent_node         = self._resolve_path(parent_path)               # <parent> node
                    clean_source.parent.children.remove(clean_source)                   # remove source node from directory
                    clean_source.parent  = parent_node                                  # set source node parent
                    clean_source.parent.insert(clean_source)                            # add source node to parent children
                    clean_source.name    = destination_name                             # rename

            
        return errors



    def cp(self):
        pass

    def rm(self):
        pass

    def edit(self, filename: str):
        pass

    def show(self):
        pass

    def whereis(self):
        pass
    

    def _pwd(self, node: DirectoryNode | FileNode = None) -> str:
        """
            Returns current working directory.
            Can be used to get full path of a node.
        """

        directories     = list()
        cwd             = self.pwd if node is None else node
        while cwd != self.root:
            directories.insert(0, cwd.name)
            cwd = cwd.parent
        
        return '/' + '/'.join(directories)



    def _resolve_path(self, path: str) -> DirectoryNode | FileNode | None:
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



    def _wildcard_handler(self, paths: list) -> list:
        """
            Take a list of paths and check if that list contains a wildcard `*`.
            Check each path in paths if a wildcard exists then add it to path queues.
            Attempt to convert the `*` to proper paths. Only convert 1 wildcard from the left.
            Add the converted `*` to the cleaned paths. Check if at least one of the path 
            contains a wildcard `*`.

            Return a list of fully cleaned path, without any wildcards.
        """

        cleaned_paths   = list()

        for path in paths:
            if '*' in path:
                # find all wildcards as a list
                # will be used for string substitution later on
                wildcards           = re.findall(r'[^\\^/^\s]*\*[^\\^/^\s]*', path)
                # find the first * in path
                wildcard_index      = path.find('*')
                # get substring until *
                wildcard_substring  = path[:wildcard_index]
                # get its node
                wildcard_node       = self._resolve_path(wildcard_substring)
                # check if the wildcard node exists, add all its children to list
                # to be checked for matching paths
                if wildcard_node:
                    # add the child's path to children list
                    children        = [wildcard_substring + child.name for child in wildcard_node.children]
                    # match only the ones with a wildcard
                    matches         = fnmatch.filter(children, wildcard_substring+wildcards[0])
                    # get back on this issue where the stuffs gets duplicated, eat first

                    # iterate the list then append the matched child + the remaining path string
                    for match in matches:
                        tmp     = path
                        cleaned_paths.append(tmp.replace(wildcard_substring+wildcards[0], match, 1))

            else:
                cleaned_paths.append(path)
                
        # remove duplicates in cleaned paths
        cleaned_paths   = list(dict.fromkeys(cleaned_paths))
        # check if wildcard `*` still exists in a list, then recursively call the function if it does
        wildcard_bool   = False
        for cp in cleaned_paths:
            wildcard_bool   = '*' in cp
            if wildcard_bool:
                # call the function
                cleaned_paths   = self._wildcard_handler(cleaned_paths)
                break

        return cleaned_paths



