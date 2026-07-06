class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = 1
        left = 0
        chars = defaultdict(int)
        for right in range(len(s)):
            chars[s[right]] += 1

            current_window_length = right - left + 1
            mc = max(chars.values())

            while current_window_length - mc > k:
                chars[s[left]] -= 1
                left += 1
                mc = max(chars.values())
                current_window_length = right - left + 1
                
            m = max(m, current_window_length)

        return m
