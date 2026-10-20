class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        i=0 
        j = 0 
        dlzka = len(s)
        if dlzka <= 1:
            return dlzka
        mnozina = set()
        count = 0
        while j < dlzka:
            if s[j] not in mnozina:
                max_length = max(max_length, count) 
                mnozina.add(s[j])
                count+=1
                j+=1
            else:
                while s[j] in mnozina:
                    mnozina.remove(s[i])
                    i+=1
                    count-=1
            max_length = max(max_length,count)

        return max_length


            
            