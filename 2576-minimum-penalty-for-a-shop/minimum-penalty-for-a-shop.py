class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        check_customers = Counter(customers)
        y_count = check_customers['Y']
        if y_count == 0:
            return 0
        if y_count == n:
            return n

        min_penalty = y_count
        earliest_hour = 0
        current_closing_hour = 0
        n_count = 0
        for i in range(n):
            if customers[i] == 'Y':
                y_count -= 1
            else:
                n_count += 1

            current_closing_hour += 1
            curr_penalty = y_count + n_count
            
            if curr_penalty < min_penalty:
                min_penalty = curr_penalty
                earliest_hour = current_closing_hour
            
        return earliest_hour