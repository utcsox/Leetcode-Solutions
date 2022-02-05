class Solution:
    def simplifyPath(self, path: str) -> str:

        tmp = []
        for sub in path.split("/"):
            if sub == '..':
                if tmp:
                    tmp.pop()
                    
            elif sub == '.' or not sub:
                continue
                
            else:
                tmp.append(sub)
                
                
                
        return '/' + '/'.join(tmp)
