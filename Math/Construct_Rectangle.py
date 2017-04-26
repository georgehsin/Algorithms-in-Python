class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        x = int(math.sqrt(area))
        while area % x !=0:
            x-=1
        return [int(area/x),int(x)]

        