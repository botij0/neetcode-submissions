class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = 1
        left = 0
        chars = defaultdict(int)
        for right in range(len(s)):
            chars[s[right]] += 1

            current_window_length = right - left + 1

            mc = self.getMaxChar(chars)

            if current_window_length - mc <= k:
                m = max(m, current_window_length)
            else:
                while current_window_length - mc > k:
                    chars[s[left]] -= 1
                    left += 1
                    mc = self.getMaxChar(chars)
                    current_window_length = right - left + 1

        return m

    def getMaxChar(self, chars: dict) -> int:
        current_max = 0
        for v in chars.values():
            current_max = max(current_max, v)
        return current_max