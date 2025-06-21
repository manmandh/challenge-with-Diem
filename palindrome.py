class Solution:
  def isPalindrome(self, x):
    a = x
    result = 0
    while a > 0:
      last = a % 10
      result = result * 10 + last
      a //= 10
    return result == x

if __name__ == "__main__":
  s = Solution()
  test_cases = [121, -121, 121, 10, 12321, 0, 123456789987654321]

  for x in test_cases:
    result = s.isPalindrome(x)
    print(f"Is {x} a palindrome? {result}")
