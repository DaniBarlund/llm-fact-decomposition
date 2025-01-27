from typing import List, Set
from pydantic import BaseModel
from openai import OpenAI

from src.fact_decomposition.extractors.extractors import FactExtractor, FactList


class FactAnalysis(BaseModel):
    common_facts: List[str]
    hallucinations: List[str]
    missing_facts: List[str]
    highlighted_output: str


class FactComparator:
    def __init__(self, model: str = "gpt-4o"):
        self.client = OpenAI()
        self.model = model

    def analyze_facts(self, input_facts: List[str], output_text: str) -> FactAnalysis:
        # Extract facts from output text
        completion = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """You will be provided with a list of facts and a text content.
                    Your job is to detect the facts into the following categories: common_facts, hallucinations, missing_facts.

                    where common_facts are the facts that are present in both the input and output lists.
                    hallucinations are the facts that are present in the output text but not in the input list.
                    missing_facts are the facts that are present in the input list but not in the output text.

                    After the analysis, highlight facts in the output text using markdown.
                    
                    Highlighting rules:
                    1. Common_facts should be highlighted as green
                    2. Hallucinations should be highlighted as red
                    """,
                },
                {"role": "user", "content": input_facts},
                {"role": "user", "content": output_text},
            ],
            response_format=FactAnalysis,
        )
        return completion.choices[0].message.parsed
