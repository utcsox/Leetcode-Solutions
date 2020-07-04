
"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        
        # total loops require to read n characters given the api call can read 4 chracters at a time is:
        #  n//4 + 1
        #  1. Use read4 api to read the value and store it in a list of empty string
        #  2. If remaining element is greater than output of read4 api call, 
        #.    a).  write the full read4 api call data to the buffer array (buff)
        #.    b). increment the return output number by return value of read4 api call
        #  3. if remaining element (n) is less than output of read4 api call,
        #.    a). write only the remaining element to the buffer array (buff)
        #.    b). increment the return output number by n
         
        output_index = 0
        
        for index in range(n//4 + 1):
            buf4 = ['']*4
            buff_size = read4(buf4)
            
            #if the reamining element is more than buff_size
            
            if n >= buff_size:
                buf[output_index: output_index+buff_size] = buf4       

                n -= buff_size
                output_index += buff_size   
            
            # remaining elements that are less than buff_size
            else:
                buf[output_index: output_index + n ] = buf4
                output_index += n

        return output_index
