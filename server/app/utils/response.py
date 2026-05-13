from fastapi.responses import JSONResponse
from typing import Any

def success_response(data: Any, status_code: int = 200):
    return {
        "data": data
    }

def error_response(message: str, status_code: int = 400):
    return JSONResponse(
        status_code=status_code,
        content={"error": message}
    )
