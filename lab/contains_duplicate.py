#An algorithm difficulty O(n log n)
def contains_duplicates(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


print(contains_duplicates([6, 7, 1, 2, 3, 4, 5, 7]))

# An algorithm difficulty O(n)
def contains_duplicates_1(nums):
    met = set()
    for num in nums:
        if num in met:
            return True
        met.add(num)
    return False
