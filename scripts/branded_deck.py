from pptx import Presentation 
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

NAVY = RGBColor(0x1B, 0x3A, 0x5C)
ORANGE = RGBColor(0xE8, 0x79, 0x2C)
GOLD = RGBColor(0xF2, 0xB2, 0x33)
BACKGROUND = RGBColor(0xFA, 0xFA, 0xFA)
BLACK = RGBColor(0x2B, 0x2B, 0x2B)

def add_brand_slide(prs, title_text):
      slide = prs.slides.add_slide(prs.slide_layouts[6])

      background = slide.background
      fill = background.fill
      fill.solid()
      fill.fore_color.rgb = BACKGROUND
      
      title_textbox = slide.shapes.add_textbox(Inches(0.6), Inches(1.0), Inches(8.8), Inches(1.0))
      textframe = title_textbox.text_frame 
      textframe.text = title_text
      run = textframe.paragraphs[0].runs[0]
      run.font.size = Pt(28)
      run.font.bold = True 
      run.font.color.rgb = NAVY

      return slide
