class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")

        if len(words) == 1:
            return words[0][0] == words[0][-1]

        for i in range(len(words)-1):
            if i == 0:
                if words[i][0] != words[-1][-1] or words[i][-1] != words[i+1][0]:
                    return False
           
            elif words[i][0] != words[i-1][-1] or words[i][-1] != words[i+1][0]:
                return False

        return True
