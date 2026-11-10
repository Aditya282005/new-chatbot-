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
documents=["virat kholi is indian",
           "shame whatson is australian",
           "chris gayle"
           ]

query='tell me about virat kholi'
doc_embedding=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)
score=(cosine_similarity([query_embedding],  doc_embedding))
index,score=sorted(list(enumerate(score)),key=lamda x:x[1])[-1]
print(query)
print(document[index])
print("vector similarity",score)


















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
