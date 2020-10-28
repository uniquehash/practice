# links to interesting modules
# textwrap: https://pymotw.com/2/textwrap/index.html#module-textwrap
# fileinput: https://pymotw.com/2/fileinput/index.html#module-fileinput

import fileinput
import in_place

def printFile(fp):
  for line in fileinput.input(filepath):
    cnt += 1
    printLine(cnt, line)

def printLine(cnt, line):
  print("Line {}: {}".format(cnt, line.strip()))

def appendLine(filepath, msg):
  with open(filepath, 'a') as fp:
    fp.write(msg)

def printByWord(filepath):
  for line in fileinput.input(filepath):
    cnt = 1
    for word in line.split(" "):
      wrd = 1
      print("Line {}: Word {}: {}".format(cnt, wrd, word))
      wrd += 1
    cnt += 1  

def boldWord(filepath, keyword):
  for line in fileinput.input(filepath):
    cnt = 1
    for word in line.split(" "):
      wrd = 1
      # print("Line {}: Word {}: {} == {}".format(cnt, wrd, word, keyword))
      if word == keyword:
        print("found the word: {}".format(keyword))
      wrd += 1
    cnt += 1  

def inplace(filepath, keyword):
  with in_place.InPlace(filepath) as fp:
      for line in fp:
        queue = []
        for word in line.split(" "):
          print("word: {}".format(word))
          if word == keyword:
            queue.append("**{}**".format(word))
          else:
            queue.append(word)
        fp.write(' '.join(queue))
          
          



# filepath = './testpy.md'
filepath = './test.md'
inplace(filepath, "all")

# boldWord(filepath, "all")
  
