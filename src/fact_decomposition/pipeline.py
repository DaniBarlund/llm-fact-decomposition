from typing import List, Dict, Any

class FactDecompositionPipeline:
    """Main pipeline class for fact decomposition and verification."""
    
    def __init__(self, extractor=None, verifier=None):
        self.extractor = extractor
        self.verifier = verifier
    
    def process_text(self, text: str) -> Dict[str, Any]:
        """
        Process input text through the fact decomposition pipeline.
        
        Args:
            text: Input text to process
            
        Returns:
            Dictionary containing extracted facts and their verification status
        """
        facts = self.extract_facts(text)
        verified_facts = self.verify_facts(facts)
        return {
            "facts": facts,
            "verification": verified_facts
        }
    
    def extract_facts(self, text: str) -> List[str]:
        """Extract facts from input text."""
        if self.extractor is None:
            raise ValueError("No fact extractor configured")
        return self.extractor.extract(text)
    
    def verify_facts(self, facts: List[str]) -> List[Dict[str, Any]]:
        """Verify extracted facts."""
        if self.verifier is None:
            raise ValueError("No fact verifier configured")
        return self.verifier.verify(facts)