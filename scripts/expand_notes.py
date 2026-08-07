import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
anth = Anthropic()

def expand_note(org_text):
      response = anth.messages.create(model="claude-sonnet-4-6", 
                                      max_tokens=200, 
                                      system="Expand the following note into one complete, natural sentence. Only add connective words and phrasing to make it read naturally — do not add new facts, numbers, or information that isn't in the original note, and do not make assumptions about missing context.",
                                      messages=[{"role":"user", "content": org_text}])
      exp_text = response.content[0].text
      return exp_text

if __name__ == "__main__":
    print(expand_note("conveyor motors aging, need replacement"))
    print(expand_note("revenue guidance of $100M for the quarter"))