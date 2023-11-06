
What is an API (Application Programming Interface)
- when you use an uber ride, many different apps are connecting and talking to each other,
- one is for payments, one for ride etc. 
- So, an app processing interface, is what allows them to connect to each other.

Here are the basic HTTP methods you can use with `requests`:

- `GET`: retrieve data from a specified resource.
- `POST`: send data to a server to create a new resource.
- `PUT`: send data to a server to update an existing resource.
- `DELETE`: delete the specified resource.
- `HEAD`: similar to GET but it retrieves the headers only, not the actual data.
- `OPTIONS`: returns the HTTP methods that the server supports.

e.g. 

`import requests
`response = requests.get("API")
#Check if the response status works... 
`print(response.status_code
#Now print the returned data: 
`print(response.json())`

