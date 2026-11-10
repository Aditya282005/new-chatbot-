today is 7th november,
what is pydantic =a python library used for type validation,we do from pydantic import baseModel(M is capital)

create a class Student(baseModel):
name: str
age : int

//create a dictionary to validate
student_data={"name" :"ADITYA",
"age":21}

student= Student(**student_data) unpack it importent
print(student)

with pydantic in ai i did model.structured_output store it in objct
then do this object.invoke


today on 9th,i will do chains concept.i will do cloning! here i did runnables=sequence,parallel,runnablegothrough
work on 10th= im doing document  loaderr
its easy use : its of types TextLoader=converts text(txt)to document object,pfd to document object
how to use= from langchain_community.document_loaders import TextLoader
TextLoader('your filename in txt')
store it in variable say result
do print(result.load())
