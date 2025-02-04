from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from services.math_service import MathService

router = APIRouter()
math_service = MathService()

@router.get("/api/classify-number")
async def get_math_properties(number):

    if isinstance(number, str): # Check if the input is a string
        try:
            number = int(number)
        except ValueError:
            response = {
                "number": number,
                "error": True
            }
            # raise HTTPException(status_code=400, detail = response)
            return JSONResponse(status_code=400, content=response)
        
    if number < 0:
        # raise HTTPException(status_code=400, detail="Number must be non-negative")
        return JSONResponse(status_code=400, content="Number must be non-negative")
    
    properties = math_service.get_properties(number)
    is_prime = properties["is_prime"]
    is_perfect = properties["is_perfect"]
    digit_sum = properties["digit_sum"]
    num_properties = properties["properties"]
    fun_fact = await math_service.get_fun_fact(number)
    
    return {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": num_properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }