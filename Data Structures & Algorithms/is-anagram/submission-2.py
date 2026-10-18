class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict_s = {}
        dict_t = {}
        for i in s:
            if i in dict_s.keys():
                dict_s[i]+=1
            else:
                dict_s[i]= 1
        for i in t:
            if i in dict_t.keys():
                dict_t[i]+=1
            else:
                dict_t[i]=1

        if (dict_t.keys()!= dict_s.keys()):
            return False
        for i in dict_t.keys():
            if dict_t[i]!= dict_s[i]:
                return False
        return True
