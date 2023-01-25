
class GeneralTreeNode:
    def __init__(self, name: str, parent = None) -> None:
        self.children   = list()
        self.parent     = parent
        self.name       = name

    def delete(self, node) -> None:
        node.parent.children.remove(node)
        node.parent     = None
        node.children   = None
        node            = None




class DirectoryNode(GeneralTreeNode):
    def __init__(self, name: str, parent = None) -> None:
        super().__init__(name, parent)
        

    def insert(self, child: GeneralTreeNode):
        """
            Appends child to the current node or parent node.
        """

        self.children.append(child)

    def remove(self, node):
        """
           Removes node.
           Note: Python has its own garbage collection so the node gets deleted.
        """
        
        node.parent.children.remove(node)   # remove node from parent's children
        node.parent     = None              # remove reference to parent
        node.children   = None              # remove references to children
        node            = None

        

    def search(self, name: str):
        """
           Recursively search for a child node with a given name. 
        """ 

        for child in self.children:
            if child.name == name:
                return child
            result = child.search(name)
            if result:
                return result

        return None





class FileNode(GeneralTreeNode):
    def __init__(self, name: str, parent = None) -> None:
        super().__init__(name, parent)

        self.data: bytearray    = bytearray()


    def append(self, contents: str):
        self.data.extend(bytes(contents, 'utf-8'))
        self.data.extend(bytes('\n', 'utf-8'))
        


