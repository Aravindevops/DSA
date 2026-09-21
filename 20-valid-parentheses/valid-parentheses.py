class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        parentheses={"}":"{","]":"[",")":"("}
        if len(s)==1:
            return False
        else:
            for i in s:
                if i in parentheses:
                    if stack:
                        top = stack.pop()
                    else:
                        top = '#'
                    if parentheses[i]!=top:
                        return False
                else:
                    stack.append(i)
                
            if not stack:
                return True

            else:
                return False
e


                


        