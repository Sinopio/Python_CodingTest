class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = 0 
        start = 0
        
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:  # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)

            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length