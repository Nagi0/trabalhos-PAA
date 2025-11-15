# Python program for maximum subarray sum
# using Divide and Conquer


def max(a, b, c=None):
    if c is None:
        return a if a > b else b
    return max(max(a, b), c)


def maxCrossingSum(arr, l, m, h):

    # Include elements on the left of mid
    leftSum = float("-inf")
    sum = 0
    for i in range(m, l - 1, -1):
        sum += arr[i]
        leftSum = max(leftSum, sum)

    # Include elements on the right of mid
    rightSum = float("-inf")
    sum = 0
    for i in range(m, h + 1):
        sum += arr[i]
        rightSum = max(rightSum, sum)

    # Return the maximum of left sum, right sum, and their combination
    return max(leftSum + rightSum - arr[m], leftSum, rightSum)


def MaxSum(arr, l, h):
    if l > h:
        return float("-inf")
    if l == h:

        # Base case: one element
        return arr[l]

    # Find the middle point
    m = l + (h - l) // 2

    # Return the maximum of three cases
    return max(
        MaxSum(arr, l, m),
        MaxSum(arr, m + 1, h),
        maxCrossingSum(arr, l, m, h),
    )


def maxSubarraySum(arr):
    return MaxSum(arr, 0, len(arr) - 1)


arr = [0.5, 0.5, 6.5, -5.5]
print(maxSubarraySum(arr))
