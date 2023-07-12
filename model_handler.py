from cryptography.fernet import Fernet
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

index_name = 'v1-index-pinecone'
text_field = "text"

with open("key.key", "rb") as key_file:
    key =  key_file.read()
with open("encrypted.key", "rb") as encrypted_message:
    encrypted_message =  encrypted_message.read()

fernet = Fernet(key)
decrypted_message = fernet.decrypt(encrypted_message)
OPENAI_API_KEY = decrypted_message.decode()

def initialize_model(model_type):
    llm = ChatOpenAI(model_name=model_type, openai_api_key=OPENAI_API_KEY, temperature=0.0)
    return llm

def return_ai_response(llm,input_question, vectorstore): 
    # template = "Answer the question as an expert on LAU only. Question: {question}."
    # prompt = PromptTemplate(template=template, input_variables=["question"])
    # output = prompt.format(question=input_question)
    # llm = OpenAI(model_name=model_name, openai_api_key=OPENAI_API_KEY)
    # print(input_question)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever()) 
    response = qa.run(input_question)
    return response

# def get_vector_store():
#     vectorstore = intialize_vector_store()
#     return vectorstore

def return_open_api_key():
    return OPENAI_API_KEY
