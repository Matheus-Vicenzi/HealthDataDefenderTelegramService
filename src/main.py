import uvicorn
from fastapi import FastAPI

    
if __name__ == "__main__":
    uvicorn.run("controller.MainController:main_app", host="localhost", port=8000, reload=True)