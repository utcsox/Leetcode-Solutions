class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1bl, y1bl, x1tr, y1tr = rec1[0], rec1[1], rec1[2], rec1[3]
        x2bl, y2bl, x2tr, y2tr = rec2[0], rec2[1], rec2[2], rec2[3]

        # if there is intercept:
        # 1. the top right of rectangle 2 will be greater than bottom left of rectangle 1
        # 2. the bottom left of rectangle 2 will be less than the top right of rectangle 1

        if (x1bl < x2tr) & (y1bl < y2tr) & (x2bl < x1tr) & (y2bl < y1tr):
            return True

        return False
