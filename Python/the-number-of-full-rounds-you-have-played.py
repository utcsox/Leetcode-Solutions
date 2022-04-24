class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        
        login_hr, login_minute = loginTime.split(':')
        logout_hr, logout_minute = logoutTime.split(':')
        
        login = int(login_hr) * 60 + int(login_minute)
        logout = int(logout_hr) * 60 + int(logout_minute)
        
        if login > logout:     
            logout += 24* 60
            
        login = (login + 14)//15
        logout = logout//15
            
        return max(0, logout-login)
