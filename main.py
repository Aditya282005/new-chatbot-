from dotenv import load_dotenv
from groq import Groq
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_groq import ChatGroq
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()
client=Groq()
models=client.models.list()
for model in models.data:
  print(model.id)

llm=ChatGroq(model="openai/gpt-oss-20b")
result=llm.invoke("what is pond")
# print(result.content)

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=22)
documents=["virat kholi is indian milf",
           "shame whatson is australian",
           "siya is very beautiful,we all like her body"
           ]

query='tell me about siya'
doc_embedding=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)
print(cosine_similarity([query_embedding],  doc_embedding))





# response=client.chat.completions.create(
#          model="openai/gpt-oss-safeguard-20b",
#          messages=[{
#              "role":"user",
#            "content": "hello,who are you"
#          }]
#      )
#     print(response.choices[0].message.content)


# prompt=PromptTemplate.from_template(
#         'Summarize {topic} in {emotion} tone'
#     )
# print(prompt.format(topic='cricket',emotion='fun'))
