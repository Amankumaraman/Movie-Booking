# Movie Booking Backend System

This project implements a Django-based backend system for managing dynamic movie booking slots for theaters. The backend supports configuring weekly schedules, handling custom unavailability, and generating available slots for theaters and screens based on constraints.

---

## Features

1. **Dynamic Slot Generation**
   - Generates slots based on configured opening times.
   - Avoids overlapping with weekly or custom unavailability.

2. **Configurable Weekly Schedules**
   - Allows specifying daily opening and closing times.
   - Supports defining unavailability during specific time ranges (e.g., maintenance).

3. **Custom Unavailability**
   - Mark individual slots or entire dates as unavailable.
   - Overrides weekly schedules when necessary.

4. **API Endpoints**
   - Configure weekly availability.
   - Define custom unavailability.
   - Fetch available slots within a date range.

---

## Installation

1. **Clone the Repository**:

   ```bash
   git clone <https://github.com/Amankumaraman/Movie-Booking/>
   cd <movie_booking>
   ```

2. **Set Up the Environment**:

   ```bash
   python -m venv env
   source env/bin/activate 
   pip install -r requirements.txt
   ```

3. **Run Migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

5. **Access the API Documentation**:

   - Open [http://localhost:8000/swagger/](http://localhost:8000/swagger/) in your browser to explore the Swagger documentation.

---

## API Endpoints

### 1. Configure Weekly Availability

**Endpoint**: `POST /api/theatres/{id}/availability/`

**Payload Example**:
```json
{
  "weekly_schedule": {
    "Monday": {"open": "08:00", "close": "22:00"},
    "Tuesday": {"open": "08:00", "close": "22:00"},
    "Wednesday": {"open": "08:00", "close": "22:00"}
  },
  "weekly_unavailability": {
    "Monday": [
      {"start": "14:00", "end": "16:00"}
    ]
  }
}
```

**Response Example**:
```json
{
  "status": "success"
}
```

---

### 2. Configure Custom Unavailability

**Endpoint**: `POST /api/theatres/{id}/custom-unavailability/`

**Payload Example**:
```json
{
  "screen_id": 1,
  "unavailable_slots": [
    {"date": "2024-12-14", "start": "10:00", "end": "12:00"}
  ],
  "unavailable_dates": ["2024-12-25"]
}
```

**Response Example**:
```json
{
  "status": "success"
}
```

---

### 3. Fetch Available Slots

**Endpoint**: `GET /api/theatres/{id}/slots/`

**Query Parameters**:
- `screen_id` (required)
- `start_date` (required, format: `YYYY-MM-DD`)
- `end_date` (required, format: `YYYY-MM-DD`)

**Example Request**:
```
GET /api/theatres/1/slots/?screen_id=1&start_date=2024-12-10&end_date=2024-12-15
```

**Response Example**:
```json
{
  "slots": [
    {"date": "2024-12-10", "start": "08:00", "end": "10:00"},
    {"date": "2024-12-10", "start": "10:30", "end": "12:30"}
  ]
}
```

---

## Testing the Application

1. **Swagger UI**:
   - Navigate to [http://localhost:8000/swagger/](http://localhost:8000/swagger/).
   - Test all endpoints interactively.

2. **Postman Collection**:
   - Import the provided Postman collection from the repository.
   - Test the endpoints with the sample payloads.

---



## Project Structure

```
movie_booking/
├── booking/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
├── movie_booking/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
```

---

## Requirements

- Python 3.8+
- Django 4.2+
- Django REST Framework
- drf-yasg (for Swagger documentation)

## Video Demo

You can view the video demo of the API endpoints in the following link:

[Video Demo](https://drive.google.com/file/d/1bEfgmiC9Iyahq3oh19d_Z5aSQPJWFJBH/view?usp=sharing)



