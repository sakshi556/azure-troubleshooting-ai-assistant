from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from rag import retrieve_context


model = ChatOllama(
    model="llama3.2",
    temperature=0
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
"""
You are an Azure Troubleshooting Assistant.

Use only the supplied knowledge context to provide troubleshooting guidance.

Important rules:

1. Never present a possible cause as a confirmed root cause.
2. Distinguish clearly between:
   - Known information from the user's description
   - Possible causes
   - Validation steps
3. If evidence is insufficient, say what evidence is required.
4. Do not invent configuration values, logs, commands, test results, or resource details.
5. Recommend validation before remediation.

Return:

Issue Summary:

Possible Causes:

Troubleshooting Steps:

Recommended Next Action:

Knowledge Context:

{context}
"""
    ),
    (
        "human",
        "{question}"
    )
])


chain = prompt | model


def ask_ai(question):

    context = retrieve_context(question)

    if context is None:
        return (
            "I could not find sufficiently relevant information "
            "in the current Azure troubleshooting knowledge base."
        )

    response = chain.invoke({
        "question": question,
        "context": context
    })

    return response.content