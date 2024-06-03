from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import chainlit as cl

DB_FAISS_PATH = 'vectorstore/db_faiss'

# Define your prompt template
custom_prompt_template = """Use the following pieces of information to answer the user's question.


Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

def set_custom_prompt():
    prompt = PromptTemplate(template=custom_prompt_template,
                            input_variables=['context', 'question'])
    return prompt

# Define your Retrieval QA Chain function
def retrieval_qa_chain(llm, prompt, db):
    qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type='stuff',
                                       retriever=db.as_retriever(search_kwargs={'k': 2}),
                                       return_source_documents=True,
                                       chain_type_kwargs={'prompt': prompt}
                                       )
    return qa_chain

# Define your model loading function
def load_llm():
    llm = CTransformers(
        model="TheBloke/Llama-2-7B-Chat-GGML",
        model_type="llama",
        max_new_tokens=512,
        temperature= 0.7
    )
    return llm

# Define your QA model function
def qa_bot():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, db)

    return qa

# Define your function to answer questions
def answer_question(query):
    qa_result = qa_bot()
    response = qa_result({'query': query})
    return response

# Define your ChainLit functions
@cl.on_chat_start
async def start():
    chain = qa_bot()
    cl.user_session.set("chain", chain)  # Set the chain object in the user session
    msg = cl.Message(content="Nela is booting...")
    await msg.send()
    msg.content = "Hi, I am Nela your Health Advisor. What is your query?"
    await msg.update()


@cl.password_auth_callback
def auth_callback(username: str, password: str):
    # Fetch the user matching username from your database
    # and compare the hashed password with the value stored in the database
    if (username, password) == ("admin", "admin"):
        return cl.User(
            identifier="admin", metadata={"role": "admin", "provider": "credentials"}
        )
    else:
        return None




@cl.on_message
async def main(message: cl.Message):
    # Send initial processing message
    processing_msg = cl.Message(content="")
    await processing_msg.send()

    # Get the chain object
    chain = cl.user_session.get("chain") 

    # Initialize callback handler
    cb = cl.AsyncLangchainCallbackHandler(
        stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]
    )
    cb.answer_reached = True

    # Invoke the chain with the message content
    res = await chain.ainvoke(message.content, callbacks=[cb])
    answer = res["result"]

    # Update the processing message with the result
    processing_msg.content = answer
    await processing_msg.update()