# ExpenseTracker# ExpenseTracker

A simple web application for tracking personal expenses with multi-language support and PDF report generation.

## Features

- Add and categorize expenses
- View expenses in a table
- Download expenses as a PDF report
- Multi-language support (English, Spanish, Dutch)

## Requirements

- Python 3.8+
- See [requirements.txt](requirements.txt) for Python dependencies

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd ExpenseTracker
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Install wkhtmltopdf (for PDF export):**
   - Download from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html) and add to your PATH.

## Usage

1. **Run the app:**
   ```sh
   streamlit run app.py
   ```

2. **Open your browser** to the URL provided by Streamlit (usually http://localhost:8501).

## File Structure

- `app.py` - Main Streamlit application
- [`database.py`](database.py) - SQLite database functions
- [`pdf_utils.py`](pdf_utils.py) - PDF generation utility
- [`translator.py`](translator.py) - Translation loader and helper
- `translations/` - JSON translation files
- `requirements.txt` - Python dependencies

## Adding a New Language

1. Create a new JSON file in `translations/` (e.g., `fr.json`).
2. Add the translated keys and values.
3. Add the language option in the sidebar selectbox in `app.py`.

## License