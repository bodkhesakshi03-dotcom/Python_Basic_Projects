
import random, math

def set_tuple_module():
    try:
        nums = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
        num_set = set(nums)
        num_tuple = tuple(num_set)
        
        print("Set:", num_set)
        print("Tuple:", num_tuple)
        print("Random 3:", random.sample(num_tuple, 3))
        print("Sqrt of Sum:", math.sqrt(sum(num_tuple)))
    except Exception as e:
        print("Error:", e)

set_tuple_module()

