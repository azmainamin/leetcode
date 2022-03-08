"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
"""

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        """
        First, sort them by start time. [[0,30],[5,10],[15,20]]
        We need to keep track of how many rooms we are allocating, and for each room, when does the meeting start and end.
        For the current meeting, we first look to see if we can place them in any of the current rooms. 
        We can schedule a meeting in a room if the start time of the meeting is AFTER the end time of the meeting happening at the room.
        If we cannot find such a room, we append a new room to our list of rooms.
        
        Runtime: O(intervals * rooms required)
        Spacetime: O(# of rooms)
        """
        
        if len(intervals) == 1:
            return 1
        
        sorted_intervals = sorted(intervals, key=lambda x: x[0]) #sort by start time
        
        rooms = []

        for meeting in sorted_intervals:
            # append first meeting
            if not rooms:
                rooms.append(meeting)
            else:
                # find a room where we can put the current meeting in
                # start time of meeting is after end time of meeting in room
                found_room_idx = 0
                room_found = False
                for i in range(len(rooms)):
                    if meeting[0] >= rooms[i][1]:
                        found_room_idx = i
                        room_found = True
                
                if not room_found:
                    rooms.append(meeting)
                else:
                    # update the room to host this meeting
                    rooms[found_room_idx] = meeting
        
        return len(rooms)