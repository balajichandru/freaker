class Solution:
    def carFleet(self, target, position, speed) -> int:
        cars_right_to_left = sorted(zip(position, speed), reverse=True)

        bottleneck = float('-inf')
        fleets = 0

        for d, s in cars_right_to_left:
            print(d,s)
            remaining_dist = target - d
            time_to_reach_target = (remaining_dist / s)

            if time_to_reach_target > bottleneck:
                bottleneck = time_to_reach_target
                fleets += 1

        return fleets
Solution().carFleet(12,[10,8,0,5,3],[2,4,1,1,3])