def getHeight(self,root):
        if root == None:
            height = -1
        else:
            height = max(1+self.getHeight(root.left),1+self.getHeight(root.right))
        return height