#Import the necessary libraries
from ai_engine import UAgentResponse, UAgentResponseType
from uagents import Model, Context, Protocol
import requests

#Data Model
class StockPriceRequest(Model):
    symbol: str

#Function to get the stock price from the Alphavantage Website
async def get_stock_price(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    print(data)
    if 'Time Series (1min)' in data:
        latest_time = sorted(data['Time Series (1min)'].keys())[0]
        latest_data = data['Time Series (1min)'][latest_time]
        current_price = latest_data['1. open']
        return current_price
    else:
        return "Error: Unable to fetch stock price."

#Protocol for communication 
stock_price_agent = Protocol("Stock Price", version="1.1")

#Message Handler to handle the User's request from DeltaV
@stock_price_agent.on_message(model=StockPriceRequest, replies={UAgentResponse})
async def handle_request(ctx: Context, sender: str, msg: StockPriceRequest):
    stock_price = await get_stock_price(msg.symbol)
    final_string = f'Stock price for {msg.symbol} is $ {str(stock_price)}. '
    ctx.logger.info(f"Success: {final_string}")
    await ctx.send(sender, UAgentResponse(message=final_string, type=UAgentResponseType.FINAL))

agent.include(stock_price_agent)
