import  uvicorn
from mainapp.main import *


api_app = app
if __name__ == '__main__':
    uvicorn.run(api_app)