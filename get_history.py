import urllib2
from BeautifulSoup import BeautifulSoup as bs

def get_historical_data(name, number_of_days):
	data = []
	url = "https://finance.yahoo.com/quote/" + name + "/history/"
	rows = bs(urllib2.urlopen(url).read()).findAll('table')[1].tbody.findAll('tr')

	for each_row in rows:
		divs = each_row.findAll('td')
		if divs[1].span.text  != 'Dividend': #Ignore this row in the table
			#I'm only interested in 'Open'; For other values, play with divs[1 through 5]
			data.append({'Date': divs[0].span.text, 'Open': float(divs[1].span.text)})

	return data[:number_of_days]

#Test
for i in get_historical_data('tsla', 5):
	print i