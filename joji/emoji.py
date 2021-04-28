import os
import json
import spacy

try:
  nlp = spacy.load("en_core_web_md")
except OSError:
  print("Downloading language model for spacy (don\'t worry, this will only happen once)")
  from spacy.cli import download
  download('en_core_web_md')
  nlp = spacy.load('en_core_web_md')

emoji_dict_path = "data/emoji_dict.json"
emoji_dict = open(emoji_dict_path)
emoji_dict = json.load(emoji_dict)

class Jojify(object):
  """
  class containing methods to map text to emoji
  """  
  emoji_dict = emoji_dict
  
  @classmethod
  def _simple_check(cls, text):
    if text in cls.emoji_dict:
      return (
        cls.emoji_dict.get(text).get("emoji"),
        cls.emoji_dict.get(text).get("unicode"),
        1
      )
    return None
  
  @staticmethod
  def _similarity_match(word1, word2):
    word1 = nlp(word1)
    words = word2.split(" ")
    if len(words) > 1:
      return max([nlp(word).similarity(word1) for word in words])
    else:
      word2 = nlp(word2)
      return word1.similarity(word2)
    
  @classmethod  
  def _context_similarity_check(cls, text):
    max_score = 0 # set threshold value instead
    max_emoji = None
    for emoji_name in cls.emoji_dict:
      score = cls._similarity_match(text, emoji_name)
      if score > max_score:
        max_emoji = cls.emoji_dict.get(emoji_name).get("emoji")
        max_unicode = cls.emoji_dict.get(emoji_name).get("unicode")
        max_score = score
    return max_emoji, max_unicode, max_score


  @staticmethod
  def preprocess(text):
    text = text.lower()
    return text

  @classmethod
  def predict(cls, text):
    text = cls.preprocess(text)
    emoji = cls._simple_check(text)
    emoji = cls._context_similarity_check(text) if not emoji else emoji
    return emoji if emoji else text
  
 
  
