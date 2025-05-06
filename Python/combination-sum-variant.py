class Solution:
    def find_combinations_sum_to_k_count(self, s, k):
        count = 0
        n = len(s)

        def backtrack(index, current_sum):
            nonlocal count
            if index == n:
                if current_sum == k:
                    count += 1
                return

            for i in range(index, n):
                num_str = s[index : i + 1]
                num = int(num_str)

                if index == 0:
                    backtrack(i + 1, num)  # Start with positive
                    backtrack(i + 1, -num) # Start with negative
                else:
                    backtrack(i + 1, current_sum + num)
                    backtrack(i + 1, current_sum - num)

        backtrack(0, 0)
        return count

def test_combinations_sum_to_K_count():
    solution = Solution()
    string = "123456789"
    target = 100
    assert solution.find_combinations_sum_to_k_count(string, target) == 12
    string = "12345"
    target = 15
    assert solution.find_combinations_sum_to_k_count(string, target) == 2

test_combinations_sum_to_K_count()
