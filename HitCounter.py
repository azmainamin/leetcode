"""
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

    HitCounter() Initializes the object of the hit counter system.
    void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
    int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
"""

class HitCounter:
    def __init__(self):
        self.counter = {}

    def hit(self, timestamp: int) -> None:
        if timestamp in self.counter:
            self.counter[timestamp] = self.counter[timestamp] + 1
        else:
            self.counter[timestamp] = 1
        

    def getHits(self, timestamp: int) -> int:
        start = timestamp - 300 if timestamp - 300 > 0 else 0
        hits = [val for key, val in self.counter.items() if start <key <=timestamp]
        
        return sum(hits)