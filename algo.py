# ===========================================
# ALGO.PY - Generate possible outputs for name+digit extraction
# ===========================================
# Rules:
# 1. Find all known first names anywhere inside alphabetic sequences.
# 2. Find all valid years (1999‑2026) that are part of a longer digit block.
# 3. Find all ascending/descending digit sequences (≥3 digits).
# 4. Combine each name with each digit option, plus a fallback with "123".
# 5. If no name, use the original text (if it has digits) or original+"123".
# 6. Return a sorted list of unique candidates (years first, then longer monotonic).
# 7. Only include candidates with length >= 8 characters.
# 8. NEVER include a candidate that is exactly the original input.
# ===========================================

import re
from CUSTOM_NAMES import COMMON_NAMES

NAME_SET = COMMON_NAMES


# ---------- Digit helpers ----------
def is_ascending(s):
    return all(int(s[i + 1]) - int(s[i]) == 1 for i in range(len(s) - 1))


def is_descending(s):
    return all(int(s[i]) - int(s[i + 1]) == 1 for i in range(len(s) - 1))


def find_all_names(text):
    """Return list of all distinct names found in text (longest substring matches)."""
    names = set()
    for m in re.finditer(r"[A-Za-z]+", text):
        token = m.group()
        token_len = len(token)
        for length in range(2, token_len + 1):
            for start in range(token_len - length + 1):
                sub = token[start : start + length]
                if sub.lower() in NAME_SET:
                    names.add(sub)
    # Return sorted by length descending (longer names first) then alphabetically
    return sorted(names, key=lambda x: (-len(x), x))


def find_all_years(text):
    """Return list of all valid years (1999-2026) that are inside a longer digit block."""
    years = set()
    digit_blocks = list(re.finditer(r"\d+", text))
    for block in digit_blocks:
        block_text = block.group()
        block_len = len(block_text)
        if block_len <= 4:
            continue
        for i in range(block_len - 3):
            sub = block_text[i : i + 4]
            year = int(sub)
            if 1999 <= year <= 2026:
                years.add(sub)
    return list(years)


def find_all_monotonic(text):
    """Return list of all ascending/descending sequences of length ≥3."""
    seqs = set()
    digit_blocks = list(re.finditer(r"\d+", text))
    for block in digit_blocks:
        block_text = block.group()
        block_len = len(block_text)
        for length in range(3, block_len + 1):
            for offset in range(block_len - length + 1):
                sub = block_text[offset : offset + length]
                if is_ascending(sub) or is_descending(sub):
                    seqs.add(sub)
    # Return sorted by length descending
    return sorted(seqs, key=lambda x: (-len(x), x))


def generate_candidates(text):
    """
    Return a list of possible output strings based on the input.
    Candidates are sorted by priority and filtered to length >= 8.
    NEVER includes the original input itself.
    """
    candidates = set()
    names = find_all_names(text)
    years = find_all_years(text)
    monos = find_all_monotonic(text)

    # Priority 1: name + year
    if names and years:
        for name in names:
            for year in years:
                candidates.add(name + year)

    # Priority 2: name + monotonic
    if names and monos:
        for name in names:
            for mono in monos:
                candidates.add(name + mono)

    # Priority 3: name + "123" (if no digits at all)
    if names and not years and not monos:
        for name in names:
            candidates.add(name + "123")

    # If no name found, consider original text if it contains qualifying digits
    if not names:
        if years or monos:
            candidates.add(text)
        else:
            # No name and no qualifying digits: append "123"
            candidates.add(text + "123")

    # Always include original text as an option? No – we will remove it if present.
    # We add it only as a fallback if nothing else exists, but we'll handle that later.
    # Actually, we might need the original for cases where it contains digits but no name.
    # But we will remove it if it appears, and if after removal there's nothing, we create a new one.

    # Remove trailing spaces
    candidates = {c.rstrip() for c in candidates}

    # Remove the original input itself (if present)
    candidates.discard(text)

    # Filter by length >= 8
    candidates = {c for c in candidates if len(c) >= 8}

    # If after filtering we have no candidates, create a fallback that's different from input
    if not candidates:
        # Try to create something like "default123" or input + "123"
        fallback = text + "123"
        # Ensure fallback is at least 8 chars (if text is short, it might be less)
        if len(fallback) < 8:
            fallback = "default123"  # 9 chars, guaranteed different
        candidates.add(fallback)

    # Sort candidates in priority order
    def candidate_key(c):
        has_year = any(year in c for year in years) if years else False
        if has_year:
            return (0, -len(c), c)
        has_mono = any(mono in c for mono in monos) if monos else False
        if has_mono:
            mono_len = 0
            for mono in monos:
                if mono in c:
                    mono_len = max(mono_len, len(mono))
            return (1, -mono_len, -len(c), c)
        return (2, -len(c), c)

    sorted_candidates = sorted(candidates, key=candidate_key)
    return sorted_candidates
