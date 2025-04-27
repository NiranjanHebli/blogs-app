# FastAPI Tutorial

Welcome to the FastAPI tutorial! This guide will help you get started with FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.6+.

## Steps to Set-up

1. **Set up virtual environment**: 

```
python -m venv venv
```
```
source venv/bin/activate
```

2. **Install Requirements**:  

```
pip install -r requirements.txt
```

3. **Run the Application**:  

    Start the server using the command:
    ```bash
    uvicorn blog.main:app --reload
    ```

5. **Access the API**:  
    Open your browser and navigate to `http://127.0.0.1:8000` to see your API in action.

6. **Explore Interactive Docs**:  
    Visit `http://127.0.0.1:8000/docs` for Swagger UI or `http://127.0.0.1:8000/redoc` for ReDoc.

