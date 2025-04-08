from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title='Serverless Lambda FastAPI')



@app.get("/", tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions, yayyyy!"}

@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "healthy"}



handler = Mangum(app=app)
