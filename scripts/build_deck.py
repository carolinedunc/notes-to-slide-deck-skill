from pptx import Presentation 
from pptx.util import Inches 

from parse_notes import parse_sections
from expand_notes import expand_note
from branded_deck import add_brand_slide

def build_deck(notes, output):
      with open(notes, "r") as f:
            notes = f.read()

      sections = parse_sections(notes)

      pres = Presentation()
      pres.slide_width = Inches(10)
      pres.slide_height = Inches(5.5)

      for x, (title, bullets) in enumerate(sections):
            expandedBullet = [expand_note(b) for b in bullets]
            add_brand_slide(pres, title, x + 1, bullets=expandedBullet)

      pres.save(output)
      print(f"Saved {len(sections)} slides to {output}")

if __name__ == "__main__":
    build_deck("../example/notes.md", "../example/final_deck.pptx")
