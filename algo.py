# ===========================================
# ALGO.PY - Extract name + number using custom names list
# ===========================================
# Rules:
# 1. Find the longest known first name anywhere inside alphabetic sequences,
#    using the custom name set from CUSTOM_NAMES.py.
# 2. Digit selection (priority):
#    a) 4‑digit year (1999‑2026) that is part of a longer digit block (block length > 4).
#    b) Longest ascending/descending digit sequence (≥3 digits). If tie, last occurrence.
#    c) Default "123".
# 3. If a name is found, return name + chosen digits.
# 4. If no name is found, return original text if digits exist, else original + "123".
# 5. If the result equals the original input, append "123" to force a change.
# ===========================================

import re
from CUSTOM_NAMES import COMMON_NAMES  # import the custom name set

NAME_SET = COMMON_NAMES  # already lowercased in CUSTOM_NAMES.py


# ---------- Digit helpers ----------
def is_ascending(s):
    return all(int(s[i + 1]) - int(s[i]) == 1 for i in range(len(s) - 1))


def is_descending(s):
    return all(int(s[i]) - int(s[i + 1]) == 1 for i in range(len(s) - 1))


def find_best_digits(text):
    """
    Return the best digit string according to priority:
    1. Year (1999‑2026) that is part of a longer digit block (block length > 4).
    2. Longest monotonic (ascending/descending) sequence of length ≥3.
    3. None (then default "123" will be used later).
    """
    digit_blocks = list(re.finditer(r"\d+", text))
    # Step 1: Years inside longer runs
    year_matches = []
    for block in digit_blocks:
        block_text = block.group()
        block_start = block.start()
        block_len = len(block_text)
        if block_len <= 4:
            continue
        for i in range(block_len - 3):
            sub = block_text[i : i + 4]
            year = int(sub)
            if 1999 <= year <= 2026:
                pos = block_start + i
                year_matches.append((pos, sub))
    if year_matches:
        year_matches.sort(key=lambda x: x[0])
        return year_matches[-1][1]

    # Step 2: Longest monotonic sequence (≥3)
    seq_matches = []
    for block in digit_blocks:
        block_text = block.group()
        block_start = block.start()
        block_len = len(block_text)
        for length in range(3, block_len + 1):
            for offset in range(block_len - length + 1):
                sub = block_text[offset : offset + length]
                if is_ascending(sub) or is_descending(sub):
                    pos = block_start + offset
                    seq_matches.append((pos, length, sub))
    if seq_matches:
        best = max(seq_matches, key=lambda x: (x[1], x[0]))
        return best[2]

    return None


def find_longest_name(text):
    """
    Find the longest known first name anywhere inside alphabetic sequences.
    Returns the name (with original casing) and its starting position.
    """
    best_name = None
    best_len = 0
    best_pos = -1

    for m in re.finditer(r"[A-Za-z]+", text):
        token = m.group()
        token_start = m.start()
        token_len = len(token)
        for length in range(2, token_len + 1):
            for start in range(token_len - length + 1):
                sub = token[start : start + length]
                if sub.lower() in NAME_SET:
                    pos = token_start + start
                    if length > best_len or (length == best_len and pos > best_pos):
                        best_len = length
                        best_pos = pos
                        best_name = sub
    return best_name


def transform_text(text):
    name = find_longest_name(text)
    digits = find_best_digits(text)
    result = text  # fallback

    if name:
        if digits:
            result = name + digits
        else:
            result = name + "123"
    else:
        if digits:
            result = text  # original already contains qualifying digits
        else:
            result = text + "123"

    # Ensure result is different from input
    if result == text:
        result = text + "123"

    return result
