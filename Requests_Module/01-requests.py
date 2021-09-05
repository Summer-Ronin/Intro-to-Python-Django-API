import requests
import json

def main():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    
    if response.status_code == 200:
        print("Status Code: ", response.status_code)
        
        # Get Headers
        print(response.header)

        json_res = json.loads(response.content)
        # data = response.json()
        print("Pokemon name is", json_res['name'])
    
    else:
        print("Status Code: ", response.status_code)
        raise Exception("There was an error!")
    

if __name__ == "__main__":
    main()