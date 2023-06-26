class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        serialized = ','.join(result)

        return serialized

    def deserialize(self, data):
        data = data.split(',')
        index = 0

        def dfs():
            nonlocal index

            if data[index] == "N":
                index += 1
                return None

            root_val = int(data[index])
            root = TreeNode(root_val)
            index += 1
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()

"""
Explanation:

The serialize method performs a DFS traversal of the tree. It starts by initializing an empty result list. Then, it calls a recursive helper function dfs to traverse the tree. In the dfs function, if the current node is null, it appends the string "N" to the result list. Otherwise, it converts the node's value to a string and appends it to the result list. It then recursively calls dfs for the left and right children of the current node. Finally, it returns the serialized tree by joining the elements of the result list using commas.

The deserialize method takes a serialized string as input. It splits the string by commas to obtain a list of values. It initializes an index variable to keep track of the current position in the list. It then defines a recursive helper function dfs to reconstruct the binary tree. In the dfs function, it checks if the current value is "N", indicating a null node. If so, it increments the index and returns None. Otherwise, it converts the current value to an integer and creates a new node w/ that value. It then increments the index and recursively calls dfs to set the left and right children of the current node. Finally, it returns the reconstructed binary tree.

Notes:

Time complexity: O(n) for both serialization and deserialization

Space complexity: O(n) for both storing the serialized string and deserialized tree, as well as the recursion stack.
"""
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# Test Case 1: Empty tree
codec = Codec()
root = None
serialized = codec.serialize(root)
expected_serialized = "N"
assert serialized == expected_serialized, f"Expected '{expected_serialized}' but got '{serialized}'"

deserialized = codec.deserialize(serialized)
assert is_same_tree(deserialized, root), f"Expected {root} but got {deserialized}"

# Test Case 2: Single node
codec = Codec()
root = TreeNode(10)
serialized = codec.serialize(root)
expected_serialized = "10,N,N"
assert serialized == expected_serialized, f"Expected '{expected_serialized}' but got '{serialized}'"

deserialized = codec.deserialize(serialized)
assert is_same_tree(deserialized, root), f"Expected {root} but got {deserialized}"

# Test Case 3: Balanced binary tree
codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
serialized = codec.serialize(root)
expected_serialized = "1,2,4,N,N,5,N,N,3,6,N,N,7,N,N"
assert serialized == expected_serialized, f"Expected '{expected_serialized}' but got '{serialized}'"

deserialized = codec.deserialize(serialized)
assert is_same_tree(deserialized, root), f"Expected {root} but got {deserialized}"

# Test Case 4: Skewed binary tree
codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
serialized = codec.serialize(root)
expected_serialized = "1,2,4,N,N,5,N,N,N"
assert serialized == expected_serialized, f"Expected '{expected_serialized}' but got '{serialized}'"

deserialized = codec.deserialize(serialized)
assert is_same_tree(deserialized, root), f"Expected {root} but got {deserialized}"
