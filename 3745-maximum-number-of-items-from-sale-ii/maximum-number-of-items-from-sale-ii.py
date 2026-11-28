from collections import defaultdict
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        min_price = min(price for _, price in items)
        max_factor = max(factor for factor, _ in items)

        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1

        multiples = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                for m in range(f, max_factor + 1, f):
                    multiples[f] += freq[m]

        bonus_by_price = defaultdict(int)
        for factor, price in items:
            cap = multiples[factor] - 1
            if cap > 0 and price < 2 * min_price:
                bonus_by_price[price] += cap

        total_items = 0
        for price in sorted(bonus_by_price):
            can_buy = min(bonus_by_price[price], budget // price)
            total_items += 2 * can_buy
            budget -= can_buy * price
            if budget < price:
                break

        total_items += budget // min_price
        return total_items