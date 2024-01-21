from typing import List, Callable


def score(word: str) -> int:
    return len(word.replace("a", ""))


def score_with_bonus_and_penalty(word: str) -> int:
    score = 0
    if "c" in word:
        score += 5
    if "s" in word:
        score -= 7
    score += len(word.replace("a", ""))
    return score


def pure_func_ranked_words(words: List[str], key: Callable[[str], int]) -> List[str]:
    return sorted(words, key=key, reverse=True)


def test_pure_func_ranked_words():
    words = ["ada", "haskell", "scala", "java", "rust"]
    assert pure_func_ranked_words(words, score_with_bonus_and_penalty) == [
        "java",
        "ada",
        "scala",
        "haskell",
        "rust",
    ]
    assert words == ["ada", "haskell", "scala", "java", "rust"]


# 別解


def bonus(word: str) -> int:
    return 5 if "c" in word else 0


def penalty(word: str) -> int:
    return 7 if "s" in word else 0


def test_pure_func_ranked_words():
    words = ["ada", "haskell", "scala", "java", "rust"]
    assert pure_func_ranked_words(
        words, lambda x: score(x) + bonus(x) - penalty(x)
    ) == [
        "java",
        "ada",
        "scala",
        "haskell",
        "rust",
    ]
    assert words == ["ada", "haskell", "scala", "java", "rust"]
