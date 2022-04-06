class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        lookup, output = Counter(), []
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count, sub_domains = int(count), domain.split('.')
            
            for index in range(len(sub_domains)):
                lookup[".".join(sub_domains[index:])] += count
                
        
        for dom, cnt in lookup.items():
            output.append(str(cnt) + " " + str(dom))
            
        return output
