# Using Local Ollama to Build Dictionary

The idea behind this analyzer is to use a local LLM to generate responses to prompts asking about linguistic information about words in English.

The dictionary being used is from the current full english dictionary in the NLP++ library (en-full.dict) and the English words found in this repository: https://github.com/dwyl/english-words/blob/master/words.txt. The two have been merged into one large file and then split into separate letter files using the python script divideWords.py.

## Current Progress

Currently, David de Hilster is running the python script on his computer and generating the definition files for each letter. This is the output from running the `fileLines.py` python script.

- [ ] Total words: 492935
- [x] aaa.txt, word count: 8
- [x] x.txt, word count: 456
- [x] z.txt, word count: 1240
- [x] y.txt, word count: 1291
- [x] j.txt, word count: 2741
- [x] q.txt, word count: 3013
- [x] k.txt, word count: 3818
- [x] v.txt, word count: 5800
- [x] w.txt, word count: 10223
- [x] l.txt, word count: 11185
- [ ] g.txt, word count: 11850
- [x] o.txt, word count: 14189
- [ ] f.txt, word count: 14515
- [ ] i.txt, word count: 14680
- [ ] n.txt, word count: 14797
- [ ] e.txt, word count: 14955
- [ ] h.txt, word count: 15999
- [ ] r.txt, word count: 19730
- [ ] b.txt, word count: 20325
- [ ] d.txt, word count: 20832
- [ ] m.txt, word count: 21002
- [ ] t.txt, word count: 22465
- [ ] u.txt, word count: 23490
- [ ] a.txt, word count: 25902
- [ ] c.txt, word count: 34725
- [ ] p.txt, word count: 37960
- [ ] s.txt, word count: 46893
- [ ] caps.txt, word count: 78851

## Installing Ollama

The current python scripts were developed in a Windows WSL Linux system.

Install the python package using pip:

```
pip install ollama
```

## Useful Links

https://developers-blog.org/ollama-python-library-tutorial-with-examples/
