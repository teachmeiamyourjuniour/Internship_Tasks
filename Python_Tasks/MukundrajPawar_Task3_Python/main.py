from solutions import (
    word_frequency,
    char_frequency,
    first_non_repeating,
    are_anagrams,
    first_repeating,
    move_zeros,
    second_highest,
    remove_duplicates,
    find_missing,
    two_sum,
    closest_to_zero,
    common_elements,
    rotate_list,
    max_consecutive_sum,
    all_pairs_sum_target
)


print("--- Q1: Word Frequency ---")
print("Given Input:", word_frequency("python is easy and python is powerful"))
print("Extra Test:", word_frequency("data science is cool and data is king"))
print()

print("--- Q2: Character Frequency ---")
print("Given Input:", char_frequency("banana"))
print("Extra Test:", char_frequency("apple"))
print()

print("--- Q3: First Non-Repeating Character ---")
print("Given Input:", first_non_repeating("swiss"))
print("Extra Test:", first_non_repeating("aabbcc"))
print()

print("--- Q4: Check Anagrams ---")
print("Given Input:", are_anagrams("listen", "silent"))
print("Extra Test:", are_anagrams("triangle", "integral"))
print()

print("--- Q5: First Repeating Character ---")
print("Given Input:", first_repeating("programming"))
print("Extra Test:", first_repeating("abca"))
print()

print("--- Q6: Move Zeros to End ---")
print("Given Input:", move_zeros([0, 3, 0, 1, 2, 0, 4]))
print("Extra Test:", move_zeros([1, 0, 2, 0, 3]))
print()

print("--- Q7: Second Highest Distinct Number ---")
print("Given Input:", second_highest([10, 20, 40, 30, 40, 20]))
print("Extra Test:", second_highest([5, 5, 4, 3]))
print()

print("--- Q8: Remove Duplicates ---")
print("Given Input:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Extra Test:", remove_duplicates([1, 1, 2, 2, 3]))
print()

print("--- Q9: Missing Number from 1 to N ---")
print("Given Input:", find_missing([1, 2, 4, 5, 6], 6))
print("Extra Test:", find_missing([1, 2, 3, 5], 5))
print()

print("--- Q10: Two Numbers Sum to Target ---")
print("Given Input:", two_sum([2, 7, 11, 15], 9))
print("Extra Test:", two_sum([3, 2, 4], 6))
print()

print("--- Q11: Number Closest to Zero ---")
print("Given Input:", closest_to_zero([-8, -3, 2, 5, -2]))
print("Extra Test:", closest_to_zero([-5, 5, -1, 2]))
print()

print("--- Q12: Common Elements Between Two Lists ---")
print("Given Input:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Extra Test:", common_elements([1, 2, 2, 3], [2, 3, 4]))
print()

print("--- Q13: Rotate List Right by K ---")
print("Given Input:", rotate_list([1, 2, 3, 4, 5], 2))
print("Extra Test:", rotate_list([1, 2, 3], 1))
print()

print("--- Q14: Max Sum of Two Consecutive Elements ---")
print("Given Input:", max_consecutive_sum([4, 7, 2, 9, 5]))
print("Extra Test:", max_consecutive_sum([1, 5, 2, 8]))
print()

print("--- Q15: All Pairs Sum to Target ---")
print("Given Input:", all_pairs_sum_target([2, 4, 3, 5, 7, 8, 1], 9))
print("Extra Test:", all_pairs_sum_target([1, 5, 3, 3, 4], 6))
print()

