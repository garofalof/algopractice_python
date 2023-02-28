from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        note_count = Counter(ransomNote)
        mag_count = Counter(magazine)

        for char in note_count:
            if note_count[char] > mag_count[char]:
                return False

        return True


"""
Explanation:

Initialize dictionary note_count and mag_count to store the frequency of each character in the magazine. Iterate through each character in note_count, checking if the character frequency in note_count > the character frequency in mag_count. If so, return False. If the entire ransom note can be constructed from the magazine, return True.

Notes:

Time Complexity: O(m + n), where m and n are the lengths of the two input strings.
Space Complexity: O(1), as we never store more than 26 characters in the hashmap.
"""

# Test 1: Note length > magazine length
note = 'goodbye'
magazine = 'hello'
canConstruct = Solution().canConstruct(note, magazine)
assert canConstruct == False, f"Expected False but got {canConstruct}"

# Test 2: Can construct note from magazine
note = 'aa'
magazine = 'aab'
canConstruct = Solution().canConstruct(note, magazine)
assert canConstruct == True, f"Expected True but got {canConstruct}"

# Test 3: Cannot construct note from magazine
note = 'ac'
magazine = 'aab'
canConstruct = Solution().canConstruct(note, magazine)
assert canConstruct == False, f"Expected False but got {canConstruct}"

# Test 4: Multiple instances of note in magazine
note = 'apple'
magazine = 'apple pear apple'
canConstruct = Solution().canConstruct(note, magazine)
assert canConstruct == True, f"Expected True but got {canConstruct}"
