# Number Classifier API

This is a Flask-based API that classifies numbers based on their mathematical properties. It determines if a number is **prime**, **perfect**, **Armstrong**, and whether it is **even or odd**. Additionally, it fetches a fun fact about the number from the Numbers API.

## Features
- Classifies numbers as **Armstrong, prime, perfect, even, or odd**.
- Computes the **digit sum** of a number.
- Fetches a **fun fact** from [Numbers API](http://numbersapi.com/).
- Supports **CORS** for cross-origin requests.

## Installation

1. Clone the repository or download the files.
2. Install dependencies:
   ```sh
   pip install flask flask-cors requests
   ```
3. Run the application:
   ```sh
   python app.py
   ```
4. The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### Classify a Number
**Endpoint:**  
```http
GET /classify-number/<int:number>
```

**Example Request:**
```http
GET http://127.0.0.1:5000/classify-number/371
```

**Example Response:**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

## Project Structure

```
├── app.py         # Main API logic
├── config.py      # Flask app configuration
├── README.md      # Project documentation
```