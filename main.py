import uuid

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children=[]
        self.parent=None

    def AddChild(self,child):
        child.parent=self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def printTree(self):
        spaces = ' '*self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree()

def treeBuilder():
    root=TreeNode("Electronics")
    laptop=TreeNode("Laptop")
    laptop.AddChild(TreeNode("Mac"))
    laptop.AddChild(TreeNode("Surface"))
    laptop.AddChild(TreeNode("Thinkpad"))

    cellphone=TreeNode("cellphone")
    cellphone.AddChild(TreeNode("iPhone"))
    cellphone.AddChild(TreeNode("google pixel"))
    cellphone.AddChild(TreeNode("vivo"))

    tv=TreeNode("tv")
    tv.AddChild(TreeNode("samsung"))
    tv.AddChild(TreeNode("LG"))

    root.AddChild(laptop)
    root.AddChild(cellphone)
    root.AddChild(tv)

    return root

if __name__ == "__main__":
    root=treeBuilder()
    root.printTree()

    print(type(str(uuid.uuid1())))

    print("\n\n END OF LINE")

#
