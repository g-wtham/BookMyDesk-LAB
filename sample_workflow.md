Scans QR --> Gets SYSTEM NUMBER

Gets USER data from LOGGED IN credentials --> Gets name, class, dept, etc..

Using the SYSTEM NUMBER, get the name and location details of the system

GET request :

-----
`Select * from system WHERE system_id = 1;`

1 | System2 | TopRight

----

Now, send that as a JSON POST request.

Who is sending this? The USER (Client) is sending to FastAPI Backend (Server)

HTTP POST Request Sent: The client application then constructs and sends an HTTP POST 
request to the specific URL that your create_system endpoint is listening on
(e.g., http://127.0.0.1:8000/systems/).

This request includes the JSON payload in its body and sets the Content-Type header to application/json.

Used to CREATE a new system record.

{
  "system_id": 1,
  "system_name": "PC-101",
  "system_location": "Lab A"
}


FastAPI converts that into:

system = System(name="PC-101", location="Lab A")

Then:

db.add(system)  # ← Add this object (now a row) to the database
'''

# create a students route

'''
Fastapi - Structure API Structure, home page reach aana -> indha function pannu
UVICORN - acts as web server - http://127.0.0.1:8000/

waits for listening the requests.. incoming 

REQUEST - http://127.0.0.1:8000/home - enters in browser
          http://my_computer:8000/home
          
          GET req
          
          header = get req, content-type: application/json
          body = {message: server running}

    
UVICORN sends to python

request ---> uvicorn --> python

--------------    

UVICORN => uvicorn main:app

When server started

DB create, Table create using `app.on_event`

'''
