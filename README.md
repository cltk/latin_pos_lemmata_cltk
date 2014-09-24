# About

This repository contains part of speech (POS) data for the Latin language, made specifically for use with the [CLTK](https://github.com/kylepjohnson/cltk). Only CLTK developers need this repository. To tag parts of speech, [see here](http://docs.cltk.org/en/latest/classical_latin.html#pos-tagging).

The directory `perseus_data` contains part of speech data taken from Perseus. `pos_latin.tar.gz` contains `cltk_latin_pos_dict.txt` (252MB, too large to upload to GitHub) and is what is picked up by the corpus importer.

`parse_latin_analyses.py` was used to create `latin-analyses.txt` into Python's dictionary type. 

# Use
``` python
In [1]: s = 'Multum tibi esse animi scio; nam etiam antequam instrueres te praeceptis salutaribus et dura vincentibus, satis adversus fortunam placebas tibi, et multo magis postquam cum illa manum conseruisti viresque expertus es tuas, quae numquam certam dare fiduciam sui possunt nisi cum multae difficultates hinc et illinc apparuerunt, aliquando vero et propius accesserunt.'

In [2]: import re

In [3]: import ast

In [4]: p = re.compile('\w+', re.IGNORECASE)

In [5]: %paste
with open('/Users/kyle/cltk_data/compiled/pos_latin/cltk_latin_pos_dict.txt') as f:
    r = f.read()

In [6]: d = ast.literal_eval(r)

for match in p.finditer(s):
    w = match.group()
    tag = d[w]['perseus_pos']
    print(tag)

for match in p.finditer(s):
    w = match.group()
    try:
        tag = d[w]['perseus_pos']
        print(tag)
    except:
	    pass


In [20]: for match in p.finditer(s):
    w = match.group()
    try:
        tag = d[w]['perseus_pos']
        print(w, tag)
    except:
            pass
multum [{'pos0': {'gloss': 'a penalty', 'number': 'pl', 'gender': 'neut', 'type': 'substantive', 'case': 'gen'}}, {'pos1': {'gloss': '', 'number': 'pl', 'gender': 'masc', 'type': 'substantive', 'case': 'gen'}}, {'pos2': {'gloss': '', 'number': 'pl', 'gender': 'neut', 'type': 'substantive', 'case': 'gen'}}, {'pos3': {'gloss': '', 'number': 'pl', 'gender': 'masc', 'type': 'substantive', 'case': 'gen'}}, {'pos4': {'gloss': '', 'number': 'sg', 'gender': 'masc', 'type': 'substantive', 'case': 'acc'}}, {'pos5': {'gloss': '', 'number': 'sg', 'gender': 'neut', 'type': 'substantive', 'case': 'nom'}}, {'pos6': {'gloss': '', 'number': 'sg', 'gender': 'neut', 'type': 'substantive', 'case': 'acc'}}, {'pos6': {'gloss': '', 'number': 'sg', 'gender': 'neut', 'type': 'substantive', 'case': 'acc'}}, {'pos6': {'gloss': '', 'number': 'sg', 'gender': 'neut', 'type': 'substantive', 'case': 'acc'}}]
tibi [{'pos0': {'gloss': '', 'number': 'sg', 'gender': 'masc/fem', 'type': 'substantive', 'case': 'dat'}}, {'pos0': {'gloss': '', 'number': 'sg', 'gender': 'masc/fem', 'type': 'substantive', 'case': 'dat'}}]
esse [{'pos0': {'gloss': '', 'tense': 'pres', 'type': 'verb', 'voice': 'act'}}, {'pos1': {'gloss': '', 'tense': 'pres', 'type': 'verb', 'voice': 'act'}}]
animi [{'pos0': {'gloss': 'the rational soul in man', 'number': 'pl', 'gender': 'masc', 'type': 'substantive', 'case': 'voc'}}, {'pos0': {'gloss': 'the rational soul in man', 'number': 'pl', 'gender': 'masc', 'type': 'substantive', 'case': 'voc'}}, {'pos1': {'gloss': 'the rational soul in man', 'number': 'sg', 'gender': 'masc', 'type': 'substantive', 'case': 'gen'}}]
scio [{'pos0': {'gloss': '', 'person': '1st', 'type': 'verb', 'number': 'sg', 'tense': 'pres', 'voice': 'act', 'mood': 'ind'}}, {'pos1': {'gloss': 'knowing', 'number': 'sg', 'gender': 'neut', 'type': 'substantive', 'case': 'abl'}}, {'pos2': {'gloss': 'knowing', 'number': 'sg', 'gender': 'masc', 'type': 'substantive', 'case': 'abl'}}, {'pos3': {'gloss': 'knowing', 'number': 'sg', 'gender': 'neut', 'type': 'substantive', 'case': 'dat'}}, {'pos4': {'gloss': 'knowing', 'number': 'sg', 'gender': 'masc', 'type': 'substantive', 'case': 'dat'}}]
nam [{'pos0': {'gloss': '', 'type': 'conj', 'case': 'indeclform'}}]
etiam [{'pos0': {'gloss': '', 'type': 'conj', 'case': 'indeclform'}}]
antequam [{'pos0': {'gloss': '', 'type': 'conj', 'case': 'indeclform'}}]
instrueres [{'pos0': {'gloss': '', 'person': '2nd', 'type': 'verb', 'number': 'sg', 'tense': 'imperf', 'voice': 'act', 'mood': 'subj'}}]
te [{'pos0': {'gloss': '', 'number': 'sg', 'gender': 'masc/fem', 'type': 'substantive', 'case': 'abl'}}, {'pos0': {'gloss': '', 'number': 'sg', 'gender': 'masc/fem', 'type': 'substantive', 'case': 'abl'}}, {'pos1': {'gloss': '', 'number': 'sg', 'gender': 'masc/fem', 'type': 'substantive', 'case': 'acc'}}, {'pos1': {'gloss': '', 'number': 'sg', 'gender': 'masc/fem', 'type': 'substantive', 'case': 'acc'}}]
...
```

# License

This software is, like the rest of the CLTK, licensed under the MIT license (see LICENSE). Perseus data comes from [the Perseus Hopper](sourceforge.net/projects/perseus-hopper) and is licensed under the [Mozilla Public License 1.1 (MPL 1.1)](<http://www.mozilla.org/MPL/1.1/).