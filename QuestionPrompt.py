import os

import openai
from langchain import PromptTemplate, OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

OPENAI_API_KEY = "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"
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

def createFAQDB():
    f = open("assets/summer_camp_summary.txt")
    info = f.read()
    f.close()

    f = open("prompts/generate_faq_prompt.txt")
    prompt = f.read()
    f.close()

    messages = [
        {"role": "system", "content": info},
        {"role": "user", "content": prompt},
    ]

    max_tokens = 14000  # Set the maximum token limit
    temperature = 1
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        max_tokens=max_tokens,
        temperature=temperature,
        messages=messages)

    q_a = response.choices[0].message.content
    f = open("assets/summer_camp_faq.txt", "w")
    f.write(q_a)
    f.close()


def dbLoader():
    loader = DirectoryLoader("assets", glob="*.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    docsearch = Chroma.from_documents(texts, embeddings)
    return  docsearch

docsearch = dbLoader()

f = open("prompts/question_prompt.txt")
faq_template = f.read()
f.close()

PROMPT = PromptTemplate(
    template=faq_template,
    input_variables=["context", "question"]
)

chain_type_kwargs = {"prompt": PROMPT}
qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(temperature=0), chain_type="stuff", retriever=docsearch.as_retriever(),
                                       chain_type_kwargs=chain_type_kwargs,)

def complete(input_data: str):
    return qa_chain.run(query=input_data)

if __name__ == '__main__':
    input_data = ""
    print("Welcome to GenAi QA assistant (type exit to stop)")
    while input_data != "exit":
        print("How can I help?")
        input_data = input()
        if input_data.lower() == "exit":
            break
        response = complete(input_data)
        print(response)

    print("Bye bye")