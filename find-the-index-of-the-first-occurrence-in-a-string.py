class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '' or len(needle) > len(haystack):
            return -1
        
        if needle == haystack:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            current_window = haystack[i:i+len(needle)]
            if current_window == needle:
                return i
        return -1
