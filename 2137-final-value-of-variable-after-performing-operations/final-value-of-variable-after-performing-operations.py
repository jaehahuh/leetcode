class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if op in ('X++', '++X'):
                x += 1
            elif op in ('X--', '--X'):
                x -= 1
            else:
                raise ValueError(f"Invalid operation: {op}")
        return x