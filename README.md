# Math Fun Fact API

This is a FastAPI-based application that provides interesting mathematical properties about a given number, along with a fun fact.

## Project Structure

```
math-api
├── src
│   ├── main.py            # Entry point of the FastAPI application
│   ├── routers
│   │   └── math.py       # API endpoint for mathematical properties
│   └── services
│       └── math_service.py # Logic for mathematical calculations and fun facts
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Features

- Accepts a number and returns its mathematical properties.
- Checks if the number is prime, perfect, or an Armstrong number.
- Calculates the sum of the digits of the number.
- Fetches a fun fact about the number from the Numbers API.
- Handles CORS (Cross-Origin Resource Sharing).
- Returns responses in JSON format.

## Setup Instructions

1. Clone the repository:

   ```
   git clone <repository-url>
   cd math-api
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## API Usage

### Base URL

```
http://localhost:8000
```

### Endpoints

### GET `/api/classify-number`

Accepts a number as a query parameter and returns its mathematical properties and a fun fact.

#### Request

```http
GET /api/classify-number?number=371
```

#### Get Mathematical Properties

- **Endpoint:** `http://numbersapi.com/{number}/math`
- **Method:** `GET`
- **Query Parameters:**

  - `number`: The number to analyze (integer).

- **Response:**
  - Returns a JSON object containing:
    - `is_prime`: Boolean indicating if the number is prime.
    - `is_perfect`: Boolean indicating if the number is perfect.
    - `properties`: List of properties of the number (e.g., "armstrong", "odd").
    - `digit_sum`: The sum of the digits of the number.
    - `fun_fact`: A fun fact about the number.

### Example Request

```
GET /api/classify-number?number=28
```

### Example Response

*200 OK*

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

### Example Error Response

*400 Bad Request*
```json
{
    "number": "alphabet",
    "error": true
}
```

## Running the Application

To run the application, use the following command:

```
uvicorn src.main:app --reload
```

Visit `http://localhost:8000/docs` for the interactive API documentation.


## Deployment to AWS

### Using `systemd`

1. **Set Up a Virtual Private Server (VPS):**
   - Log in to your AWS account.
   - Navigate to the EC2 service and create a new instance.
   - Choose an operating system (e.g., Ubuntu).

2. **Connect to Your EC2 Instance:**
   - Use an SSH client (the terminal on macOS/Linux) to connect to your VPS.
   - Example command:
     ```bash
     ssh root@your_vps_ip_address
     ```

3. **Install Dependencies:**
   - Update the package list and install Python and pip:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

   - Install `uvicorn` and `fastapi`:
     ```bash
     pip3 install fastapi uvicorn
     ```

4. **Upload Your FastAPI Application:**
   - git clone the repository.
     ```bash
      git clone https://github.com/Celnet-hub/hng12-pub-api.git
      cd hng12-pub-api
     ```

5. **Create a systemd Service File:**
   - Create a new service file for your FastAPI application:
     ```bash
     sudo nano /etc/systemd/system/fastapi.service
     ```

6. **Add the Service Configuration:**
   - Add the following content to the `fastapi.service` file. Make sure to replace the placeholders with your actual paths and user information:
     ```ini
     [Unit]
     Description=FastAPI application
     After=network.target

     [Service]
     User=your_username
     Group=www-data
     WorkingDirectory=/path/to/your/app
     ExecStart=/usr/bin/env uvicorn app.main:app --host 0.0.0.0 --port 8000
     Restart=always

     [Install]
     WantedBy=multi-user.target
     ```

7. **Reload systemd and Start the Service:**
   - Reload the systemd daemon to recognize the new service:
     ```bash
     sudo systemctl daemon-reload
     ```

   - Start the FastAPI service:
     ```bash
     sudo systemctl start fastapi
     ```

   - Enable the service to start on boot:
     ```bash
     sudo systemctl enable fastapi
     ```

8. **Check the Service Status:**
   - You can check the status of your FastAPI service to ensure it is running correctly:
     ```bash
     sudo systemctl status fastapi
     ```

9. **Set Up a Reverse Proxy (Optional):**
   - To make your application accessible via a domain name, you can set up a reverse proxy using Nginx.
   - Install Nginx:
     ```bash
     sudo apt install nginx
     ```

   - Configure Nginx to proxy requests to your FastAPI application. Edit the Nginx configuration file (e.g., `/etc/nginx/sites-available/default`):
     ```nginx
     server {
         listen 80;
         server_name your_aws_domain.com;

         location / {
             proxy_pass http://127.0.0.1:8000;
             proxy_set_header Host $host;
             proxy_set_header X-Real-IP $remote_addr;
             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
             proxy_set_header X-Forwarded-Proto $scheme;
         }
     }
     ```

   - Restart Nginx to apply the changes:
     ```bash
     sudo systemctl restart nginx
     ```

10. **Access Your Application:**
    - Your FastAPI application should now be accessible via your domain name or VPS IP address.

## Technology Stack
- FastAPI
- Uvicorn
- httpx