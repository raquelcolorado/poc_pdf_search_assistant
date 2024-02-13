#!/usr/bin/env python3
import openai
import sys
import os
from fpdf import FPDF

import pdf_reader
import lookup
import gpt

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    openai.api_key = input("Please enter your OpenAI API key: ")
    print()

program_name = sys.argv.pop(0)

if len(sys.argv):
    pdf_file = sys.argv.pop(0)
else:
    pdf_file = input("Please enter the PDF file you want to read: ")
    print()

    while not os.path.exists(pdf_file):
        print("ERROR: File not found")
        pdf_file = input("Please enter the PDF file you want to read: ")
        print()

if len(sys.argv):
    chunk_size = int(sys.argv.pop(0))
else:
    chunk_size = 4000

if len(sys.argv):
    overlap = int(sys.argv.pop(0))
else:
    overlap = 1000

if len(sys.argv):
    limit = int(sys.argv.pop(0))
else:
    limit = 5

if len(sys.argv):
    gpt.model = sys.argv.pop(0)
else:
    gpt.model = "gpt-3.5-turbo"

print("Chunking PDF...\n")
chunks = pdf_reader.chunk_pdf(pdf_file, chunk_size, overlap)

# Initialize an empty conversation list
conversation = []


def save_conversation_to_pdf(conversation, filename='conversation.pdf'):
    pdf = FPDF()
    pdf.add_page()

    for role, message in conversation:
        if role == 'user':
            pdf.set_font("Arial", size= 10)
            pdf.multi_cell(0, 10, txt=f"Question: {message}", align='L')
        elif role == 'assistant':
            pdf.set_font("Arial", 'I', size=10)
            pdf.multi_cell(0, 10, txt=f"Answer: {message}", align='L')

    pdf.output(filename)


while True:
    question = input("GPT: What do you want to know?\nYou: ")
    print()
    keywords = gpt.get_keywords(question)

    print("Searching: " + ", ".join(keywords) + "")

    matches = lookup.find_matches(chunks, keywords)

    for i, chunk_id in enumerate(matches.keys()):
        print(".", end="", flush=True)

        chunk = chunks[chunk_id]
        response = gpt.answer_question(chunk, question)

        if response.get("answer_found"):
            print("\n\nGPT: " + str(response.get("response")) + "\n")

            # Append the user's question and GPT's response to the conversation
            conversation.append(("user", question))
            conversation.append(("assistant", response.get("response")))

            # Save the conversation to a PDF file
            save_conversation_to_pdf(conversation)

            break

        if i > limit:
            break

    if not response.get("answer_found"):
        print("\n\nGPT: I'm sorry, but I can't find that information\n")
