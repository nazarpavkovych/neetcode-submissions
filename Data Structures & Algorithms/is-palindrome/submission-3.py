class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        dlzka = len(s)
        j=dlzka-1
        while i<j:
            while j>0 and not ('a'<=s[j]<='z' or 'A'<=s[j]<='Z' or '0'<=s[j]<='9'):
                j-=1
            while i < dlzka and  not ('a'<=s[i]<='z' or 'A'<=s[i]<='Z' or '0'<=s[i]<='9'):
                i+=1
            if i<dlzka and j > 0 and s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True

