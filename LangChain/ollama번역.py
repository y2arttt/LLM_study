from langchain_core.prompts import SystemMessagePromptTemplate,  HumanMessagePromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableMap, RunnableLambda



question = input("질문: ")
lang = input("언어를 선택해주세요.")
llm = ChatOllama(model="qwen2:1.5b", temperature=0, base_url="http://127.0.0.1:11434/") #http://127.0.0.1:11434
prompt2 = ChatPromptTemplate.from_messages([SystemMessagePromptTemplate.from_template("""
                                            # Instruction
                                            당신은 번역가입니다. 다음에 주어진 문장을 {lang}로 번역해주세요.                                                                                      
                                            """),
                                            HumanMessagePromptTemplate.from_template("""
                                            # Text
                                            {text}                                          
                                            # Result""")])
output_parser = StrOutputParser()
chain2 = RunnableMap({"text": RunnableLambda(lambda x: chain1), "lang": RunnableLambda(lambda x: lang)}) | prompt2 | llm | output_parser
print(question)
print(lang)
chain2.invoke({"input": question})