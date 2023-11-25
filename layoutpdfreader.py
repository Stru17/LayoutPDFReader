import llmsherpa
from llmsherpa.readers import LayoutPDFReader
from llama_index.llms import OpenAI
from llama_index.readers.schema.base import Document
from llama_index import VectorStoreIndex
import openai
from IPython.core.display import display, HTML

# Load LLMSherpa API and PDF
llmsherpa_api_url = "https://readers.llmsherpa.com/api/document/developer/parseDocument?renderFormat=all"
pdf_url = "https://omscs.gatech.edu/sites/default/files/documents/Other_docs/spring_2023_orientation_document.pdf" # also can do file path
pdf_reader = LayoutPDFReader(llmsherpa_api_url)
doc = pdf_reader.read_pdf(pdf_url)

#Insert OpenAI API key
openai.api_key = ""

# Method 1: Select Section
selected_section = None
x = 0
# LLMSherap splits the pdf into multiple sections. If there are multiple sections with the same name (can be due to Table of Contents), then you must iterate to the correct section
for section in doc.sections():
    if section.title == 'SECTION B. FOUNDATIONAL COURSE REQUIREMENT' and x == 1:
        selected_section = section
        break
    elif section.title == 'SECTION B. FOUNDATIONAL COURSE REQUIREMENT':
        x += 1
# Otherwise, this code will suffice
# for section in doc.sections():
#     if section.title == 'SECTION B. FOUNDATIONAL COURSE REQUIREMENT':
#         selected_section = section
#         break

# include_children returns one sublevel of children
# recurse returns all the descendants
HTML(section.to_html(include_children = True, recurse = True))

# Ask OpenAI a question about the selected section
context = selected_section.to_html(include_children=True, recurse=True)
question = "list all the tasks discussed and one line about each task"
resp = OpenAI().complete(f"read this text and answer question: {question}:\n{context}")
print(resp.text)

# Method 2: Vector Search and RAG with Smart Chunking
index = VectorStoreIndex([])
for chunk in doc.chunks():
    index.insert(Document(text=chunk.to_context_text(), extra_info={}))
query_engine = index.as_query_engine()

# Ask a question about the PDF file!
response = query_engine.query("what are some key points in foundational course requirement")
print(response)
response = query_engine.query("what are the systems in the table for SECTION I. SYSTEMS YOU WILL BE USING AND WHY")
print(response)

# Extra 
# Can also parse through tables
# However, this method is not always perfect, it is better to just still use the Vector Search and RAG method
HTML(doc.tables()[11].to_html())
context = doc.tables()[11].to_html()
resp = OpenAI().complete(f"read this table and answer question: what are the systems in the table for SECTION I. SYSTEMS YOU WILL BE USING AND WHY:\n{context}")
print(resp.text)
