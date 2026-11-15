class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def back(i,zoznam,number):
            if number > target:
                return
            if number == target:
                res.append(zoznam[::])
                return
            if i>=len(candidates):
                return
            if number+candidates[i]>target:
                return
            zoznam.append(candidates[i])
            back(i+1,zoznam,number+candidates[i])
            zoznam.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            back(i+1,zoznam,number)
        back(0,[],0)
        return res
