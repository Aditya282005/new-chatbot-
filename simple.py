from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
prompt=PromptTemplate(
    template='advantages about {topic}'
    
)

prompt1=PromptTemplate(
    template='genrate disadvatages of {topic}'
    
)
model=ChatGroq(model="openai/gpt-oss-20b")

parser=StrOutputParser()
result=RunnableSequence(prompt1,model,parser)

result1=result.invoke({'topic' : 'ai'})
print(result1)
