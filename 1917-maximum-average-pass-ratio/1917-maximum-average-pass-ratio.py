class Solution:
    def maxAverageRatio(
        self, classes: List[List[int]], extraStudents: int
    ) -> float:
        # Lambda to calculate the gain of adding an extra student
        def _calculate_gain(passes, total_students):
            return (passes + 1) / (total_students + 1) - passes / total_students

        # Max heap to store (-gain, passes, total_students)
        max_heap = []
        for passes, total_students in classes:
            gain = _calculate_gain(passes, total_students)
            heapq.heappush(max_heap, (-gain, passes, total_students))

        # Distribute extra students
        for _ in range(extraStudents):
            current_gain, passes, total_students = heapq.heappop(max_heap)
            heapq.heappush(
                max_heap,
                (
                    -_calculate_gain(passes + 1, total_students + 1),
                    passes + 1,
                    total_students + 1,
                ),
            )

        # Calculate the final average pass ratio
        total_pass_ratio = 0
        while max_heap:
            _, passes, total_students = heapq.heappop(max_heap)
            total_pass_ratio += passes / total_students
        return total_pass_ratio / len(classes)
# class Solution:
#     def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
#         m=float('inf')
#         ind=0
#         for idx,i in enumerate(classes):
#             if m>(i[0]/i[1]):
#                 m=i[0]/i[1]
#                 ind=idx
#         classes[ind][0],classes[ind][1]=classes[ind][0]+extraStudents,classes[ind][1]+extraStudents
#         s=0
#         for i in classes:
#             s+=(i[0]/i[1])
#         return s/len(classes)    