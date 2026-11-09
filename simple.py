from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
prompt=PromptTemplate(
    template='genrate 5 interesting facts about {topic}',
    input_variable=['topic']
)
model=ChatGroq(model="openai/gpt-oss-20b")

parser=StrOutputParser()
chain=prompt | model 
result=chain.invoke({'topic' : 'cricket'})
print(result)
