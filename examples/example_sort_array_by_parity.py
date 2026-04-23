"""
Example: Sort Array By Parity (LeetCode 905)
Instrumented with TwoPointerTracker.
"""

from typing import List
from tui_pointer import TwoPointerTracker


class Solution:
    def sortArrayByParity(self, nums: List[int], tracker: TwoPointerTracker) -> List[int]:
        i, j = 0, len(nums) - 1

        tracker.record(nums, "start", i=i, j=j)

        while i < j:
            i_odd = nums[i] % 2 == 1
            j_odd = nums[j] % 2 == 1
            if i_odd and not j_odd:
                nums[i], nums[j] = nums[j], nums[i]
                tracker.record(nums, f"odd/even → swap, i →", i=i, j=j)
            elif i_odd and j_odd:
                tracker.record(nums, f"odd/odd → ← j", i=i, j=j)
            elif not i_odd and not j_odd:
                tracker.record(nums, f"even/even → i →", i=i, j=j)
            else:
                tracker.record(nums, f"even/odd → i → ← j", i=i, j=j)
            if nums[i] % 2 == 0:
                i += 1
            if nums[j] % 2 == 1:
                j -= 1

        tracker.record(nums, "done — evens left, odds right", i=i, j=j)
        return nums


if __name__ == "__main__":
    nums = [2, 7, 9, 4, 6, 3, 8, 5, 10, 1, 12, 11, 14, 13, 16]
    print(f"Input:  {nums}\n")

    tracker = TwoPointerTracker()
    result = Solution().sortArrayByParity(nums, tracker)
    tracker.animate(delay=0.7)

    print(f"\nOutput: {result}")
