class MovingAverage1:

    def __init__(self, size: int):
        self.queue = []
        self.size = size
        
        

    def next(self, val: int) -> float:
        queue, size = self.queue, self.size
        queue.append(val)
        
        window_sum = sum(queue[-size:])
        
        return window_sum/ min(size, len(queue))
