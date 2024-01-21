from typing import List, Callable


def score(word: str) -> int:
    return len(word.replace("a", ""))


def score_with_bonus(word: str) -> int:
    score = 0
    if "c" in word:
        score += 5
    score += len(word.replace("a", ""))
    return score


def pure_func_ranked_words(words: List[str], key: Callable[[str], int]) -> List[str]:
    return sorted(words, key=key, reverse=True)


def test_pure_func_ranked_words():
    words = ["ada", "haskell", "scala", "java", "rust"]
    assert pure_func_ranked_words(words, score_with_bonus) == [
        "scala",
        "haskell",
        "rust",
        "java",
        "ada",
    ]
    assert words == ["ada", "haskell", "scala", "java", "rust"]
