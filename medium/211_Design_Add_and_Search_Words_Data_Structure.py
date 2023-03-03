class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(i: int, node: TrieNode) -> bool:
            if i == len(word):
                return node.is_end

            char = word[i]

            if char == '.':
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True

                return False
            if char not in node.children:
                return False

            return dfs(i + 1, node.children[char])

        return dfs(0, self.root)


"""
Explanation:

Implement a TrieNode class that represents a node in the trie and has two properties: children, which is a dictionary of child nodes keyed by the characters in the word, and is_end, which is a boolean that indicates whether the node represents the end of a word.

Implement a WordDictionary class with the following two methods: addWord and search. The addWord method adds a word to the trie by iterating over its characters and creating new nodes as necessary. The last node in the word is marked as the end of the word by setting its is_end property to True.

The search method implements a DFS algorithm to search for a word in the trie. The DFS is implemented using a helper function dfs that takes two arguments: i, the index of the current character in the word, and node, the current node in the trie. The function returns a boolean indicating whether the word is found or not.

The dfs function checks if the curr index == the length of the word, in which case it returns the value of node.is_end, indicating whether the node represents the end of a word or not. If the current character in the word is a wildcard, the function iterates over all child nodes of the current node and recursively calls dfs with the next index and each child node. If any of the recursive calls return True, the function returns True. If no recursive call returns True, the function returns False. If the current character is not a wildcard, the function checks if the current node has a child node keyed by the character. If it doesn't, the function returns False. Otherwise, the function recursively calls dfs with the next index and the child node keyed by the character.

The search method calls the dfs function with index 0 and the root node of the trie and returns the boolean value returned by the dfs function.

Notes:

Time complexity: O(n) for add word, where n is the length of the input string. For search, time complexity is O(n) for well-defined word without wildcards and O((26 ^ n)) for undefined words, as we'll have to make up to 26 calls for each character in string.

Space complexity: O(n) for add word, O(1) for defined word search, and O(n) for undefined word search to keep recursion stack.
"""

wd = WordDictionary()

# Test 1: Test add single word
add_word = 'apple'
search_word = 'apple'
wd.addWord(add_word)
word_added = wd.search(search_word)
expected = True
assert word_added == expected, f"Expected {expected} but got {word_added}"

# Test 2: Test add multiple
add_word = 'apple'
search_word = 'apple'
add_word_2 = 'banana'
search_word_2 = 'banana'
wd.addWord(add_word)
wd.addWord(add_word_2)
word_added = wd.search(search_word)
expected = True
assert word_added == expected, f"Expected {expected} but got {word_added}"
word_added = wd.search(search_word_2)
expected = True
assert word_added == expected, f"Expected {expected} but got {word_added}"

# Test 3: Test search for word not added
search_word = 'cherry'
word_added = wd.search(search_word)
expected = False
assert word_added == expected, f"Expected {expected} but got {word_added}"

# Test 4: Test search with wildcard
add_word = 'strawberry'
search_word = 's.rawb.rry'
wd.addWord(add_word)
word_added = wd.search(search_word)
expected = True
assert word_added == expected, f"Expected {expected} but got {word_added}"

# Test 5: Search w/ max wildcard
add_word = 'pea'
search_word = '...'
wd.addWord(add_word)
word_added = wd.search(search_word)
expected = True
assert word_added == expected, f"Expected {expected} but got {word_added}"
