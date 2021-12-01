# Gender news

Small project to analyze various news site with the goal of evaluating their gender diversity.

Method for now is quite simple:

- Parse the page, getting the articles titles
- Extract anything that looks like a name using the Standford NER algorithm
- Identify probable gender of each name

## Language

Let's start in french, but translatable already?

## Pages

- Home: Explain what this is about
- Sources : Pick one for detail, see stats (today?)
- Source: Today + history

## Update analysis

- Could create a "re-analyze" based on the saved html
  - add to the results: the complete sentence from which the name was extracted
  - will make it easy to higlight
- Check hugging face interface/api for easy module switch?
- Ex: https://huggingface.co/qanastek/pos-french

