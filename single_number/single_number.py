'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# add each number once and multiply the sum by 2, this will be twice the sum of each element in the array
# subtract the sum of the whole array from twice the sum == number that comes first in the array

def single_number(arr):
    # Your code here
    return (2 * sum(set(arr))) - sum((arr))  



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")