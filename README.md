#  POC - PDF Document Search with AI Assistance
This Proof of Concept (POC) demonstrates a PDF document search system with AI assistance. The system utilizes Python scripts to chunk PDF documents, search for keywords, and provide answers to user queries using the OpenAI API and natural language queries. 
The system is designed to:

- Extract text from PDF files.
- Divide the text into smaller chunks for efficient processing.
- Identify keywords and synonyms provided by the user.
- Search for relevant information within the PDF based on the provided keywords.
- Provide responses to user queries using an AI-based model (OpenAI's GPT-3).

## Files

### `pdf_reader.py`

This file contains a function `chunk_pdf` that reads a PDF file and splits its text into smaller chunks. This is useful for processing large PDF documents efficiently.

### `lookup.py`

This file contains a function `find_matches` that searches for matches of keywords within the text chunks extracted from the PDF. It ranks the matches based on relevance and returns the results.

### `gpt.py`

This file interacts with OpenAI's GPT-3 model to perform two main tasks:

1. `get_keywords(question)`: This function takes a user's question as input and prompts the user to provide keywords and synonyms. It then extracts and returns the keywords from the user's input.

2. `answer_question(chunk, question)`: This function takes a chunk of text from the PDF and the user's question as input. It prompts the user to answer the question based on the provided text and returns the response along with whether the answer was found in the text.

### `conversation.py`

This script orchestrates the interaction with the user. It prompts the user for questions, extracts keywords, searches for answers within the PDF, and maintains a conversation log. It also saves the conversation log to a PDF file.

## Usage

To use the intelligent PDF reader:

1. Ensure you have the necessary dependencies installed. You can install them using the following command:
    ```
    pip install -r requirements.txt
    ```
   Make sure to have Python installed in your environment.

2. Set up your OpenAI API key as an environment variable named `OPENAI_API_KEY` in a `.env` file.

3. Run the `conversation.py` script and follow the prompts to ask questions and retrieve answers from the PDF.

## Requirements

Ensure you have the following dependencies installed:

- `PyPDF2`
- `openai`
- `fpdf`


## Files to be read

If you want to process specific PDF files, make sure to include the file paths in the `conversation.py` script or provide them as command-line arguments when running the script.

---


