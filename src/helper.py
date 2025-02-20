from langchain.embeddings import HuggingFaceEmbeddings

def download_hf_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
    return embeddings