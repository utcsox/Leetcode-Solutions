class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        closing_bracket_stack = []
        
        # loop over the string
            # i) if "()", we skip the rest
            # ii) if the char is open bracket, add the index of in the stack
            # iii ) if there is no element in the stack, we add the closing bracket to 
            # closing_bracket_stack for removal
            # iv) if there is more than one opening bracket in the stack,
            # pop the last one
            
        for index, char in enumerate(s):
            if char not in "()":
                continue
            if char == '(':
                stack.append(index)
            elif not stack:
                closing_bracket_stack.append(index)
                
            else:
                stack.pop()
                
            # want to the index of all that we want to remove
            
        set_stack = set(stack)
        set_closing_bracket_stack = set(closing_bracket_stack)
        index_to_remove = set_stack.union(set_closing_bracket_stack)

        # build the list of char that we want to return

        string_builder = []
        for index, char in enumerate(s):
            if index not in index_to_remove:
                string_builder.append(char)

        return ''.join(string_builder)
                    
