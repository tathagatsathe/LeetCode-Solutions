class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = bin(n)[2:]
        flipped = ""
        
        for b in binary:
            if b == "0":
                flipped+="1"
            else:
                flipped+="0"

        return int(flipped,2)