# Developer Documentation 

This documentation is a guide for adding new features (tools) to the API Gateway. It assumes a basic understanding of Python, FastAPI, and the existing project structure.

Learn more about it here:
https://fastapi.tiangolo.com/
https://docs.python.org/3/

and of course,
https://google.com

## 1. The Core Principle: Plug-and-Play

The project is designed as a modular API Gateway. Each tool is a self-contained module that can be "plugged in" to the main application without altering the existing codebase. A new tool is added by simply creating a new file in the `tools/` directory and including its router in `main.py`.

See Example: 
```py
#tools/base64_convertor.py
router = APIRouter() #Router Instance

#Create a route
@router.post("/encode_base64") 
async def encode_base64(payload: StringPayload):
    """
    Encodes a given string into a Base64 string.
    """
#Rest of the code...
```

Then include the router in `main.py`:
```py
#main.py
#Plug & Play Section
app.include_router(base64_converter.router, prefix="/base64_tools", tags=["Base64 Converter"])
```

## 2. Step-by-Step Guide for Adding a New Tool

Follow these steps to create and integrate a new tool into the API.

### Step 1: Create a New Tools Module

- Inside the `tools/` directory, create a new Python file for your tool (e.g., `tools/new_tool.py`)
- This file must import `APIRouter` from FastAPI.
- Define a new router instance at the top of the file.
  
```py
from fastapi import APIRouter

router = APIRouter()
```

### Step 2: Implement the Tool Logic

- Write the Python code for your new tool's functionality.
- Use standard FastAPI decorators(`@router.get()`, `@router.post`, etc.) to define your API endpoints. 
- The endpoints should be self-contained within this module.
- Use Pydantic models to define the request and response data structures for clarity and automatic validation.

### Step 3: Register the New Router in `main.py`

- Open `main.py`, which is the central API Gateway file.
- Import the `router` you defined in your new feature module.
- Use `app.include_router()` to add new tool's endpoints to the main application.

```py
# In main.py
from fastapi import FastAPI
from features import base64_converter, new_tool

app = FastAPI(
    title="Multi-Utility Tool API",
    description="A simple API gateway for various developer tools.",
    version="0.1.0"
)

# Existing router
app.include_router(base64_converter.router, prefix="/base64_tools", tags=["Base64 Converter"])

# Register your new tool here
app.include_router(new_tool.router, prefix="/new_tool_path", tags=["New Tool Name"])
```

- The `prefix` argument is crucial as it defines the URL path for all endpoints in that module (e.g., `/new_tool_pathj/endpoint` or simply `/endpoint/`)
- The `tags` argument helps organize the documentation on the `/docs` page.

## 3. Best Practices
-  **Documentation:** Add a docstring to your new module and each endpoint. This will automatically appear in the interactive `/docs` UI (Swagger UI) provided by FastAPI.
-  **Dependencies:** If your new tool requires external libraries, add them to `requirements.txt`.
-  **Testing:** Test your new endpoints using the interactive `/docs` page to ensure they are working correctly before committing your changes.
  