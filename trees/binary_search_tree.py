class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def insert(root: TreeNode, val):

    if not val:
        return TreeNode(val)

    current = root

    while current != None:

        if current.value > val:

            if current.left == None:
                current.left = TreeNode(val)
            else:
                current = current.left

        elif current.value < val:

            if current.right == None:
                current.right = TreeNode(val)
            else:
                current = current.right

        else:
            break

    return TreeNode(val)


def search(node: TreeNode, val):
    if not node:
        return False

    current = node
    while current:

        if current.value == val:
            return True

        if current.value > val:
            current = current.left
        else:
            current = current.right

    return False


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
            queue.append(current.right)

    return result


def deleteNode(node: TreeNode, val):
    if not node:
        return None

    if node.value > val:
        node.left = deleteNode(node.left, val)
    elif node.value < val:
        node.right = deleteNode(node.right, val)
    else:

        if not node.right and not node.left:
            return None
        elif not node.right:
            temp = node.left
            node.left = temp
            return temp
        elif not node.left:
            temp = node.right
            node.right = temp
            return temp
        else:
            temp = findMin(node.right)
            node.value = temp.value
            node.right = deleteNode(node.right, temp.value)

            return node

    return node


def findMin(node):
    if not node:
        return None

    while node.left:
        node = node.left

    return node


a = TreeNode(1)

insert(a, 2)
insert(a, 3)
insert(a, 4)
insert(a, -1)
insert(a, -2)

# print(levelOrderTraversal(a))
# print(search(a, 100))
# print(findMin(a).value)

print(deleteNode(a, 2).value)
print(search(a, 2))
