def password_recovery_window(log, pattern):
    if not log or not pattern:
        return ""

    from collections import Counter

    pattern_count = Counter(pattern)
    window_count = {}

    required = len(pattern_count)
    formed = 0

    left = 0
    min_len = float("inf")
    min_window = ""

    for right in range(len(log)):
        char = log[right]
        window_count[char] = window_count.get(char, 0) + 1

        if char in pattern_count and window_count[char] == pattern_count[char]:
            formed += 1

        while formed == required:
            window_size = right - left + 1
            if window_size < min_len:
                min_len = window_size
                min_window = log[left:right+1]

            left_char = log[left]
            window_count[left_char] -= 1
            if left_char in pattern_count and window_count[left_char] < pattern_count[left_char]:
                formed -= 1
            left += 1

    return min_window

log = str(input("log: "))
pattern = str(input("pattern: "))


print("Output: ", password_recovery_window(log, pattern))