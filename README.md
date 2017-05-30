# yahoo_finance_get_historical_fix
A workaround for the recently discontinued get_historical() functionality for yahoo_finance API.

It looks like this functionality has been discontinued: 
https://forums.yahoo.net/t5/Yahoo-Finance-help/ichart-not-working-in-my-app/td-p/253560

Here's a workaround (grab the data directly from the history pages), using urllib2 and BeautifulSoup
