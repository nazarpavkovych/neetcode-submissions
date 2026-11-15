class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def back(i, zoznam, rem):
            if rem == 0:
                res.append(zoznam[:])
                return
            if i >= len(candidates) or candidates[i] > rem:
                return

            zoznam.append(candidates[i])
            back(i + 1, zoznam, rem - candidates[i])
            zoznam.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            back(i + 1, zoznam, rem)

        back(0, [], target)
        return res