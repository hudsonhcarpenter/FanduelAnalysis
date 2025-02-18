import csv
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key )

# with open("transcripts2.csv") as f:
#   reader = csv.DictReader(f)
#   for line in reader:
#     segmented_transcript = ""
#     segment_list = line['transcript'].split(r"\n")
#     for i in range(len(segment_list)):
#       segmented_transcript += f"Paragraph {i}: {segment_list[i]}\n"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)
      

