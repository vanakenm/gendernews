# Gender news

Small project to analyze various news site with the goal of evaluating their gender diversity.

Method for now is quite simple:

- Parse the page, getting the articles titles
- Extract anything that looks like a name us- ing the Standford NER algorithm
- Identify probable gender of each name

## Todo

### v1

- [ ] Source page: total citation, history per day, word cloud?
- [x] Contact (page ok, need to send email)
- [x] Add prev/next day to dashboard
- [x] Analysis detail page (with prev/next)
- [x] Let's start in french, but translatable already?
- [x] Add text to dashboard
- [x] Home: Explain what this is about
- [x] Sources : Pick one for detail, see stats (today?)
- [x] Dashboard
- [x] Store all titles (to do some keywords analysis after?), not only those with identified names
- [x] Could create a "re-analyze" based on the saved html

### Later

- [ ] Add sentiment analysis on titles?
- [ ] Check hugging face interface/api for easy module switch?
  - Ex: https://huggingface.co/qanastek/pos-french
- [ ] Add Django translations

