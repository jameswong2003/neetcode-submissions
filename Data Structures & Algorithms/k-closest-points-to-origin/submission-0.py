class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for point in points:
            xi, yi = point
            distance.append((xi * xi + yi * yi, point))

        heapq.heapify(distance)
        result = []

        for _ in range(k):
            dist, point = heapq.heappop(distance)
            result.append(point)
        return result