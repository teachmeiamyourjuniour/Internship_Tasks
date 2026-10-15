# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


# Q2. Find the Frequency of Each Character in a Word
def char_frequency(word):
    freq = {}
    for char in word:
        freq[char] = freq.get(char, 0) + 1
    return freq


# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating(word):
    freq = {}
    for char in word:
        freq[char] = freq.get(char, 0) + 1

    for char in word:
        if freq[char] == 1:
            return char
    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)


# Q5. Find the First Repeating Character in a String
def first_repeating(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

# Q6. Move All Zeros to the End of a List
def move_zeros(lst):
    non_zeros = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros


# Q7. Find the Second Highest Distinct Number in a List
def second_highest(lst):
    unique_nums = list(set(lst))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]


# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# Q9. Find the Missing Number from 1 to N
def find_missing(nums, N):
    expected_sum = N * (N + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


# Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum(nums, target):
    seen = set()
    for num in nums:
        needed = target - num
        if needed in seen:
            return [needed, num]
        seen.add(num)
    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(lst):
    closest = lst[0]
    for num in lst:
        if abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest) and num > closest:
            closest = num
    return closest


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    set2 = set(list2)
    result = []
    seen = set()
    for item in list1:
        if item in set2 and item not in seen:
            result.append(item)
            seen.add(item)
    return result

# Q13. Rotate a List to the Right by K Positions
def rotate_list(nums, K):
    if not nums:
        return nums
    K = K % len(nums)
    if K == 0:
        return nums
    return nums[-K:] + nums[:-K]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_sum(lst):
    max_sum = float('-inf')
    for i in range(len(lst) - 1):
        current_sum = lst[i] + lst[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_pairs_sum_target(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        needed = target - num
        if needed in seen:
            pair = tuple(sorted((needed, num)))
            pairs.add(pair)
        seen.add(num)
    return [list(p) for p in sorted(list(pairs))]