class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def preOrderTraversal(node: TreeNode):
    if not node:
        return

    print(node.value)
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)


def inOrderTraversal(node: TreeNode):
    if not node:
        return

    inOrderTraversal(node.left)
    print(node.value)
    inOrderTraversal(node.right)


def postOrderTraversal(node: TreeNode):
    if not node:
        return

    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.value)


def levelOrderTraversal(node: TreeNode):
    if not node:
        return []

    queue = []
    result = []
    queue.append(node)

    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            current.append(current.right)

    return result


# Tree includes
# def treeIncludes(root, target):

#     if not root:
#         return False

#     queue = [root]

#     while queue:
#         current = queue.pop(0)

#         if current.value == target:
#             return True

#         if current.left:
#             queue.append(current.left)

#         if current.right:
#             queue.append(current.right)

#     return False


def treeIncludes(root, target):
    if not root:
        return False

    if root.value == target:
        return True

    return treeIncludes(root.left, target) or treeIncludes(root.right, target)


a = TreeNode("a")
b = TreeNode("b")
c = TreeNode("c")
d = TreeNode("d")
e = TreeNode("e")
f = TreeNode("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(treeIncludes(a, "a"))

# Tree sum

# def treeSum(root: TreeNode):
#     if not root:
#         return 0
#     return root.value + treeSum(root.left) + treeSum(root.right)


def treeSum(root: TreeNode):
    if not root:
        return 0

    queue = [root]
    totalSum = 0

    while queue:
        current = queue.pop(0)
        totalSum += current.value

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return totalSum


a = TreeNode(3)
b = TreeNode(11)
c = TreeNode(4)
d = TreeNode(4)
e = TreeNode(2)
f = TreeNode(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(treeSum(a))


# Tree min
# def treeMinValue(root: TreeNode):
#       queue = [root]
#     smallest = float("inf")
#     while queue:
#         current = queue.pop()

#         if current.value < smallest:
#             smallest = current.value

#         if current.left:
#               queue.append(current.left)

#         if current.right:
#               queue.append(current.right)

#     return smallest


# def treeMinValue(root: TreeNode):
#     queue = [root]
#     smallest = float("inf")
#     while queue:
#         current = queue.pop(0)

#         if current.value < smallest:
#             smallest = current.value

#         if current.left:
#             queue.append(current.left)

#         if current.right:
#             queue.append(current.right)

#     return smallest


def treeMinValue(root: TreeNode):
    if not root:
        return float("inf")

    leftMin = treeMinValue(root.left)
    rightMin = treeMinValue(root.right)

    return min(root.value, leftMin, rightMin)


print(treeMinValue(a))

a = TreeNode(5)
b = TreeNode(11)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(2)
f = TreeNode(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# max root to leaf path sum
def maxPathSum(root: TreeNode):
    if not root:
        return float("-inf")
    if root.left == None and root.right == None:
        return root.value
    maxChild = max(maxPathSum(root.left), maxPathSum(root.right))
    return root.value + maxChild


print(maxPathSum(a))
