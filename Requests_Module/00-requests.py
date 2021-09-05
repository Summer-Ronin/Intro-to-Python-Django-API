"""
    A simple GET req using requests
"""

import requests
from rich import style
from rich.console import Console

console = Console()

def main():
    #response = requests.get("http://www.google.com")
    response = requests.get("http://www.google.com")
    # response = requests.get("http://www.google.com/random-address/")
    console.print("Status Code: ", response.status_code, style="cyan2")
    print('\n')
    console.print("Headers: ", response.headers, style = "cyan2")
    print('\n')
    console.print("'Content-Type': ", response.headers['Content-Type'], style = "cyan2")
    print('\n')
    console.print("Content: ", response.text, style="cyan2")


if __name__ == "__main__":
    main()
