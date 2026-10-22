
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "gemini-3.8-flash"

REQUIRED_SECTIONS = [
    "1. SUMMARY OF DOCUMENT A",
    "2. SUMMARY OF DOCUMENT B",
    "3. SIMILARITIES",
    "4. DIFFERENCES",
    "5. DATES COMPARISON",
    "6. NAMES COMPARISON",
    "7. AMOUNTS COMPARISON",
    "8. CONDITIONS AND REQUIREMENTS",
    "9. MISSING OR CONFLICTING INFORMATION",
    "10. FINAL CONCLUSION",
    "11. LIMITATIONS",
]


def validate_ai_response(response_text):
    if not response_text or not response_text.strip():
        return False, "The AI returned an empty response."

    missing = [
        section
        for section in REQUIRED_SECTIONS
        if section.lower() not in response_text.lower()
    ]

    if missing:
        return False, "The AI response is missing required sections."

    return True, None


def compare_documents(document1_text, document2_text):
    if not document1_text or not document1_text.strip():
        return None, "Document A contains no readable text."

    if not document2_text or not document2_text.strip():
        return None, "Document B contains no readable text."

    # Warn instead of silently cutting off important information.
    max_chars = 60000

    if (
        len(document1_text) > max_chars
        or len(document2_text) > max_chars
    ):
        return None, (
            "One or both documents are too long for this comparison. "
            "Please upload shorter PDFs. No text was silently removed."
        )

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return None, (
            "Gemini API key is missing. Add GEMINI_API_KEY "
            "to your .env file."
        )

    prompt = f"""
You are a careful document comparison assistant.

Use ONLY the supplied document text. Never invent facts.
Keep Document A and Document B summaries separate.
Support important findings with short exact excerpts.
Identify which document supports each finding.
If information is absent, say:
"Not found in the provided text."
Do not claim differences when facts match.
Distinguish missing information from contradictions.

DOCUMENT A:
{document1_text}

DOCUMENT B:
{document2_text}

Return all these headings exactly:

1. SUMMARY OF DOCUMENT A
Provide a separate summary of Document A.

2. SUMMARY OF DOCUMENT B
Provide a separate summary of Document B.

3. SIMILARITIES
List facts shared by both documents.

4. DIFFERENCES
Explain additions, removals, changes, and contradictions.
Include short supporting excerpts where possible.

5. DATES COMPARISON
Compare dates, deadlines, and time periods.

6. NAMES COMPARISON
Compare people, companies, and organizations.

7. AMOUNTS COMPARISON
Compare prices, salaries, totals, percentages, and numbers.

8. CONDITIONS AND REQUIREMENTS
Compare eligibility, rules, obligations, and requirements.

9. MISSING OR CONFLICTING INFORMATION
Identify missing details and conflicting statements.

10. FINAL CONCLUSION
Summarize the most important findings.

11. LIMITATIONS
Mention unreadable, unavailable, or missing information.
Do not claim legal compliance.
"""

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        response_text = response.text or ""

        is_valid, error = validate_ai_response(response_text)

        if not is_valid:
            return None, error

        return response_text, None

    except Exception:
        return None, (
            "Document comparison failed. Check your internet connection, "
            "Gemini API key, model availability, and API limits. "
            "Please try again."
        )
