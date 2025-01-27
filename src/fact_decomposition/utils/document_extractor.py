from pathlib import Path
from typing import Union, Optional
from markitdown import MarkItdown


class DocumentExtractor:
    """Utility class for extracting text from various document formats and converting to markdown."""

    def __init__(self):
        self.converter = MarkItdown()

    def extract_to_markdown(
        self,
        file_path: Union[str, Path],
        output_path: Optional[Union[str, Path]] = None,
    ) -> str:
        """
        Extract text from a document and convert it to markdown format.

        Args:
            file_path: Path to the input document
            output_path: Optional path to save the markdown output

        Returns:
            str: Extracted text in markdown format
        """
        file_path = Path(file_path)

        # Convert the document to markdown
        markdown_content = self.converter.convert_file(file_path)

        # Save to file if output path is provided
        if output_path:
            output_path = Path(output_path)
            output_path.write_text(markdown_content, encoding="utf-8")

        return markdown_content

    def extract_from_text(self, text: str) -> str:
        """
        Convert plain text to markdown format.

        Args:
            text: Input text to convert

        Returns:
            str: Text in markdown format
        """
        return self.converter.convert_text(text)
