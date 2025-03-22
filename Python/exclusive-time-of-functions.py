class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        output = [0] * n
        call_stack = []
        prev_start_time = 0

        for log in logs:
            id, call_type, timestamp = log.split(":")
            id, timestamp = int(id), int(timestamp)

            if call_type == "start":
                if call_stack:
                    output[call_stack[-1]] += timestamp - prev_start_time
                call_stack.append(id)
                prev_start_time = timestamp

            else:
                output[call_stack.pop()] += timestamp - prev_start_time + 1
                prev_start_time = timestamp + 1

        return output
   
