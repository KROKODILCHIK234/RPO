def reverse_string(s: str) -> str:
    """Переворачивает строку."""
    return s[::-1]

def remove_vowels(s: str) -> str:
    """Удаляет гласные из строки."""
    vowels = "aeiouAEIOU"
    return "".join(char for char in s if char not in vowels)

def char_count(s: str) -> dict:
    """Подсчитывает количество каждого символа в строке."""
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return counts
