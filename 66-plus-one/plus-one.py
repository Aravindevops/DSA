class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s=""
        add=0
        for i in digits:
            s+=str(i)
        add=int(s)+1
        digits=[]
        for i in str(add):
            digits.append(int(i))
        return digits
        