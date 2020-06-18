'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# Create a nested loop, the outer loop from starting index to n – k th elements. The inner loop will run for k iterations.
# Create a variable to store the maximum of k elements traversed by the inner loop.
# Find the maximum of k elements traversed by the inner loop.
# Print the maximum element in every iteration of outer loop

def sliding_window_max(nums, k):
    # Your code here
    maximum = []
    for i, num in enumerate(nums):

        window = nums[i:i + k]

        if len(window) == k:
            maximum.append(max(window))
    return maximum

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
