from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs(0, len(nums) - 1, nums)

    def dfs(self, l: int, r: int, nums: List[int]) -> Optional[TreeNode]:
        if l > r:
            return None

        mid = (l + r) // 2
        root = TreeNode(nums[mid])

        root.left = self.dfs(l, mid - 1, nums)
        root.right = self.dfs(mid + 1, r, nums)

        return root

"""
Explanation:

The sortedArrayToBST method takes the sorted array nums as input and returns the root node of the resulting BST. It calls the dfs method, passing the start and end indices to the function, as well as the nums list.

The dfs method is a helper function that performs the actual conversion. If the start index > the end index, it means that the current subtree is empty. In this case, the method returns None. Otherwise, it calculates the middle index. It creates a new node w/ the value at the nums[mid], representing the root of the current subtree.The method then recursively calls dfs for the left subtree, passing the start index and the current mid - 1 as the end index. Similarly, it recursively calls dfs for the right subtree, passing mid + 1 as the start index and the end index.

Finally, it assigns the left and right subtrees obtained from the recursive calls to the root.left and root.right attributes, respectively. The dfs method returns the root of the constructed BST.

Notes:

Time complexity: O(n), where n is the length of the nums array. Each element in the array is visited once to construct the corresponding tree node, resulting in a linear time complexity.

Space complexity: O(n), as the recursion depth can reach n depth in the worst case scenario, and each recursive call consumes additional memory on the call stack. Additionally, the space required for the resulting BST is also proportional to the number of elements in the nums array.
"""
def is_height_balanced(root):
    def get_height(node):
        if node is None:
            return 0
        return max(get_height(node.left), get_height(node.right)) + 1

    def is_balanced_helper(node):
        if node is None:
            return True

        left_height = get_height(node.left)
        right_height = get_height(node.right)

        if abs(left_height - right_height) > 1:
            return False

        return is_balanced_helper(node.left) and is_balanced_helper(node.right)

    return is_balanced_helper(root)

# Test Case 1: Single element
nums = [0]
solution = Solution()
result = solution.sortedArrayToBST(nums)
expected = True
assert is_height_balanced(result) == expected, f"Expected {expected} but got {result}"

# Test Case 2: Two elements
nums = [0, 1]
solution = Solution()
result = solution.sortedArrayToBST(nums)
expected = True
assert is_height_balanced(result) == expected, f"Expected {expected} but got {result}"

# Test Case 3: Even number of elements
nums = [0, 1, 3, 6]
solution = Solution()
result = solution.sortedArrayToBST(nums)
expected = True
assert is_height_balanced(result) == expected, f"Expected {expected} but got {result}"

# Test Case 4: Odd number of elements
nums = [0, 1, 3, 6, 10]
solution = Solution()
result = solution.sortedArrayToBST(nums)
expected = True
assert is_height_balanced(result) == expected, f"Expected {expected} but got {result}"

# Test Case 5: Large number of elements
nums = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
solution = Solution()
result = solution.sortedArrayToBST(nums)
expected = True
assert is_height_balanced(result) == expected, f"Expected {expected} but got {result}"