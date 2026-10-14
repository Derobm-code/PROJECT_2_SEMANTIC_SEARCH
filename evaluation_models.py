from pydantic import BaseModel

class FactEvaluation(BaseModel):
    fact: str
    covered: bool
    supported_by_context: bool

class GenerationEvaluation(BaseModel):
    passed: bool
    answers_question: bool
    facts: list[FactEvaluation]
    unsupported_claims: list[str]


