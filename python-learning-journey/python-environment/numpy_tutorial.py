import numpy as np

#1
# one_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

# print(one_array.shape)
# print(one_array.size)
# print(one_array.ndim)
# print(len(one_array))
# print(type(one_array))


# new_arr = one_array.reshape(2, 10)

# print(new_arr)



# 2
# even_arr = [2, 4, 6, 8, 10]
# odd_arr = [1, 3, 5, 7, 9]

# np_even_arr = np.array(even_arr)
# np_odd_arr = np.array(odd_arr)

# arr_sum = np_even_arr + np_odd_arr
# arr_diff = np_even_arr - np_odd_arr
# arr_mul = np_even_arr * np_odd_arr
# arr_div = np_even_arr / np_odd_arr

# print(arr_sum)
# print(arr_diff)
# print(arr_mul)
# print(arr_div)

# list_sum = even_arr + odd_arr
# list_diff = even_arr - odd_arr
# list_mul = even_arr * odd_arr
# list_div = even_arr / odd_arr

# print(list_sum)
# print(list_diff)
# print(list_mul)
# print(list_div)  # Doesn't work the same way as numpy arrays


#3

# arr2 = [[95, 62, 83], 
#         [71, 63, 90], 
#         [99, 81, 75],
#         [84, 70, 64]]


# np_arr2 = np.array(arr2)

# print(np_arr2[0])
# print(np_arr2[:, 0])
# print(np_arr2[:2, 0:2])
# print(np_arr2[-1: -3: -1 ])
# print(np_arr2[0])


#4
# test_scores = [
#     85, 92, 78, 64, 89, 95, 71, 83, 76, 90,
#     58, 87, 91, 73, 80, 68, 94, 82, 77, 85,
#     62, 88, 79, 93, 70, 86, 69, 74, 98, 81
# ]

# np_arr = np.array(test_scores)

# print(np.mean(np_arr))
# print(np.median(np_arr))
# print(np.min(np_arr))
# print(np.max(np_arr))

# print(np.std(np_arr))



#5

# arr2 = [[95, 62, 83], 
#         [71, 63, 90],   
#         [99, 81, 75],
#         [84, 70, 64]]


# np.set_printoptions(precision=2 , suppress= True, floatmode= 'fixed')

# np_arr2 = np.array(arr2)

# print(np.round(np.mean(np_arr2, axis= 0), 2))
# print(np.round(np.average(np_arr2, axis= 1), 2))

# print(np.round(np.max(np_arr2, axis= 0), 2))
# print(np.round(np.min(np_arr2, axis= 0), 2))



#6
# arr = [23, 55, 58, 58, 12, 37, 12, 42, 47, 23, 0, 11, 25, 31, 60, 44, 47, 36, 11, 36, 4, 57, 32, 27, 31, 2, 39, 53, 1, 16]


# np_arr = np.array(arr)

# print(np_arr[(np_arr >= 20) & (np_arr <= 30)])


# arr2 = []
# np_arr2 = np.array(arr2)

# if np_arr.any > 30:
#     np_arr2.copy(np_arr)


# print(np_arr2)


#7
# arr = [23, 25, -1, 27, 999, 24, -1, 28]
# np_arr = np.array(arr)

# missing_values = np.where((np_arr == -1) | (np_arr == 999), np.median(np_arr[(np_arr != -1) & (np_arr != 999)] ), np_arr)

# print(missing_values)


#8
# arr = [23, 55, 58, 58, 12, 37, 12, 42, 47, 23, 0, 11, 25, 31, 60, 44, 47, 36, 11, 36, 4, 57, 32, 27, 31, 2, 39, 53, 1, 16]

# np_arr = np.array(arr)

# results = np.where(np_arr > 30, 1, 0)

# print(results)


#9

# arr = [[  0,  50, 100],
#        [150, 200, 250],
#        [ 25,  75, 125]]

# np_arr = np.array(arr)

# # Brighten the Image
# np_arr = np_arr + 10

# # Darken the Image
# np_arr = np_arr -5

# # Invert the Image
# np_arr = 255 - np_arr

# # Crop the Image
# print(np_arr[0:2, 0:2])

# # threshold it into black/white
# results = np.where(np_arr >= 128, 255, 0)

# print(results)

# out_np_arr = np.clip(np_arr, a_min=0, a_max=255)


# print(out_np_arr)


#10
arr1 = [[95, 62, 83], 
        [71, 63, 90], 
        [99, 81, 75],
        [84, 70, 64]]


arr2 = [[48, 35, 38], 
        [56, 68, 36], 
        [22, 94, 12],
        [19, 70, 43]]


np_arr1 = np.array(arr1)
np_arr2 = np.array(arr2)


added_matrix = np_arr1 + np_arr2
multiplied_matrix = np_arr1 * np_arr2


# print(multiplied_matrix)
# print(added_matrix)

print(np.transpose(np_arr2))