# represents a single request sent from the validator to miners
from typing import List
from pydantic import BaseModel

from template.protocol import RankingRequest


class DendriteQueryResponse(BaseModel):
    class Config:
        allow_mutation = True

    request: RankingRequest
    responses: List[RankingRequest]


class ScoreItem(BaseModel):
    completion_id: str
    score: float


# meant to be used with JSON mode
class ScoresResponse(BaseModel):
    scores: List[ScoreItem]


class PreferenceResponse(BaseModel):
    preference_text: int
