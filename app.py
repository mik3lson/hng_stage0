from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/me")
async def me():

    timestamp = datetime.utcnow().isoformat()
    email = "ndudimichael06@gmail.com"
    name = "Michael Ndudi"
    stack = "python/fastapi, django, flask"
    url = "https://catfact.ninja/fact"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url )
            response.raise_for_status()
            cat_data = response.json().get("fact")
    except httpx.RequestError as exc:
        raise HTTPException(status_code=500, detail=f"An error occurred while requesting {exc.request.url!r}.") from exc
    
    except httpx.TimeoutException as exc:
        raise HTTPException(status_code=504, detail=f"Request to Cats factsAPI timed out.") from exc
    
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.") from exc


    return {
        "status" : "success",
        "user":{
            "email": email,
            "name": name,
            "stack": stack
        },
        "timestamp": timestamp,
        "fact": cat_data

    }