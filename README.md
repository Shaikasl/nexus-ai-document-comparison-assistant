# Nexus AI — AI Document Comparison Assistant

## Project Overview

Nexus AI is an AI-powered web application that compares two PDF documents and helps users understand their similarities, differences, and important details.

The application extracts text from both PDFs and uses Google's Gemini AI to generate a structured comparison report.

## Features

- Upload two PDF documents for comparison.
- Extract text from PDF files using `pypdf`.
- Preview extracted text and document information.
- Generate separate summaries for Document A and Document B.
- Identify similarities and differences between documents.
- Compare key details such as names, dates, amounts, and requirements.
- Display an overall conclusion and limitations.
- Download the comparison report as a Word document (`.docx`).
- Handle invalid PDFs and API errors.
- Reset the application to compare another pair of documents.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- pypdf
- python-docx
- python-dotenv

## Project Structure

```text
ai-document-comparison-assistant/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── .env
```

Note: The `.env` file stores your private API key. Never upload it to GitHub.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai-document-comparison-assistant
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API Key

Create a `.env` file in the project folder and add:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the example value with your own Gemini API key. Keep this file private.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your web browser.

## How to Use

1. Open the Nexus AI application.
2. Upload the first PDF as Document A.
3. Upload the second PDF as Document B.
4. Start the comparison.
5. Review the summaries, similarities, differences, key details, conclusion, and limitations.
6. Download the comparison report.
7. Reset the application to compare other documents.

## Error Handling

The application is designed to handle invalid or empty PDF files and errors during document processing or AI requests. Actual behavior depends on the implemented validation and error-handling code.

## Security and Limitations

- Keep API keys and other secrets private.
- AI-generated comparisons may contain mistakes; verify important findings against the original documents.
- Scanned PDFs may require OCR if they do not contain extractable text.
- Comparison quality depends on the text extracted and the AI model's response.

## Author

**Shaik Aslam Basha**
B.Tech — Computer Science and Engineering

## Project Purpose

This project demonstrates PDF text extraction, AI-powered document analysis, web application development, and report generation using Python.
