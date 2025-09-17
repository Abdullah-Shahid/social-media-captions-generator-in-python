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

  ## Key Files
- `main.py`, `generator.py`, `templates/index.html`, `static/style.css`

  **Note**: Add your Gemini API key in .env file to use the code.
