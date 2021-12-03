# Gender news

Small project to analyze various news site with the goal of evaluating their gender diversity.

Method for now is quite simple:

- Parse the page, getting the articles titles
- Extract anything that looks like a name us- ing the Standford NER algorithm
- Identify probable gender of each name

## Todo

### Language

- [x] Let's start in french, but translatable already?
- [] Add Django translations

### Pages

- [x] Home: Explain what this is about
- [x] Sources : Pick one for detail, see stats (today?)
- [] Source: Today + history
- [] Dashboard
- [] Contact (page ok, need to send email)

### Update analysis

- [] Store all titles (to do some keywords analysis after?), not only those with identified names
- [x] Could create a "re-analyze" based on the saved html
  - add to the results: the complete sentence from which the name was extracted
  - will make it easy to higlight
- [] Check hugging face interface/api for easy module switch?
  - Ex: https://huggingface.co/qanastek/pos-french

