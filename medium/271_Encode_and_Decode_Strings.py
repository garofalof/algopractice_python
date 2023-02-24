from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for s in strs:
            encoded += f"[{len(s)}]{s}"

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            str_len = 0

            while s[i] != ']':
                if s[i].isdigit():
                    str_len = str_len * 10 + int(s[i])

                i += 1

            start = i + 1
            end = start + int(str_len)
            result.append(s[start:end])
            i = end

        return result


"""
Explanation:

Define a class called Codec with two methods: encode and decode. Encode iterates through the list of strings, computes the length of each string, and concatenates the length and string into a single string, surrounded by square brackets. The resulting string is the encoded version of the input list. Decode iterates through the encoded string, extracting the length of each string and the string itself by searching for the square brackets. It then appends the decoded string to a list, and continues iterating through the encoded string until all strings have been decoded. The resulting list is the original list of strings that was encoded.

Notes:

Time complexity: O(n) for encode and decode.

Space complexity: O(n), where n is the total number of characters in the input. This is because in the worst case, the encoded string could contain all characters in the input list of strings plus additional bracket characters, and the decoded result could be a list of all the strings in the input list.
"""

# Test 1: Single element in list, empty
codec = Codec()
list = ['']
encoded = codec.encode(list)
decoded = codec.decode(encoded)
expected = list
assert decoded == expected, f"Expected {expected} but got {decoded}"

# Test 2: Single element in list, not empty
codec = Codec()
list = ['abc']
encoded = codec.encode(list)
decoded = codec.decode(encoded)
expected = list
assert decoded == expected, f"Expected {expected} but got {decoded}"

# Test 3: Two elements in list, one empty
codec = Codec()
list = ['abc', '']
encoded = codec.encode(list)
decoded = codec.decode(encoded)
expected = list
assert decoded == expected, f"Expected {expected} but got {decoded}"

# Test 4: Two elements in list, not empty
codec = Codec()
list = ['abc', 'def']
encoded = codec.encode(list)
decoded = codec.decode(encoded)
expected = list
assert decoded == expected, f"Expected {expected} but got {decoded}"

# Test 5: Multiple elements in list, only letters
codec = Codec()
list = ['hello', 'beautiful', 'world']
encoded = codec.encode(list)
decoded = codec.decode(encoded)
expected = list
assert decoded == expected, f"Expected {expected} but got {decoded}"

# Test 6: Multiple elements in list, alphanumeric
codec = Codec()
list = ['hello5', 'beautiful', '1world']
encoded = codec.encode(list)
decoded = codec.decode(encoded)
expected = list
assert decoded == expected, f"Expected {expected} but got {decoded}"

# Test 7: Multiple elements in list, ASCII characters
codec = Codec()
list = ['hell!5@', 'beautiful^12', '1world_po@']
encoded = codec.encode(list)
decoded = codec.decode(encoded)
expected = list
assert decoded == expected, f"Expected {expected} but got {decoded}"
