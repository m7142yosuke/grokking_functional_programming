from typing import List, Callable


def score(word: str) -> int:
    return len(word.replace("a", ""))


# memo:純粋関数では、シグネイチャを見るだけで関数内で行われる処理がわかるようにする必要がある。そのため、ソートのアルゴリズムを引数に取るようにする。
def pure_func_ranked_words(words: List[str], key: Callable[[str], int]) -> List[str]:
    return sorted(words, key=key, reverse=True)

# memo:既存の値を変更する以下の関数は純粋関数ではない。
def not_pure_func_ranked_words(words: List[str], key: Callable[[str], int]) -> List[str]:
    words.sort(key=key, reverse=True)
    return words


def test_pure_func_ranked_words():
    words = ["ada", "haskell", "scala", "java", "rust"]
    assert pure_func_ranked_words(words, score) == [
        "haskell",
        "rust",
        "scala",
        "java",
        "ada",
    ]
    assert words == ["ada", "haskell", "scala", "java", "rust"]


def test_not_pure_func_ranked_words():
    words = ["ada", "haskell", "scala", "java", "rust"]
    assert not_pure_func_ranked_words(words, score) == [
        "haskell",
        "rust",
        "scala",
        "java",
        "ada",
    ]
    assert words == ["haskell", "rust", "scala", "java", "ada"]
