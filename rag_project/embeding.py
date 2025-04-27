from langchain_google_genai import GoogleGenerativeAIEmbeddings
from creating_index import index
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from google_genaiAPI import google_api
print ("embeding index",index)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=google_api
)
vector = embeddings.embed_query("hello, this is muhammad suleman and i am learning agentic ai. and hopefully i will be able to learn it")
vector[:5]
#vector store we can easily use other vector datastore like cromma by just changing the vectorstore

from langchain_pinecone import PineconeVectorStore

vector_store = PineconeVectorStore(index=index, embedding=embeddings)