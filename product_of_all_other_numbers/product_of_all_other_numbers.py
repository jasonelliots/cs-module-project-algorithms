'''
Input: a List of integers
Returns: a List of integers
'''

#U: for a given array of numbers, produce a new array that multiplies the all of the values together EXCEPT for the value at the corresponding index
def product_of_all_other_numbers(arr):
    # initialize newarray
    # loop through the original array 
    # for each item in the array, loop through the array again and multiply the numbers together UNLESS the index is equal to that item 
    # add that product to the newarray

    newArr = []

    for index, value in enumerate(arr):
        newValue = 1 
        for xIndex, xValue in enumerate(arr):
            if xIndex != index:
                newValue = newValue * xValue
        newArr.append(newValue)
    
    return newArr 


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
