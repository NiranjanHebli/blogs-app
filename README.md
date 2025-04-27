# FastAPI Tutorial

Welcome to the FastAPI tutorial! This guide will help you get started with FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.6+.

## Steps to Set-up

1. **Install FastAPI**:  
    Use `pip install fastapi` to install the FastAPI library.

2. **Install ASGI Server**:  
    Install an ASGI server like `uvicorn` using `pip install uvicorn`.

3. **Create a FastAPI App**:  
    Write a Python script (e.g., `main.py`) and create a FastAPI instance:
    ```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def read_root():
         return {"Hello": "World"}
    ```

4. **Run the Application**:  
    Start the server using the command:
    ```bash
    uvicorn main:app --reload
    ```

5. **Access the API**:  
    Open your browser and navigate to `http://127.0.0.1:8000` to see your API in action.

6. **Explore Interactive Docs**:  
    Visit `http://127.0.0.1:8000/docs` for Swagger UI or `http://127.0.0.1:8000/redoc` for ReDoc.

