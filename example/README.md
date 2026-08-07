# Example: notes.md → final_deck.pptx

Mock input: general meeting notes

Run:python build_deck.py

**Output**
1. `notes.md` is parsed into sections based on its `##` headers and `-` bullets.
2. Each bullet is expanded into a full, natural sentence using the Anthropic API.
3. The expanded text is placed into slides built from the Duncan & Co. branded template
4. The finished deck is saved as `final_deck.pptx`
