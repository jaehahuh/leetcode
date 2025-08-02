class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        all_items_merged = basket1 + basket2
        item_counts_total = Counter(all_items_merged)

        for count in item_counts_total.values():
            if count % 2 != 0:
                return -1

        # Count items in each individual basket
        b1_counts = Counter(basket1)
        b2_counts = Counter(basket2)

        excess_b1 = [] # Items in basket1 that exceed their target count for basket1
        excess_b2 = [] # Items in basket2 that exceed their target count for basket2

        for item_val in item_counts_total.keys():
            half_count = item_counts_total[item_val] // 2 # Target count for each basket

            # If basket1 has more of this item than basket2 (meaning it has excess)
            if b1_counts[item_val] > b2_counts[item_val]:
                # Add excess items to excess_b1 list
                for _ in range(b1_counts[item_val] - half_count):
                    excess_b1.append(item_val)
            
            # If basket2 has more of this item than basket1 (meaning it has excess)
            if b2_counts[item_val] > b1_counts[item_val]:
                # Add excess items to excess_b2 list
                for _ in range(b2_counts[item_val] - half_count):
                    excess_b2.append(item_val)
            
        items_to_swap = []
        items_to_swap.extend(excess_b1)
        items_to_swap.extend(excess_b2)
        items_to_swap.sort()

        # Calculate the minimum swap cost
        total_swap_cost = 0
        min_overall_item_val = min(item_counts_total.keys()) # Smallest item value across both baskets
        num_swap_pairs = len(items_to_swap) // 2 # Number of swap operations required

        for i in range(num_swap_pairs):
            # Cost is the minimum of direct swap vs. indirect swap via min_overall_item_val
            total_swap_cost += min(items_to_swap[i], 2 * min_overall_item_val)
    
        return total_swap_cost