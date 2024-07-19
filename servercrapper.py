import requests
from bs4 import BeautifulSoup

def get_server_ids():
    url = 'https://servers.fivem.net/'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Trouver les balises ou les classes CSS qui contiennent les informations des serveurs
            server_elements = soup.find_all('div', class_='server-info')
            server_ids = []
            for server in server_elements:
                # Extraire l'identifiant ou d'autres informations pertinentes
                server_id = server.find('span', class_='server-id').text.strip()
                server_ids.append(server_id)
            return server_ids
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

if __name__ == "__main__":
    server_ids = get_server_ids()
    if server_ids:
        print("List of server IDs:")
        for server_id in server_ids:
            print(server_id)
