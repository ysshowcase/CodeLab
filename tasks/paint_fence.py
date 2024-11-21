# 276 medium
# You are painting a fence with n posts using k different colors. You must paint the posts following these rules:
#     •	Each post must be painted with one color.
#     •	There cannot be three or more consecutive posts with the same color.
# Given two integers n and k, return the number of ways to paint the fence.

def paint_fence(n: int, k: int) -> int:
    if n == 1:
        return k

    two_post_back = k
    one_post_back = k * k

    for i in range(3, n + 1):
        curr = (k - 1) * (one_post_back + two_post_back)
        two_post_back = one_post_back
        one_post_back = curr

    return one_post_back


print(paint_fence(3, 2))