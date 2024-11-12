class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        #first, sort the items by price, and then set the maximum beauty for each price
        new_items = []
        items.sort(key=lambda x : x[0])
        for price, beauty in items:
            if new_items:
                last_price, last_beauty = new_items[-1]
                if last_price == price:
                    new_items[-1][1] = max(last_beauty, beauty)
                else:
                    # if new price
                    new_items.append([price, beauty])
            else:
                # if new queries is empty
                new_items.append([price, beauty])
        
        queries_with_index = sorted((q, i) for i, q in enumerate(queries)) 
        max_beauty = 0
        j = 0   

        for query, original_index in queries_with_index:
            while j < len(new_items) and new_items[j][0] <= query:
                max_beauty = max(max_beauty, new_items[j][1])
                j += 1
            res.append((original_index, max_beauty))
        
        #sort result by orignal queries order
        res.sort(key=lambda x: x[0]) 
        return [x[1] for x in res]
        