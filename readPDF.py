# https://medium.com/better-programming/how-to-convert-pdfs-into-searchable-key-words-with-python-85aab86c544f
import tika
tika.initVM()
from tika import parser

parsed = parser.from_file('englishwords.pdf')
print(parsed["metadata"])
print(parsed["content"])
print(parsed)


words = open("words.txt","w")
words.write(parsed["content"])
words.close()