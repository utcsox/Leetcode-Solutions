class Solution:
    def maximumSwap(self, num: int) -> int:

        num_list = list(str(num))
        lookup = [0] * len(num_list)

        max_index, max_value = len(num_list) - 1, num_list[len(num_list) - 1]

        for i in reversed(range(len(num_list))):
            if num_list[i] > max_value:
                max_index = i
                max_value = num_list[i]

            lookup[i] = max_index


        for i in range(len(num_list)):
            if num_list[lookup[i]] > num_list[i]:
                num_list[i], num_list[lookup[i]] = num_list[lookup[i]], num_list[i]
                return int("".join(num_list))

        return num
