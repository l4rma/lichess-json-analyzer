# Lichess JSON Analyzer
A simple python script made with the help of ChatGPT to automate the process of analyzing chess games recorded with LiveChess from DGT on Lichess.org

## How to use
1. Clone the repository ``git clone https://github.com/l4rma/lichess-json-analyzer.git``
2. Install the required packages ``pip install -r requirements.txt``
3. Add lichess API token to the environment variables. Create a new file named ``.env`` and add the following line ``LICHESS_API_TOKEN=lip_xxx``
4. Run the script ``python main.py <json_file>``

## Lichess API token
To get the Lichess API token, you need to create an account on Lichess.org and go to ``https://lichess.org/account/oauth/token`` where you can generate a bearer token.
