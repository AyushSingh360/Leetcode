from bisect import bisect_right

class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        n = len(rains)
        ans = [-1] * n
        
        # Track which lakes are full and when they were filled
        full_lakes = {}  # lake_id -> day index when filled
        
        # Track available dry days (indices where rains[i] == 0)
        dry_days = []
        
        for i, lake in enumerate(rains):
            if lake == 0:
                # This is a dry day - we'll decide later which lake to dry
                dry_days.append(i)
            else:
                # It's raining on this lake
                if lake in full_lakes:
                    # This lake is already full - need to find a dry day to dry it
                    last_rain_day = full_lakes[lake]
                    
                    # Find the first dry day after last_rain_day using binary search
                    idx = bisect_right(dry_days, last_rain_day)
                    
                    if idx >= len(dry_days):
                        # No available dry day - flood is inevitable
                        return []
                    
                    # Use this dry day to dry this lake
                    dry_day = dry_days[idx]
                    ans[dry_day] = lake
                    dry_days.pop(idx)
                    
                    # Remove from full_lakes since we dried it
                    del full_lakes[lake]
                
                # Mark this lake as full
                full_lakes[lake] = i
        
        # For remaining dry days, just dry any lake (use lake 1)
        for day in dry_days:
            ans[day] = 1
        
        return ans
