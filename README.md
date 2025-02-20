# Medical-Chatbot-using-RAG

<hr>

# How to Run?

## Steps:

### Clone the Repository  

Project repo: [https://github.com/ashwinikumar2003/Medical-Chatbot-using-RAG.git](https://github.com/ashwinikumar2003/Medical-Chatbot-using-RAG.git)

### STEP 01 - Create a Conda Environment  

After opening the repository, run the following commands:  

```bash
conda create -n medbot python=3.10 -y
conda activate medbot
```

### STEP 02 - Install the Requirements

```bash
pip install -r requirements.txt
```

### Configure Environment Variables
Create a .env file in the root directory and add your Pinecone & ChatGroq credentials as follows:

### Run the Application
```bash
python app.py
```

Now, open up localhost in your browser.

## Technology Used:
- Python
- LangChain
- Flask
- Groq
- Pinecone