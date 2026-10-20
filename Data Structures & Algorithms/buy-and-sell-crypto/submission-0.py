class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dlzka = len(prices)
        prefix = [prices[0]]
        sufix = [prices[-1]]
        for i in range(1,dlzka):
            prefix.append(min(prefix[-1],prices[i]))
        for i in range(dlzka-2,-1,-1):
            sufix.append(max(sufix[-1],prices[i]))
        max_sum = 0
        for i in range(dlzka-1):
            max_sum= max(max_sum,sufix[-i-1] - prefix[i])
        print(prefix)
        print(sufix)
        return max_sum