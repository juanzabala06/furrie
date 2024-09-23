from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import config
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware




HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']
portalid = 6395217


client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True)
print(client)
db = client.get_database_client(DATABASE_ID)
print(db)
container = db.get_container_client(CONTAINER_ID)
print(container)


app = FastAPI()

# Add CORS middleware to allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://furr.ie", "http://127.0.0.1:8000"],  # Replace with your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)



app.mount("/static", StaticFiles(directory="static"), name="static")


# Serve the React/Vite frontend at the root URL
@app.get("/")
async def serve_frontend():
    return FileResponse('static/index.html')

@app.get('/favicon.ico')
async def favicon():
    file_name = 'favicon.ico'
    file_path = './static/' + file_name
    return FileResponse(path=file_path, headers={'mimetype': 'image/vnd.microsoft.icon'})

# Define a Pydantic model for the request body
class HelloRequest(BaseModel):
    name: str

@app.post("/hello")
async def hello(request: HelloRequest):
    name = request.name
    print(f"Request to say hello to {name}")
    return {"message": f"Hello, {name}!"}



def read_item(container, doc_id, portalid):
    print(container)

    # We can do an efficient point read lookup on partition key and id
    response = container.read_item(item=doc_id, partition_key=portalid)

    print('Item read by Id {0}'.format(doc_id))
    print('Partition Key: {0}'.format(response.get('portalid')))
    print('RedirectURL: {0}'.format(response.get('redirectUrl')))
    return response.get('redirectUrl')


@app.get("/{redirect_name}")
async def read_root(redirect_name: str):
    try:
        redirect_url = read_item(container, redirect_name, portalid)
        return RedirectResponse(url=redirect_url)
    except exceptions.CosmosResourceNotFoundError:
        return "Redirect not found"



if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)

