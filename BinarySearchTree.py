
class TreeNode:
    def __init__(self,data,parent):
        self.data=data
        self.parent=parent
        self.leftChild=None
        self.rightChild=None


class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=TreeNode(data=data,parent=None)
        else:
            self.insertNode(data,self.root)

    def insertNode(self,data,node):

        if(data < node.data):

            if (node.leftChild):
                self.insertNode(data,node.leftChild)
            else:
                node.leftChild=TreeNode(data,node )
        else:
            if(node.rightChild):
                self.insertNode(data,node.rightChild)
            else:
                node.rightChild=TreeNode(data,node)


    def traverseInorder(self):
        if self.root:
            self.traversalInorder(self.root)
        else:
            print(self.root)

    def traversalInorder(self,node):
        if node.leftChild:
            self.traversalInorder(node.leftChild)
        print(node.data)
        if node.rightChild:
            self.traversalInorder(node.rightChild)


    def findMax(self):
        if(self.root):
            self.finMax(self.root)
        else:
            print("has no root element")
    def finMax(self,node):

        if(node.rightChild):
            self.finMax(node.rightChild)
            print(node.rightChild)


        return(node.data)
bst=BinarySearchTree()
bst.insert(23)
bst.insert(30)
bst.insert(50)
bst.insert(3)
bst.insert(99)
bst.insert(10)
bst.traverseInorder()
print("Max :",bst.findMax())



