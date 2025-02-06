# numpy_task.py
import numpy as np


# Question 1: Why doesn’t np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float)) create a two-dimensional array?
# Answer: The syntax np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float)) is incorrect because np.array() 
# expects a single argument, which is an iterable (like a list or tuple) of elements to form the array. 
# Also, the dtype=float should be placed outside the nested tuples.

# Correct way to create a 2D array:
array_2d = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)], dtype=float)
print("2D array:\n", array_2d)

# Question 2: What is the difference between a = np.array([0, 0, 0]) and a = np.array([[0, 0, 0]])?
# Answer: a = np.array([0, 0, 0]) creates a 1D array with shape (3,). 
# a = np.array([[0, 0, 0]]) creates a 2D array with shape (1, 3), which is essentially a row vector.

a1 = np.array([0, 0, 0])
a2 = np.array([[0, 0, 0]])

print("1D array a1:", a1)
print("Shape of a1:", a1.shape)
print("2D array a2:\n", a2)
print("Shape of a2:", a2.shape)

# Creating a 3 by 4 by 4 array
arr = np.linspace(1, 48, 48).reshape(3, 4, 4)

# Extracting elements or slices
# 1. The element 20.0
element_20 = arr[1, 1, 3]
print("Element 20.0:", element_20)

# 2. The slice [9. 10. 11. 12.]
slice_9_to_12 = arr[0, 2, :]
print("Slice [9. 10. 11. 12.]:", slice_9_to_12)

# 3. The slice [[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47. 48.]]
slice_last_block = arr[2, :, :]
print("Last 4x4 block:\n", slice_last_block)

# 4. The slice [[5. 6.] [21. 22.] [37. 38.]]
slice_specific = arr[:, 1, 0:2]
print("Slice [[5. 6.] [21. 22.] [37. 38.]]:\n", slice_specific)

# 5. The slice [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
slice_reverse = arr[2, :, 2:][::-1, ::-1]
print("Slice [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]:\n", slice_reverse)

# 6. The slice [[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]
slice_step = arr[:, ::-1, ::-3]
print("Slice [[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]:\n", slice_step)

# 7. The slice [[1. 4.] [45. 48.]]
slice_corners = arr[:, [0, -1], [0, -1]]
print("Slice [[1. 4.] [45. 48.]]:\n", slice_corners)

# 8. The slice [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]
slice_middle = arr[1, :, :]
print("Slice [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]:\n", slice_middle)
