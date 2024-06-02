word = "Hello World"
char_words = {}

char_count = [ char_words.get(char)+1  for char in word  ]

print(char_count)