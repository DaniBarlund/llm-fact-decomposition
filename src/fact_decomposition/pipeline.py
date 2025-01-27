from src.fact_decomposition.extractors.extractors import FactExtractor
from src.fact_decomposition.verifiers.fact_comparator import (
    FactComparator,
    FactAnalysis,
)
from src.fact_decomposition.utils.document_extractor import DocumentExtractor


class FactDecompositionPipeline:
    """Main pipeline class for fact decomposition and verification."""

    def __init__(self, model: str = "gpt-4o"):
        self.extractor = FactExtractor(model)
        self.comparator = FactComparator(model)
        self.doc_extractor = DocumentExtractor()

    def process_text(self, input_text: str, output_text: str) -> FactAnalysis:
        """
        Process input and output text through the fact decomposition pipeline.

        Args:
            input_text: Source/reference text or path to document
            output_text: Generated text to analyze

        Returns:
            FactAnalysis containing common facts, hallucinations, missing facts,
            and highlighted output
        """
        input_markdown = self.doc_extractor.extract_to_markdown(input_text)
        input_facts = self.extractor.extract(input_markdown)
        return self.comparator.analyze_facts(input_facts, output_text)
