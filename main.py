import json
import sys
import subprocess
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def convert_moves_to_pgn(moves):
    pgn_moves = []
    move_number = 1

    for i in range(0, len(moves), 2):
        move_pair = []
        move_pair.append(moves[i].split()[0])  # White move
        if i + 1 < len(moves):
            move_pair.append(moves[i + 1].split()[0])  # Black move if available

        if len(move_pair) == 2:
            pgn_moves.append(f"{move_number}. {move_pair[0]} {move_pair[1]}")
        else:
            pgn_moves.append(f"{move_number}. {move_pair[0]}")

        move_number += 1

    return ' '.join(pgn_moves)

def process_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    moves = data[0]["0@recorded-game"].get("moves", [])
    pgn = convert_moves_to_pgn(moves)

    return pgn

def upload_to_lichess(pgn):
    token = os.getenv("LICHESS_API_TOKEN")
    if not token:
        print("Error: LICHESS_API_TOKEN not found in .env file.")
        sys.exit(1)
    url = "https://lichess.org/api/import"
    headers = ["-H", f"Authorization: Bearer {token}", "-H", "Content-Type: application/x-www-form-urlencoded"]
    data = ["-d", f"pgn={pgn}"]

    result = subprocess.run(["curl", url, "-X", "POST"] + headers + data, capture_output=True, text=True)
    response_json = json.loads(result.stdout)
    print(f"Lichess URL: {response_json['url']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file>")
        sys.exit(1)

    json_file = sys.argv[1]
    pgn = process_json_file(json_file)
    upload_to_lichess(pgn)
