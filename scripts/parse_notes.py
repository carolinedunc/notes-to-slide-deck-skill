import re

def parse_sections(org_text):
      sections = []
      currTitle = None
      currBullets = []

      for x in org_text.splitlines():
            x = x.strip()
            if not x:
                  continue 
            
            heading_match = re.match(r"^#{1,3}\s+(.*)", x)
            bullet_match = re.match(r"^[-*•]\s+(.*)", x)

            if heading_match:
                  if currTitle is not None:
                        sections.append((currTitle, currBullets))
                  currTitle = heading_match.group(1)
                  currBullets = []
            elif bullet_match:
                  currBullets.append(bullet_match.group(1))

      if currTitle is not None:
           sections.append((currTitle, currBullets))
            
      return sections

if __name__ == "__main__":
    org_text = """## Site Visit
- Toured the new facility
- Conveyor motors aging, need replacement

## Pipeline
- Two new distributors signed
- Revenue guidance of $100M for the quarter
"""
    result = parse_sections(org_text)
    for title, bullets in result:
        print(f"SECTION: {title}")
        for b in bullets:
            print(f"  - {b}")