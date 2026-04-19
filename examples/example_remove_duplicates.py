"""
Example: Remove Duplicates from Sorted Array (LeetCode 26)
Instrumented with TwoPointerTracker.
"""

from typing import List
from tui_pointer import TwoPointerTracker


class Solution:
    def removeDuplicates(self, nums: List[int], tracker: TwoPointerTracker) -> int:
        tracker.record(nums, "start", writer=1, reader=1)

        writer, reader = 1, 1
        while reader < len(nums):
            a, b = nums[reader - 1], nums[reader]
            if a != b:
                nums[writer] = nums[reader]
                tracker.record(nums, f"{a} != {b} → write {b} at [{writer}]", writer=writer, reader=reader)
                writer += 1
            else:
                tracker.record(nums, f"{a} == {b} → skip duplicate", writer=writer, reader=reader)
            reader += 1

        tracker.record(nums, f"done — {writer} unique elements", writer=writer - 1, reader=reader - 1)
        return writer


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f"Input:  {nums}\n")

    tracker = TwoPointerTracker()
    k = Solution().removeDuplicates(nums, tracker)
    tracker.animate(delay=0.7)

    print(f"\nOutput: k={k}, nums[:{k}] = {nums[:k]}")
