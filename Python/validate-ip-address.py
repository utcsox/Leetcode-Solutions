class Solution:
    def validIPAddress(self, IP: str) -> str:
        def validate_IPv4(IP: str) -> str:
            split = IP.split('.')
            for sub in split:
                # check if each address field has to be between 1-3 digits
                if len(sub) == 0 or len(sub) >3:
                    return 'Neither'
                # check if first digit is '0' and it has more than one digit -> False
                # check if subnet is are only digits
                if ((sub[0] == '0' and len(sub) != 1) or not sub.isdigit() or int(sub) > 255):
                    return 'Neither'
            return 'IPv4'
                    
        def validate_IPv6(IP: str) -> str:
            split = IP.split(':') 
            hexadigits = '0123456789abcdefABCDEF'
            for sub in split:
                if len(sub) == 0 or len(sub) > 4: #or not all(c in hexdigits for c in sub):
                    return "Neither"
                for c in sub:
                     if c not in hexadigits:
                        return "Neither"
            return 'IPv6'
        
        if len(IP.split('.'))-1 == 3:
            return validate_IPv4(IP)
        elif len(IP.split(':'))-1 == 7:
            return validate_IPv6(IP)
        else:
            return "Neither"

            
        
