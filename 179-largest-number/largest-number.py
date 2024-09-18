class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))

        def compare(n1, n2):
            # Return -1 to indicate that x should come before y in the sorted order.
            if n1 + n2 > n2 + n1:
                return -1

            # Return 1 to indicate that y should come before x in the sorted order.
            elif n1 + n2 < n2 + n1:
                return 1

            # Return 0 to indicate that x and y are equivalent for sorting.
            else:
                return 0
            
        # Sort the numbers based on the custom comparator
        nums_str.sort(key=cmp_to_key(compare))

        largest_num = ''.join(nums_str)

        # Edge case: if the largest number is "0", return "0" (e.g., nums = [0, 0, 0])
        return '0' if largest_num[0] == '0' else largest_num