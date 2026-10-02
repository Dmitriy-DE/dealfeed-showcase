from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Opportunity:
    side: str
    vertical: Optional[str]
    geo: Optional[str]
    source: Optional[str]
    payout: Optional[float]


@dataclass(frozen=True)
class Match:
    score: int
    demand: Opportunity
    supply: Opportunity


def match(demand: Opportunity, supply: Opportunity) -> Optional[Match]:
    if demand.side != "BUY" or supply.side != "SELL":
        return None

    score = 0

    if demand.vertical and supply.vertical:
        if demand.vertical != supply.vertical:
            return None
        score += 40

    if demand.geo and supply.geo:
        if demand.geo != supply.geo:
            return None
        score += 30

    if demand.source and supply.source and demand.source == supply.source:
        score += 20

    # Missing values remain missing. They are not invented to improve a match.
    return Match(score=score, demand=demand, supply=supply)
