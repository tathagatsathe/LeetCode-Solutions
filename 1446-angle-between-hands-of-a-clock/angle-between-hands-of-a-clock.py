class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle = minutes*(360//60)
        hour_angle = hour*(360//12) + (360//12)*(1/60)*minutes 
    
        angle_between = abs(hour_angle - min_angle)

        return min(angle_between, 360 - angle_between)