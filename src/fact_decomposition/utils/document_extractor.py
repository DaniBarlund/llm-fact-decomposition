from pathlib import Path
from typing import Union, Optional
from markitdown import MarkItDown


class DocumentExtractor:
    """Utility class for extracting text from various document formats and converting to markdown."""

    def __init__(self):
        self.converter = MarkItDown()

    def extract_to_markdown(
        self,
        input_value: str,
    ) -> str:
        """
        Extract text from a document and convert it to markdown format.

        Args:
            input_value: Path to the input document or plain text content

        Returns:
            str: Extracted text in markdown format
        """

        possible_path = Path(input_value)
        if (
            possible_path.exists()
            or possible_path.is_absolute()
            or possible_path.suffix
        ):
            # Convert the document to markdown
            markdown_content = self.converter.convert(input_value).text_content
        else:
            markdown_content = input_value

        return markdown_content
