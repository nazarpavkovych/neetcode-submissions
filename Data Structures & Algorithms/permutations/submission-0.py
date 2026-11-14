class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def back(zoznam,visited):
            if len(nums)==len(zoznam):
                res.append(zoznam)
            else:
                for i in nums:
                    if i not in visited:
                        back(zoznam+[i],visited|{i})
        for i in nums:
            back([i],{i})
        return res
