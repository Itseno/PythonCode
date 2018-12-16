pyg = 'ay'
clusters_two = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
clusters_three = ['str','thr']
original = input('Enter a word: ')
while original != "exit":

  if len(original) > 0 and original.isalpha():
    new_word = ''
    word = original.lower()
    first = word[0]
    if first in ['a','e','i','o','u']:
      new_word = word + pyg
    elif word[0] + word[1] + word[2] in clusters_three:
      first_three = word[3:]
      new_word = first_three + word[:3] + pyg
    elif word[0] + word[1] in clusters_two:
      first_two = word[2:]
      new_word = first_two + word[:2] + pyg
    else:
      new_word = word + first + pyg
      new_word = new_word[1:]
    print(new_word)
  else:
    print('empty')
  original = input('Enter a word or type exit to end program')
def clean( input ):
    clean + ''
    for character in input:
        if character in alphabet:
            clean += character
    return clean.lower()
def toPigLatin( word ):
    if len(word) > 0 and word.isalpha():
        new_word = ''
        first = word[0]
        if first in ['a','e','i','o','u'] or len(word) < 3:
            new_word = word + pyg
        elif word[0] + word[1] + word[2] in clusters_three:
            first_three = word + pyg
            new_word = first_three + word[:3] + pyg
        elif word[0] + word[1] in clusters_two:
            first_two = word[2:]
            new_word = first_two + word[:2] + pyg
        else:
            new_word = word + first +pyg
            new_word = new-word[1:]
        return new_word
    else:
        return ''
sentence = input('Enter a sentence: ')
sentence = clean( sentence )
for word in sentence.split():
    print( toPigLatin( word ), end=" " )
