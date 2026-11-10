from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
model=ChatGroq(model="openai/gpt-oss-20b")
prompt=PromptTemplate(
    template= 'write a summary for {poem}'
)
parser=StrOutputParser()

loader= TextLoader('cricket.txt')
docs=loader.load()
chain=prompt|model|parser
print(chain.invoke({'poem':docs[0].page_content}))