
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        
        buffer = [''] * 4
        result = 0
        for index in range(n//4 + 1):
            buffersize = read4(buffer)
            
            
            if buffersize:
                if n >= buffersize:
                    buf[result: result+buffersize] = buffer[:buffersize]
                    result += buffersize
                    n = n - buffersize
                else:
                    buf[result: result + n] = buffer[:n]
                    result += n
            else:
                continue
        return result
