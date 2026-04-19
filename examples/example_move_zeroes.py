"""
Example: Move Zeroes (LeetCode 283)
Instrumented with TwoPointerTracker.
"""

from typing import List
from tui_pointer import TwoPointerTracker


class Solution:
    def moveZeroes(self, nums: List[int], tracker: TwoPointerTracker) -> None:
        writer = 0

        tracker.record(nums, "start", writer=writer, reader=0)

        for reader in range(len(nums)):
            if nums[reader] != 0:
                nums[writer], nums[reader] = nums[reader], nums[writer]
                tracker.record(nums, f"nums[{reader}]={nums[writer]} != 0 → swap with [{writer}]", writer=writer, reader=reader)
                writer += 1
            else:
                tracker.record(nums, f"nums[{reader}]=0 → skip", writer=writer, reader=reader)

        tracker.record(nums, "done — zeroes moved to end", writer=writer, reader=len(nums) - 1)


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(f"Input:  {nums}\n")

    tracker = TwoPointerTracker()
    Solution().moveZeroes(nums, tracker)
    tracker.animate(delay=0.7)

    print(f"\nOutput: {nums}")
