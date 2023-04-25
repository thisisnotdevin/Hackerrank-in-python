class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = len(digits)-1
        if digits[0] == None:
            return [1]
        elif digits[num] != 9:
            digits[num] += 1
            return digits
        
        while digits[num] == 9:

            digits[num] = 0
            
            if digits[num-1] is 0:
                print("if called")
                digits.insert(0, 1)
                
            elif digits[num-1] < 9:
                print("elif called")
                digits[num-1] += 1
                break
            num -= 1
        return digits
