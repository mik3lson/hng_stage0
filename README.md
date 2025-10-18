# Dynamic profile Endpoint with Cat fats

A simple **FastAPI** service that fetches profile data and random cat facts from the [Cat Facts API](https://catfact.ninja/fact).  
Each time you call `/me`, it returns:
status
email
name 
stack
timestamp
a new cat fact.  

The app also handles network errors, timeouts, and API failures gracefully.

---

## 🚀 Features
- ✅ Fetches a new cat fact from `https://catfact.ninja/fact`
- 🕒 Enforces timeout for external API requests
- ⚠️ Graceful error handling for timeouts, network errors, and bad responses
- 🌍 CORS enabled (all origins allowed, credentials disabled)
- ⚡ Built with **FastAPI** and **httpx**

---

## 🧩 Project Structure
```
hng_stage0/
├── app.py
├── requirements.txt
├── README.md

---
```

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/mik3lson/hng_stage0
cd hng_stage0

```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running the Server

### Start the FastAPI development server:
```bash
uvicorn app:app --reload
```
### You should see output similar to
```arduino
INFO:     Uvicorn running on http://127.0.0.1:8000
```

## 🌐 Example Request
### Endpoint:
```vbnet
GET /me
```
### Example using curl
```bash
curl http://127.0.0.1:8000/me
```

### Response: 
```json
{
  "status": "success",
  "user": {
    "email": "ndudimichael06@gmail.com",
    "name": "Michael Ndudi",
    "stack": "python/fastapi, django, flask"
  },
  "timestamp": "2025-10-17T13:48:12.636473",
  "fact": "A cat’s nose pad is ridged with a unique pattern, just like the fingerprint of a human."
}
```

##🧪 Testing
###You can test the API using:

curl<br>
Postman<br>
http://127.0.0.1:8000/docs— FastAPI’s built-in Swagger UI
