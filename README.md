# LLMSherpa and LayoutPDFReader Enhancement for EvaDB

## Introduction
This project focuses on enhancing the PDF Reader script and Story QA application in EvaDB. The improved script is crucial for effectively extracting information from PDFs for Text Analysis. A key application that cana be improved with this project is the Story QA application.

## Implementation
The project utilizes LLMSherpa's API and LayoutPDFReader model to parse PDFs while keeping their layout intact. This includes extracting sections, paragraphs, lists, and tables. The extracted data is then fed into ChatGPT via OpenAI’s API so the user can ask questions about the data. Manual section selection is needed due to LayoutPDFReader's method of dividing documents into sections and can be inconsistent and a burden. However, the implementation of Vector Search and RAG with Smart Chunking using llama_index library improves text analysis and querying efficiency. This method, preferable for running in Jupyter notebooks, stores text chunks as vectors and utilizes NLP for querying, though it may sometimes return no answer based on the contents extracted.

## Sample Input/Output
Sample input and output can be seen in the report.

## Requirements:
Ensure the following libraries are installed:

```plaintext
openai
IPython
llmsherpa
llama-index
