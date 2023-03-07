from collections import defaultdict
from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        merged = sorted(zip(timestamp, username, website))
        user_entries = defaultdict(list)

        def create_three_sequences(sites):
            size = len(sites)
            seqs = set()

            for i in range(size - 2):
                for j in range(i + 1, size - 1):
                    for k in range(j + 1, size):
                        seq = f"{sites[i]},{sites[j]},{sites[k]}"
                        seqs.add(seq)

            return seqs

        for _, user, site in merged:
            user_entries[user].append(site)

        patterns = defaultdict(int)

        for sites in user_entries.values():
            seqs = create_three_sequences(sites)

            for seq in seqs:
                patterns[seq] += 1

        max_count = 0
        result = ''

        for seq, count in patterns.items():
            if count > max_count:
                max_count = count
                result = seq
            elif count == max_count and seq < result:
                result = seq

        return result.split(',')


"""
Explanation:

First merge the three input lists into a single list of tuples sorted by timestamp. Then, group the websites visited by each user into a dictionary using the username as the key. Next, create a function that generates all possible three-sequence patterns for a given list of websites. Iterate over the user entries and generate all the possible three-sequence patterns for each user. Keep track of the count of each pattern in a dictionary. Finally, find the pattern with the highest count and return it as a list of three strings.

Notes:

Time complexity: O(m * n ^ 3), where m is the number of users and n is the length of the longest site list for a user. This is due to the nested loops in the create_three_sequences function.

Space complexity: O(n), where n is the length of the input lists. This is due to the storage of the input lists in the merged variable, the user entries in the user_entries dictionary, and the pattern counts in the patterns dictionary.
"""

# Test 1: Single user visiting 3 sites in chronological order
username = ['john']
timestamp = [1, 2, 3]
website = ['web1', 'web2', 'web3']
most_visited_pattern = Solution().mostVisitedPattern(username, timestamp, website)
expected = ['web1', 'web2', 'web3']
assert most_visited_pattern == expected, f"Expected {expected} but got {most_visited_pattern}"
