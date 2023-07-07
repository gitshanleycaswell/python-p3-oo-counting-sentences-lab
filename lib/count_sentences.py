#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value =''):
    self.value = value

  def set_value(self):
    return self._value
  
  def get_value(self, new_value):
    if type(new_value) == str:
      self._value = new_value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    if self.value.endswith('.'):
      return True
    else:
      return False
    
  def is_question(self):
    if self.value.endswith('?'):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value.endswith('!'):
      return True
    else:
      return False
    
  def count_sentences(self):
    new_sentences = self.value.replace('?', '.').replace('!','.')
    new_sentences = new_sentences.replace('..', '.')
    sentences = new_sentences.split('.')
    sentences=[sentence for sentence in sentences if sentence]
    count = len(sentences)
    print(sentences)
    return count
  value = property(set_value, get_value)


# def count_sentences(self):
#     sentences = re.split(r'(?<![.!?])[.!?]+', self.value)
#     sentences=[sentence for sentence in sentences if sentence]
#     count=len(sentences)
#     print(sentences)
#     return count