class Solution:
    def addBinary(self, a: str, b: str) -> str:

        num1 = int(a, 2)
        num2 = int(b, 2)
        
        # Add the integers
        result = num1 + num2
        
        # Convert the result back to a binary string and remove the '0b' prefix
        return bin(result)[2:]
        