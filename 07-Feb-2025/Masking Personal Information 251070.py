# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        masked= ''
        if '@' in s:
            #email
            name = (s[:s.index('@')]).lower()
            masked = name[0] + "*****" + name[len(name)-1] + (s[s.index('@'):]).lower()
        else:
            # let us remove any non alpha numeric content out of the phone number
            cleaned = ''.join([num for num in s if num.isalnum()])
            code = cleaned[:len(cleaned) -10]
            if (len(code) == 2):
                masked = "+**-***-***-"+ cleaned[len(cleaned)-4:]
            elif (len(code) == 3):
                 masked = "+***-***-***-"+ cleaned[len(cleaned)-4:]

            elif (len(code) == 0):
                masked = "***-***-"+cleaned[len(cleaned)-4:]
            else:
                masked = "+*-***-***-"+cleaned[len(cleaned)-4:]
        return masked
        
            