class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_cnt = defaultdict(int) # n1 * n2 -> count
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_cnt [product] += 1
        # 1 count -> ◊ pair -> ◊ tuples
        # 2 count -> 1 pair -> 8 tuples
        # 3 count -> 3 pairs -> 24 tuples
        # 4 count -> 6 pairs -> 48 tuples
        # 5 count -> 10 pairs -> 80 tuples
        res = 0
        for cnt in product_cnt.values():
            pairs = (cnt * (cnt-1)) // 2
            res += 8 * pairs
        return res