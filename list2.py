def sum_squared(numbers):
    sum_odd = 0
    sum_even = 0
    if len(numbers) == 0:
        return None
    for x in numbers:
        if x % 2 != 0:
            sum_odd += x**2
        else:
            sum_even += x**2
    return [sum_odd, sum_even]

print(sum_squared([1, 2, 3, 4, 5]))  # Example usage

# Challenge 1: Write a function that returns the largest number in a list.
# Challenge 2: Write a function that reverses a string.
# Challenge 3: Write a function that counts the number of vowels in a given string.

def largest(lst):
    if not lst:
        return None
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count 
    # Tips to improve at solving coding challenges:
    # 1. Practice regularly with problems of varying difficulty.
    # 2. Break down problems into smaller steps before coding.
    # 3. Read and understand the problem statement carefully.
    # 4. Test your code with different inputs, including edge cases.
    # 5. Review solutions from others and learn new techniques.
    # 6. Focus on writing clean, readable, and efficient code.
    # 7. Learn common algorithms and data structures.
   
    # Common data structures: lists, dictionaries, sets, tuples, stacks, queues, linked lists, trees, graphs.
    # Common algorithms: sorting (bubble, merge, quick), searching (linear, binary), recursion, dynamic programming, hash maps, tree traversals (DFS, BFS).
    
    # Coding problems you can solve using lists, sorting, searching, loops, and conditionals:
    # 1. Find the maximum or minimum value in a list.
    # 2. Remove duplicates from a list.
    # 3. Sort a list in ascending or descending order.
    # 4. Search for an element in a list (linear or binary search).
    # 5. Count occurrences of an element in a list.
    # 6. Find the second largest or smallest element.
    # 7. Merge two sorted lists.
    def find_pairs_with_sum(lst, target):
        pairs = []
        seen = set()
        for num in lst:
            complement = target - num
            if complement in seen:
                pairs.append((complement, num))
            seen.add(num)
        return pairs
    # 9. Separate even and odd numbers into different lists.
    # 10. Find the intersection or union of two lists.
    # 11. Rotate a list left or right by n positions.
    # 12. Find the longest increasing or decreasing subsequence.
    # 13. Check if a list is a palindrome.
    # 14. Remove all negative numbers from a list.
    # 15. Find the frequency of each element in a list.
    
    
def same_sum(lst):
    if len(lst) == 0:
        return None
    for i in lst:
        if (lst[0] + lst[1]) == (lst[i] + lst[i + 1]):
            return True
    return False
