from PyDictionary import PyDictionary
import pprint

def meaning(word):
  dictionary=PyDictionary()
  defenition = dictionary.meaning(word) # get meaning
  defenition = pprint.pformat(defenition) # increase readablity
  return defenition

if __name__ == "__main__":
  print(meaning("test"))