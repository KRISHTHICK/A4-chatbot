import openai
import os

# Load your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def load_documents(directory):
    documents = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r') as file:
                documents[filename] = file.read()
    return documents

def answer_query(query, documents):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Answer the following query based on the provided documents: {query}\n\nDocuments:\n{documents}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    documents = load_documents('financial_documents')
    while True:
        query = input("Enter your query: ")
        answer = answer_query(query, documents)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
