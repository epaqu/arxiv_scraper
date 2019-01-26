import urllib.request
import xml.etree.ElementTree as ET
import pandas as pd
baseURL = 'http://export.arxiv.org/api/query?search_query=all:machine&learning'

page = 0
result = ""
FileNumber = 1
papers = {}
paper_count = 0
save_at = 100
entry_start = 7
row_number = 0
while page < 1409:
	try:
		newURL = baseURL + "&start=" + str(page) + "&max_results=100"
		newData = urllib.request.urlopen(newURL).read().decode('utf-8')
		root = ET.fromstring(newData)
		for i in range(100):
			paper = []
			curr_entry = entry_start + i
			paper.append(root[curr_entry][0].text)
			paper.append(root[curr_entry][1].text)
			paper.append(root[curr_entry][2].text)
			paper.append(root[curr_entry][3].text)
			paper.append(root[curr_entry][4].text)
			papers[row_number]=paper
			row_number += 1
	except :
		print(page)
	page += 1
	if page % save_at == 99:
		df = pd.DataFrame.from_dict(papers, orient='index', columns=['id', 'updated_at', 'published_at', 'title', 'summary'])
		with open('abc.csv', 'a', encoding='utf-8') as f:
			df.to_csv(f, header=False, encoding='utf-8')
		print("page"+str(page))
		papers = {}