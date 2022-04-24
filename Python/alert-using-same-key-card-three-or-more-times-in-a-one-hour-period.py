class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        lookup, output = defaultdict(list), set()
        
        for name, ktime in zip(keyName, keyTime):
            lookup[name].append(ktime)
            
        for name, time in lookup.items():

            for index in range(len(time)):
                hour, minute = time[index].split(':')
                hour_minute = 60* int(hour) + int(minute)
                time[index] = hour_minute
                
            time.sort()

            for i in range(len(time)-1):
                if name in output:
                    break
                count = 1
                for j in range(i+1, len(time)):
                    if time[j] - time[i] <= 60:
                        count += 1
                        
                if count >= 3:
                    output.add(name)
                        
                    
        return sorted(list(output))
