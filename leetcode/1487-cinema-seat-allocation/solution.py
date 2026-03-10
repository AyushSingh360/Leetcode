class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        if not reservedSeats:
            return (n + 1) // 2
        
        # Only care about rows with reserved seats
        reserved_map = {}
        for row, seat in reservedSeats:
            if row not in reserved_map:
                reserved_map[row] = set()
            reserved_map[row].add(seat)
        
        # Count families
        # For unreserved rows, each can fit 2 families (using seats 2-5 and 6-9)
        families = (n - len(reserved_map)) * 2
        
        # Check each affected row
        for row in reserved_map:
            reserved = reserved_map[row]
            count = 0
            
            # Check the three main configs
            # Config 1: seats 2-5 available
            can_place_2_5 = all(seat not in reserved for seat in [2, 3, 4, 5])
            # Config 2: seats 6-9 available
            can_place_6_9 = all(seat not in reserved for seat in [6, 7, 8, 9])
            # Config 3: seats 4-7 available (spans aisle)
            can_place_4_7 = all(seat not in reserved for seat in [4, 5, 6, 7])
            
            # Greedy selection to maximize families
            if can_place_2_5 and can_place_6_9:
                # Best option: place both
                count = 2
            elif can_place_2_5:
                count = 1
            elif can_place_6_9:
                count = 1
            elif can_place_4_7:
                count = 1
            
            families += count
        
        return families
