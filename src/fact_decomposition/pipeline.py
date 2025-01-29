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

def main():
    # Sample texts for testing
    reference_text = """
    The Golden Gate Bridge is a suspension bridge spanning the Golden Gate strait. 
    It was opened in 1937 and connects San Francisco to Marin County. 
    The bridge is painted in a distinctive orange color called "International Orange".
    """

    generated_text = """
    The Golden Gate Bridge, opened in 1937, is a famous bridge in San Francisco.
    It is painted orange and connects to Marin County. It's one of the most
    photographed bridges in the world and was designed by Joseph Strauss.
    """

    # Initialize and run pipeline
    pipeline = FactDecompositionPipeline()
    analysis = pipeline.process_text(reference_text, generated_text)

    # Print results
    print("\nCommon Facts:")
    for fact in analysis.common_facts:
        print(f"- {fact}")

    print("\nHallucinations:")
    for fact in analysis.hallucinations:
        print(f"- {fact}")

    print("\nMissing Facts:")
    for fact in analysis.missing_facts:
        print(f"- {fact}")

    print("\nHighlighted Output:")
    print(analysis.highlighted_output)


if __name__ == "__main__":
    main()


