class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        total_days = 365
        arrive_alice = [int(num) for num in arriveAlice.split('-')]
        leave_alice = [int(num) for num in leaveAlice.split('-')]
        arrive_bob = [int(num) for num in arriveBob.split('-')]
        leave_bob = [int(num) for num in leaveBob.split('-')]

        months = {1 : 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334}

        alice_start = months[arrive_alice[0]] + arrive_alice[1]
        alice_end = months[leave_alice[0]] + leave_alice[1]
        bob_start = months[arrive_bob[0]] + arrive_bob[1]
        bob_end = months[leave_bob[0]] + leave_bob[1]

        if alice_start > bob_end or bob_start > alice_end:
            return 0

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        return end - start + 1