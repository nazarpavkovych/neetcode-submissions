class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dlzka = len(strs)
        result = {}
        for i in strs:
            prvok = ''.join(sorted(i))
            if prvok in result.keys():
                result[prvok].append(i)
            else:
                result[prvok] = [i]
        return list(result.values())

    


