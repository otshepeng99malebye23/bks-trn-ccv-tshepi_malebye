from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse, JSONResponse 
from starlette.staticfiles import StaticFiles
from check_validation import Is_Valid_Credit_card
from pydantic import BaseModel

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "detail": "Invalid path parameter: 'number' must be an string.",
            "errors": exc.errors()
        }
    )

class NumberModel(BaseModel):
    value: str

@app.get("/validate/{credit_number}")
def validate(credit_number: str):  
    try:
        
        if credit_number.isdigit():
            is_valid = Is_Valid_Credit_card(credit_number)
            return {"number": credit_number, "valid": is_valid}
        else:
            raise HTTPException(status_code=422, detail="Enter an Integer")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))