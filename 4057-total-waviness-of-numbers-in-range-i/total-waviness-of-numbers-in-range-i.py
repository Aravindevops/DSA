class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def wave(n:int)->int:
            s=str(n)
            if len(s)<3:
                return 0

            waviness=0
            for i in range(1,len(s)-1):
                prev_d=s[i-1]
                curr_d=s[i]
                next_d=s[i+1]

                if curr_d>prev_d and curr_d>next_d:
                    waviness+=1
                elif curr_d<prev_d and curr_d<next_d:
                    waviness+=1
            
            return waviness

        total_sum=0
        for num in range(num1,num2+1):
            total_sum+=wave(num)
        return total_sum

            

        