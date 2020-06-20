class Solution1:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        result = []
        for point in points:
            result.append((point, math.sqrt(point[0]**2 + point[1]**2)))
        
        final = sorted(result, key=lambda x:x[1])
        final = [item[0] for item in final]
                        
        return final[:K]
