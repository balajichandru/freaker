class Solution:
    def preorderTraversal(self, root):
        def preorder(root):
            print("Inside the sub preorder " )
            if not root:
                print("return function from preorder",arr,root)
                return
            print("Before appending a root val",arr)
            arr.append(root.val)
            print("appended a root val ",arr)
            print("bfre calling root left",arr)
            preorder(root.left)
            print("after calling root left",arr)
            print("bfre calling root right",)
            preorder(root.right)
            print("after calling root right",arr)
       
        arr =[]
        print("Inside the main preorder")
        preorder(root)
        return arr

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
    
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting preorder traversal
    result = Solution().preorderTraversal(root)

    # Displaying the preorder traversal result
    print("Preorder Traversal:", end=" ")
    # Output each value in the
    # preorder traversal result
    for val in result:
        print(val, end=" ")
    print()
