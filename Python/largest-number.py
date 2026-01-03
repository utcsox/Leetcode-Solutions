class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        num_strings = [str(num) for num in nums]
        
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1

            else:
                return 1
        sorted_string = sorted(num_strings, key=cmp_to_key(compare))

        return str(int("".join(sorted_string)))
