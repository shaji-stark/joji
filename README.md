# Joji
Joji convert a sentence to corresponding emoji if emoji is available

## How it Works ?
```
1. There is a json file with emoji names as keys and corresponding unicode of emojis as values.
2. There is a method that check if the input word is in the key space of the json. If yes then will return corresponding value.
3. There is a method that do similarity matching of word against the keys in json and return the emoji unicode corresponding to the key with maximum similarity value.
4. There is a threshold to avoid False Positives.
5. If both checking and matching don't return anything, just return the word - means there is no emoji for that word. 
```

## Libraries used
- [Spacy](https://spacy.io)
## How to configure (ippo nokeetu karyam illa)
```
python setup.py install 
```
## How to Run
varum varathirikkilla

## How to Test 
```
pytest tests
```
