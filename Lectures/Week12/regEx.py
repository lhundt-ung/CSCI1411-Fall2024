import re

log = '''1157689595.034 TEST http://google.com TARGET 1 
         1157689595.531 TEST http://ung.edu TESTING https://mailbox.ung.edu END OF http://www.espn.com LOG'''

x = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', log)
print(x)