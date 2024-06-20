from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
 )
with open('law1.txt', 'r', encoding='utf-8') as file:
    text = file.read()
   
text_splitter = RecursiveCharacterTextSplitter(  
    separators = ["\n\n"],    
    chunk_size = 250,
    chunk_overlap  = 100,
    length_function = len,
    is_separator_regex = False,
 )
texts = text_splitter.create_documents([text])

from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
embedding_function = SentenceTransformerEmbeddings(model_name="jhgan/ko-sroberta-multitask")

from langchain.vectorstores import FAISS
db2 = FAISS.from_documents(texts, embedding_function )

retriever = db2.as_retriever(search_type="similarity", 
search_kwargs={'k':5, 'fetch_k': 100})
q1 = retriever.invoke("혈족을 설명해주세요.")
print(q1)