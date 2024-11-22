# Stock Price Agent

## Overview
The Stock Price Agent is an autonomous agent designed to fetch real-time stock prices of any listed company using the Alpha Vantage API. This agent can be deployed on Agentverse and can be interacted with via DeltaV, a chat interface.

---

## How It Works

### Data Flow:
1. **User Request**:
   - The user sends a stock price request via DeltaV using a symbol (e.g., `AAPL` for Apple Inc.).
   
2. **Agent Processing**:
   - The agent validates the request and queries the Alpha Vantage API for the latest stock price.
   
3. **Response**:
   - The fetched stock price is sent back to the user in a readable format via DeltaV.

---

## Deployment
### Prerequisites:
- **Alpha Vantage API Key**: Obtain from [Alpha Vantage](https://www.alphavantage.co).

### Steps:
1. **Host on Agentverse**:
   - Sign-in on [Agentverse](https://agentverse.ai/)
   - Click on New Agent and copy the code in `agent.py` file
   - Start the agent.

3. **Integrate with DeltaV**:
   - Create a Function in order to interact with the Agent using DeltaV.

---

For more on Fetch.ai ecosystem, visit [Fetch.ai Documentation](https://fetch.ai/docs).


