from bs4 import BeautifulSoup as BS
import requests
import traceback
import json


f1 = open('out11.txt', 'w')




URL="https://quizlet.com/47571/barrons-gre-wordlist-4759-words-flash-cards/"
#URL = "http://localhost:443/github/site.html"
response = requests.get(URL)
#response.encoding = "ISO-8859-1" 
#print response.encoding
soup = BS(response.text, "lxml" ,from_encoding="UTF-8")
#print soup

results_list = soup.find_all('div', class_="text")
#print results_list

words_list = []
try:
	for result in results_list:
		word_tag = result.find('span',class_="TermText qWord lang-en")
		defination_tag = result.find('span',class_="TermText qDef lang-en")
      	#wrs = unicode(word_tag, "utf-8")

		#word = wrs.contents[0]
		#data[word_tag.text.encode('utf-8')] = defination_tag.text
		#print defination_tag.text
		local_data = {}
		local_data={
		'meaning' : defination_tag.text.encode('utf-8') ,
		'word' : word_tag.text.encode('utf-8') 
		}
		#print local_data
		#local_data_json = json.dumps(local_data)	
		#print >> f1, json.dumps(local_data)
		words_list.append(local_data)
		#data['words_list'].append({json.dumps(local_data)})
		
		#json_data = json.dumps(data)
		#print json_data
		


		
except:
	pass

#data_json = json.dumps(data['words_list'])
#print data['words_list']
data = { 'all_words' : words_list}
print >> f1, json.dumps(data)
#f1.close()	