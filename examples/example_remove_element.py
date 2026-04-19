"""
Example: Remove Element (LeetCode 27)
Instrumented with TwoPointerTracker.
"""

from typing import List
from tui_pointer import TwoPointerTracker


class Solution:
    def removeElement(self, nums: List[int], val: int, tracker: TwoPointerTracker) -> int:
        ne = 0
        i, j = 0, len(nums) - 1

        tracker.record(nums, f"start  (removing val={val})", i=i, j=j)

        while i <= j:
            if nums[i] != val:
                tracker.record(nums, f"nums[{i}]={nums[i]} != {val} → keep, move i →", i=i, j=j)
                ne += 1
                i += 1
            else:
                tracker.record(nums, f"nums[{i}]={nums[i]} == {val} → swap with nums[{j}]={nums[j]}, move j ←", i=i, j=j)
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1

        tracker.record(nums, f"done — {ne} elements != {val}", i=i, j=j)
        return ne


if __name__ == "__main__":
    nums = [3, 2, 2, 3, 4, 3, 5]
    val = 3
    print(f"Input:  {nums},  val={val}\n")

    tracker = TwoPointerTracker()
    k = Solution().removeElement(nums, val, tracker)
    tracker.animate(delay=0.8)

    print(f"\nOutput: k={k}, nums[:{k}] = {nums[:k]}")
