class Solution:
    def findBuildingViewCount_variant_1762(self, heights: list[int]) -> int:
        """
        Counts the number of buildings with an ocean view (taller than all buildings to their right).

        Args:
            heights: A list of integers representing the heights of the buildings.

        Returns:
            The number of buildings with an ocean view.
        """

        if len(heights) == 0:
            return 0

        max_height, res = heights[-1], 1

        for i in range(len(heights)- 2, -1, -1):
            if heights[i] > max_height:
                max_height = heights[i]
                res += 1

        return res

def test_findBuildingViewCount_variant_1762():
    solution = Solution()
    heights = [4, 2, 3, 1]
    assert 3 == solution.findBuildingViewCount_variant_1762(heights)

    heights = [6, 1, 2, 4, 2, 2, 2, 2, 3, 1]
    assert 4 == solution.findBuildingViewCount_variant_1762(heights)

    heights = [4, 3, 2, 1]
    assert 4 == solution.findBuildingViewCount_variant_1762(heights)

    heights = [1, 3, 2, 4]
    assert 1 == solution.findBuildingViewCount_variant_1762(heights)

    heights = [2, 2, 2, 2, 2, 2, 2]
    assert 1 == solution.findBuildingViewCount_variant_1762(heights)

    heights = [0, 1, 2, 3, 2, 1, 0]
    assert 4 == solution.findBuildingViewCount_variant_1762(heights)

    heights = [1, 2, 3, 4]
    assert 1 == solution.findBuildingViewCount_variant_1762(heights)

    heights = [10]
    assert 1 == solution.findBuildingViewCount_variant_1762(heights)

# You can call the test function to verify the implementation
test_findBuildingViewCount_variant_1762()
