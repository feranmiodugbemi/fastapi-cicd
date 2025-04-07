from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title='Serverless Lambda FastAPI')



@app.get("/", root_path="/prod", tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions, yayyyy!"}



handler = Mangum(app=app)
