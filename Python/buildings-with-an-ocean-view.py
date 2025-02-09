class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        output, max_height = [], -1

        for i in range(len(heights) - 1, -1, -1):

            if heights[i] > max_height:
                print(i, max_height)
                output.append(i)
                max_height = heights[i]
        output.sort()
        return output
