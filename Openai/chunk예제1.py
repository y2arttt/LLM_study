from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
)


loader = PyPDFLoader("law1.pdf")
pages = loader.load_and_split()
text_splitter = RecursiveCharacterTextSplitter(   #청크를 나누는데 사용
    separators = "\n \n",   # 구분자
    chunk_size = 400, # 청크의 최대 길이
    chunk_overlap  = 100, # 청크의 겹침
    length_function = len, # 길이 계산
    is_separator_regex = False, #정규식인지
)
texts = text_splitter.split_documents(pages)


from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
embedding_function = SentenceTransformerEmbeddings(model_name="jhgan/ko-sroberta-multitask")

from langchain.vectorstores import FAISS
db = FAISS.from_documents(texts, embedding_function)

from langchain_community.chat_models import ChatOllama
llm = ChatOllama(model="qwen2:1.5b", temperature=0,
base_url="http://127.0.0.1:11434/") #http://127.0.0.1:11434

from langchain.chains import RetrievalQA
question = """신의성실의 원칙은 민법 몇 조이니?"""
qa_chain = RetrievalQA.from_chain_type(llm,retriever=db.as_retriever())
result = qa_chain({"query": question})
print(result['result'])

retriever = db.as_retriever(search_type="similarity", search_kwargs={'k':5, 'fetch_k': 100})
retriever.get_relevant_documents("혈족을 설명해주세요.")