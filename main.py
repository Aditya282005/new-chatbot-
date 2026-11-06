from dotenv import load_dotenv
from groq import Groq
from langchain_core.prompts import PromptTemplate
load_dotenv()
client=Groq()
models=client.models.list()
for model in models.data:
    print(model.id)


    response=client.chat.completions.create(
        model="openai/gpt-oss-safeguard-20b",
        messages=[{
            "role":"user",
            "content": "hello,who are you"
        }]
    )
    print(response.choices[0].message.content)


    prompt=PromptTemplate.from_template(
        'Summarize {topic} in {emotion} tone'
    )
    print(prompt.format(topic='cricket',emotion='fun'))