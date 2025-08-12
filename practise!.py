# To check whether a string is palidrome or not

def is_pali(s):
  if (s == s[::-1]):
      return True
  return False

print(is_pali("madam"))
print(is_pali("hello"))

def sec_large(nums):
    # Remove duplicates
    lst = list(set(nums))   
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[-2]

print(sec_large([1,1,1,1]))  # Example usage

# Printing the largest consecutive sequence
def longest_consecutive(nums):
    if not nums:
        return 0
    nums = sorted(set(nums))
    longest = count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            count += 1
        else:
            count = 1
        longest = max(longest, count)
    return longest

# Example
print(longest_consecutive([100, 4, 200, 1, 3, 5,6,2]))

# Read input
cstr = input().strip()

# Initialize an empty string for the result
result = ""

# Loop through each character
for ch in cstr:
    if ch.isupper():
        if result:  # avoid leading space
            result += " "
        result += ch.lower()
    else:
        result += ch

# Print final formatted string
print(result)



ins = input("").strip()

srt = ""

for ele in ins:
    if ele.isupper():
        srt += " " + ele.lower()
    else:
        srt += ele

# Print final formatted string
print(srt)
