
import requests 


def test_answer():
    # api-endpoint 
    URL = "https://api.github.com"
    # sending get request and saving the response as response object 
    r = requests.get(url = URL) 
    # extracting data in json format 
    data = r.json() 
    # printing the output 
    print("done") 

    assert(r.status_code  == 200)
