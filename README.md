# CruisePriceCheck
Scrapes Royal Caribbean website and detects changes in price. 
Will send email to me if the price range is ever in my budget.
----------
## How Does It Work?
Uses the python beautiful soup library to scrape Royal Carribean's website for the current price for a specific cruise line.

Uses python's built in smtp library to send an email to be if the price ever drops below a target price

## Example Output
2020-04-09 09:28:18.954016 <br>
Price of ticket: 
1199

2020-04-09 09:29:34.499124
Price of ticket: 
1199

2020-04-09 09:33:03.592982
Price of ticket: 
1199

2020-04-09 09:35:27.001652
Price of ticket: 
1199

... so on
