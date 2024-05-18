class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        if k <= arr[0] - 1:
            return k
        k -= arr[0] - 1 

        for index in range(len(arr) - 1):
            num_missing_elements = arr[index + 1] - arr[index] - 1

            if k <= num_missing_elements:
                return arr[index] + k

            else:
                k -= num_missing_elements

        # if k > 0, we want to add it to the end
        return arr[-1] + k
