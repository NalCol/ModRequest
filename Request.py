import requests 
"""
A learning project aimed to browser and download mods from Modrinth.
Code by NaturalCool/NalCol.

lang = input("Choose your language (zh/us) ")
TODO Impl language choose & store system
"""

# User input type & keyword and set default value
type = input("Insert your request type to Modrinth(search): ").strip()
keyword = input("Insert your keyword(none): ").strip()
if type == '':
    type = 'search'

def Modrinth(type,keyword):
    BaseUrl = 'https://api.modrinth.com/v2/'
    InternetError = "Ouch! I can't reach to the Internet."
    FailedFetchData = "Ouch! Failed to fetch the data!"
    try:
        print(f'{BaseUrl}{type}?query={keyword}/')
        resp = requests.get(f'{BaseUrl}{type}?query={keyword}/')
        resp_dict = resp.json()
    except requests.exceptions.ConnectionError:
        print(InternetError)
        exit(1)
    
    # Check Status Code, Return Errors 
    if resp.status_code != 200:
        print(f'Request Failed! ({resp.status_code})')
        print(f"Error: {resp_dict['error']}")
        print(f"Description: {resp_dict['description']}")
        exit()

    _search_request(type, FailedFetchData, resp_dict)
        

def _search_request(type, FailedFetchData, resp_dict):
    if type == 'search':
        try:
            projects = resp_dict['hits']
            # print("The Top 1 Project in Modrinth's info:")
            print(f"Slug: {projects[0]['slug']}")
            print(f"Name: {projects[0]['title']}")
            print(f"Description: {projects[0]['description']}")
            print(f"Project ID: {projects[0]['project_id']}")
        except ValueError:
            print(FailedFetchData)

    # for key,content in resp_dict.items():
    #     print(f'{key}: {content}')

    # def _return_error(msg):
    #     print(msg)
    #     exit(1)

Modrinth(type,keyword)


