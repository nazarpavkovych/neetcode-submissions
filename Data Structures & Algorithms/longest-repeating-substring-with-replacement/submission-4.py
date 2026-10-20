from collections import deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dlzka = len(s)
        j = 0

        slovnik = {}
        for i in set(s):
            slovnik[i] = 0
        i = 0

        skip = k
        max_count = 0
        fronta = deque()
        count = 0
        while j < dlzka:
            slovnik[s[j]]+=1
            count+=1
            print(i,j)
            while max(slovnik.values()) + k < (j - i+1):
                slovnik[s[i]]-=1
                i+=1
                count-=1
            max_count = max(max_count,count)
            j+=1

        return max_count

            