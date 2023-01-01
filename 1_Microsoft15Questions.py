'''3. Longest Substring Without Repeating Characters
Level : Medium

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.'''
# Answer : 1

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len: int = 0
        print('MaxLen:', max_len)

        # [1] longest substring is the one with the largest 
        #    difference between positions of repeated characters; 
        #    thus, we should create a storage for such positions 
        pos = defaultdict(int)
        print("POS", pos)

        # [2] while iterating through the string (i.e., moving 
        #    the end of the sliding window), we should also 
        #    update the start of the window 
        start: int = 0
        print("start: ", start)

        for end, ch in enumerate(s):
            print(end, ch)
            # [3] get the position for the start of sliding window 
            #    with no other occurences of 'ch' in it 
            start = max(start, pos[ch])
            print(start)
            # [4] update maximum length 
            max_len = max(max_len, end - start + 1)
            print('m', max_len)
            # [5] set the position to be used in [3] on next iterations
            pos[ch] = end + 1
            print("pos", pos)

        return max_len


a = Solution()
print(a.lengthOfLongestSubstring('abcabcbb'))

'''  *****************************************************************************     '''
