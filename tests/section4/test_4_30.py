from typing import List, Callable


def score(word: str) -> int:
    return len(word.replace("a", ""))


def bonus(word: str) -> int:
    return 5 if "c" in word else 0


def penalty(word: str) -> int:
    return 7 if "s" in word else 0


def high_scoring_words(words: List[str], score: Callable[[str], int]) -> List[str]:
    return list(filter(lambda x: score(x) > 1, words))


def test_pure_func_ranked_words():
    words = ("ada", "haskell", "scala", "java", "rust")
    assert high_scoring_words(words, lambda x: score(x) + bonus(x) - penalty(x)) == [
        "java"
    ]
