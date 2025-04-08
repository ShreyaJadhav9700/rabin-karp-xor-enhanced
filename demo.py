from xor_filter import XORFilter
from rabin_karp_xor import rolling_hash

def rabin_karp_with_xor(text, pattern):
    m, n = len(pattern), len(text)
    base, prime = 256, 101
    xor_filter = XORFilter()

    pattern_hash = rolling_hash(pattern, base, prime)
    xor_filter.add(pattern_hash)

    results = []

    for i in range(n - m + 1):
        substr = text[i:i + m]
        substr_hash = rolling_hash(substr, base, prime)
        if xor_filter.contains(substr_hash):
            if substr == pattern:
                results.append(i)
    return results

if __name__ == "__main__":
    text = "This is a simple example where the pattern example appears."
    pattern = "example"
    matches = rabin_karp_with_xor(text, pattern)
    print("Pattern found at indices:", matches)
