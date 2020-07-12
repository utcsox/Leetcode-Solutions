class Solution1:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        result = []
        for point in points:
            result.append((point, math.sqrt(point[0]**2 + point[1]**2)))
        
        final = sorted(result, key=lambda x:x[1])
        final = [item[0] for item in final]
                        
        return final[:K]
    
    
class Solution2:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(x) ->int:
            return math.sqrt(x[0]**2 + x[1]**2)
        
        def partition(i, j) -> int:
        # two pointer, left and right
        # initialize left to be -1, 0 or i-1 , 1
            pivot = points[j]
            left = i - 1
            for right in range(i, j):
                centerpoint = points[right]
                
                # if the centerpoint is less than pivot, increase the left pointer, and swape elments on left/right
                if dist(centerpoint) < dist(pivot):
                    left += 1
                    points[left], points[right] = points[right], points[left]
                    
            # swap the last element with left+1
            points[j], points[left+1] = points[left+1], points[j]
            return left+1
        
        def sort(i, j, K):
            if i >= j:
                return
            mid = partition(i, j)
            
            if (mid - i + 1) == K:
                return
            elif (mid - i + 1) < K:
                sort(mid+1, j, K-(mid-i +1))
            else:
                sort(i, mid-1, K)
                
        sort(0, len(points)-1, K)        
        return points[:K]
