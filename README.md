# final-project-Topher05-COSC381

# Movie Review API

A Python-based application for exploring movie reviews, descriptions, and more, powered by FastAPI.

## Features

- Retrieve movie reviews by title or language.
- Get video descriptions by ID.
- Interactive API documentation at `/docs`.

## Installation

1. **Clone or download the repository**:
   ```bash
   git clone https://github.com/Topher05/final-project-Topher05.git
   cd final-project-Topher05
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the app**:
   ```bash
   uvicorn main:app --reload
   ```
2. **Access the app**:
   - Open a browser and navigate to:
     - `/moviereviews/{movie_name}`
     - `/descriptions/{video_id}`
     - `/moviereviews/{language}/{movie_name}`
   - Replace placeholders with:
     - `{movie_name}`: The title of the movie to search.
     - `{video_id}`: The ID of the video for its description.
     - `{language}`: A valid ISO 639-1 two-letter language code.

3. **Interactive API Documentation**:
   - Navigate to `/docs` for an easy-to-use interface to test all API methods.

4. **Stop the app**:
   - Press `Ctrl+C` in the terminal.

## Running Tests

Run the test suite with:
```bash
pytest
```

## Requirements

- Python 3.6 or higher
- See `requirements.txt` for additional dependencies.
