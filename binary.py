# convert a string to binary
def convert_binary(text): # text must be passed as list
  text = text.split(" ")
  binaryList = []
  tempWord = ""

  for word in text:
    tempWord = ""  # reset temp word for each list item
    for letter in word:
      tempWord += " " + str(bin(ord(letter)))[2:]  # append each letter to tempWord word, [2:] to remove beginning 0b
    binaryList.append(tempWord)
    binaryList.append(bin(ord(" "))[2:])  # append space to list
  binaryList.pop()  # deletes last space in list

  return ' '.join(binaryList)