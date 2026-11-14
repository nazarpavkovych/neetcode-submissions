class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        zoz = [[]]
        def back(zoznam,visited):
            zoz.append(zoznam)

            for i in nums:
                if i > zoznam[-1]:

                    back(zoznam+[i],visited|{i})
        for i in nums:
            back([i],{i})
        return zoz
            


