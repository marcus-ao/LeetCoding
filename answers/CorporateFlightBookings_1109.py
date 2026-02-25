from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)

        for left, right, booking in bookings:
            diff[left - 1] += booking

            diff[right] -= booking

        for i in range(1, n):
            diff[i] += diff[i - 1]

        return diff[:-1] # diff[:n]
