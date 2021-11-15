class TweetCounts:

    def __init__(self):
        self.defaultdict = defaultdict(list)
        self.lookup = {"minute": 60, "hour":3600, "day": 86400}
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.defaultdict[tweetName].append(time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        
        times = self.defaultdict[tweetName]
        
        seconds = self.lookup[freq]
        size = (endTime-startTime)//seconds + 1
            
        r = [0] * int(size)
        
        for t in times:
            if(startTime <= t and t <=endTime):
                index = int((t-startTime)/seconds)
                r[index] += 1
                
        return r
        
        
# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
