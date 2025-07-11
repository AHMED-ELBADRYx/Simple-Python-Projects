# Rewrite the sentence without punctuation 

import string
Sentence = input("Enter a sentence: ")
New_sent = " "
for i in Sentence:
  if i not in string.punctuation:
    New_sent = New_sent + i
print(New_sent)