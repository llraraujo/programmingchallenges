class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        aux = stones.copy()
        aux2 = []
        if len(stones) == 1:
            return stones[0]
        while len(aux) > 1:
            heavier = max(aux)
            index_h = aux.index(heavier)
            aux.pop(index_h)
            second_heavier = max(aux)
            index_sh = aux.index(second_heavier)
            aux.pop(index_sh)
            
            smash = heavier - second_heavier
            
            if smash > 0:
                aux2.append(smash)
                
        h = max(aux2)
        m = min(aux2)
        aux2 = [h-m]
        stones = aux2.copy()
        return stones[0]
                
