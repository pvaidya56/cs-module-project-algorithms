'''
Input: a List of integers
Returns: a List of integers
'''
# loop through the list
#if number is zero than move it to the end of the list (remove it and append it to the end of the list)
    #do this until all zeros are at the end of the list


def moving_zeroes(arr):
    # Your code here
    for nums in arr:
        if nums == 0:
            arr.remove(nums)
            arr.append(0)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")