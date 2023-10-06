# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         last_digit = x % 10
#         if x < 0:
#           return False
#         if x > 100:
#             first_digit = x // 100
#         else:
#             first_digit = x // 10
#         if first_digit == last_digit:
#             return True
#         else:
#             return False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
          return False
        i = x
        rev_num = 0
        while(i > 0 ):
          reminder = i % 10
          rev_num = rev_num * 10 + reminder
          i = i // 10
        if rev_num == x:
            return True
        else:
            return False
        