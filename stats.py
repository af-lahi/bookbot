def word_count(text=''):
  split_words = text.split()
  return len(split_words)

def each_char_count(text=''):
  char_count = dict()
  lower_text = text.lower()
  for char in lower_text:
    if char_count.get(char) == None:
      char_count[char] = 1
    else:
      char_count[char] += 1
  return char_count

def sorted_char_count(char_count={}):
  char_list = list()
  for k,v in char_count.items():
    char_list.append({'char': k, 'count': v})
  char_list.sort(reverse=True, key=lambda x: x['count'])
  return char_list