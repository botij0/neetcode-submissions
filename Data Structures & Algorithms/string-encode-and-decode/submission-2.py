class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "<empty>"
        r = "<word>".join(s for s in strs)
        return r

    def decode(self, s: str) -> List[str]:
        if s == "<empty>":
            return []

        return s.split("<word>")