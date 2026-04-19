"""
Example: Two-Sum (sorted array) visualized with TwoPointerTracker.
"""

from tui_pointer import TwoPointerTracker


def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int] | None:
    tracker = TwoPointerTracker()
    left, right = 0, len(nums) - 1

    tracker.record(nums, "start", left=left, right=right)

    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            tracker.record(nums, f"found! nums[{left}] + nums[{right}] = {target}", left=left, right=right)
            break
        elif s < target:
            tracker.record(nums, f"sum {s} < {target} → move left →", left=left, right=right)
            left += 1
        else:
            tracker.record(nums, f"sum {s} > {target} → move right ←", left=left, right=right)
            right -= 1
    else:
        tracker.record(nums, "no solution found", left=left, right=right)

    tracker.animate(delay=0.8)
    return (left, right) if left < right else None


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]
    target = 10
    print(f"Finding two numbers in {nums} that sum to {target}\n")
    result = two_sum_sorted(nums, target)
    if result:
        i, j = result
        print(f"\nResult: indices ({i}, {j})  →  {nums[i]} + {nums[j]} = {target}")
