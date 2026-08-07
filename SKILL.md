---
name: notes-to-slide-deck
description: >-
  Takes notes and/or text and generates a deck that translates said text into an organized and logically sound deck, using the Duncan & Co. template.
---

# Notes to Slide Deck

## What it does
Takes any input of notes and translates them into a predefined powerpoint deck template.
Any brief notes and/or bullet points will be transformed into full sentences using the
Anthropic API. No changes to the content of the text will be performed, only connecting
phrasing to make sentence flow better. Each slide will mirror the exact formatting of the
predefined "Duncan & Co." template.

## Workflow
1. Take input of notes, bullet points, etc. (what user wants to put in slide)
2. Each part of the note is expanded into fully formed sentences
3. The branded slides are built
4. Expanded text is inputted into slide deck
5. The finished deck is outputted to user

## What it does not do
Does not come up with new information or make assumptions about inputted information, add to it outside of connective phrasing etc.  Does not add any additional formatting besides what is defined to the slide deck.

## Requirements 
This skill calls the Anthropic API so it required a valid API key. 