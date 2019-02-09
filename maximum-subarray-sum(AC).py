def maxSequence(arr):
    n = len(arr)
    msum = sum = 0
    for val in arr:
        sum += arr
        sum = max(sum, 0)
        msum = max(msum, sum)
    return msum
    