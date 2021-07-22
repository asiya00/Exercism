from typing import List
def latest(scores: int) -> int:
    return scores[-1]

def personal_best(scores: int) -> int:
    return max(scores)

def personal_top_three(scores: int) -> List[int]:
    return sorted(scores,reverse=True)[:3]
