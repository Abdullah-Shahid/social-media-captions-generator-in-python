# Copilot Instructions for Social Media Caption Generator

## Project Overview
This is a simple web application for generating social media captions using AI. The project is structured as a minimal Flask app with the following key components:

- `main.py`: Flask app entry point. Handles HTTP requests, renders the main form, and processes user input.
- `generator.py`: Contains the core logic for generating captions based on user input (description, tone, length).
- `templates/index.html`: Jinja2 HTML template for the main UI form.
- `static/style.css`: Optional CSS for styling the web interface.

## Key Patterns & Workflows
- **Form Handling**: The main form posts to `/` (root). The backend expects `description`, `tone`, and `length` fields.
- **Caption Generation**: All AI logic is in `generator.py`. Update this file to change how captions are generated.
- **Template Rendering**: Use Jinja2 syntax in `templates/index.html` to display results and errors.
- **Static Files**: Place CSS and other static assets in the `static/` directory.

## Running & Debugging
- Start the app with: `python main.py` (ensure Flask is installed)
- Access the app at `http://localhost:5000/`
- Debug by adding print statements or using Flask's debug mode (`app.run(debug=True)`)

## Project Conventions
- Keep business logic in `generator.py`, not in the Flask route.
- Use clear, user-friendly error messages in the UI.
- Follow Flask's default project structure for templates and static files.

## External Dependencies
- Flask (install with `pip install flask`)
- Any AI/ML libraries used in `generator.py` (add to `requirements.txt` if needed)

## Example Data Flow
1. User submits form on `/`.
2. `main.py` receives POST, extracts form data, calls `generator.py`.
3. Generated caption is rendered in `index.html`.

## Key Files
- `main.py`, `generator.py`, `templates/index.html`, `static/style.css`

---
For questions or improvements, update this file to help future AI agents and developers.
