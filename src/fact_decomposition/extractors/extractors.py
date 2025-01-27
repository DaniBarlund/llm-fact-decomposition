from typing import List
from pydantic import BaseModel
from openai import OpenAI


class FactList(BaseModel):
    facts: List[str]


class FactExtractor:
    """Extracts facts from text using OpenAI's API with structured output."""

    def __init__(self, model: str = "gpt-4"):
        self.client = OpenAI()
        self.model = model

    def extract(self, text: str) -> List[str]:
        completion = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "Extract atomic facts from the text given to you. Only list the facts and nothing else.",
                },
                {"role": "user", "content": text},
            ],
            response_format=FactList,
        )
        return completion.choices[0].message.parsed.facts
