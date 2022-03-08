"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""

class Solution:
    def merge(self, intervals):
        """
        Are intervals sorted? 
        If not, sort them
        IDEA1
        - find if 2+ intervals intersect. 
            - brute force: create arrays from start to end of both. check intersection using set intersection. if len(intersecion) > 0, it overlaps.
            - 1,3, and 2,6 VS 2,6 and 8,10
            - end[i] >= start[i+1]
        - once we find this, take min(start[i], start[i+1]) and max(end[i], end[i+1]) -> This works when we are merging only two intervals
        - the tricky part is, once we find 2 intervals that intersect, we cannot stop. Because the next interval might also intersect with the first two
        - example: [[0,2], [1,4], [3,5]]
        - what we need to do is, get the previous interval from our merged, look at the end, and take the max(prev_interval[end], current_interval[end]) 
        """
        
        intervals = sorted(intervals, key= lambda x: x[0])
        
        if len(intervals) == 1: return intervals
        
        merged = []

        for interval in intervals:
            if not merged:
                merged.append(interval)
            else:
                last_interval = merged[-1]
                # if there is no intersection
                if last_interval[1] < interval[0]: 
                    merged.append(interval)
                else:
                    # there is intersection
                    merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
            