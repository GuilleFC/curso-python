"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

import os
os.system('clear')

# def find_first_sum(nums: list[int], goal: int) -> list[int] | None:
#     length = len(nums)
#     for i in range(length):
#         for j in range(i+1, length):
#             if nums[i] + nums[j] == goal:
#                 return [i,j]
#     return None

# print(find_first_sum([4, 5, 6, 2], 8))  # [2, 3]
# print(find_first_sum([4, 5, 6, 1], 8)) 

def find_first_sum(nums: list[int], goal: int) -> list[int] | None:
    seen = {}
    for i, num in enumerate(nums):
        missing = goal - num
        if missing in seen: return [seen[missing], i]
        seen[num] = i # guardar el número actual a los vistos, porque no hemos encontrado la suma aún
        # print(f"index: {i}, num: {num}")

    return None

print(find_first_sum([4, 5, 6, 2], 8))  # [2, 3]