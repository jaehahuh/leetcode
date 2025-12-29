class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_map = defaultdict(list)
        for pattern in allowed:
            allowed_map[pattern[0], pattern[1]].append(pattern[2])
        
        @functools.lru_cache(None)
        def dfs(current_row):
            if len(current_row) == 1:
                return True
            next_row_length = len(current_row) - 1
            def generate_next_row(index, next_row):
                if index == next_row_length:
                    return dfs(tuple(next_row)) # Convert from list to tuple to use @functools.lru_cache
                left_block = current_row[index]
                right_block = current_row[index+1]

                possible_tops = allowed_map.get((left_block, right_block), [])

                for top_block in possible_tops:
                    next_row.append(top_block)
                    if generate_next_row(index+1, next_row):
                        return True
                    next_row.pop()
                return False
            return generate_next_row(0, [])
        return dfs(tuple(bottom))