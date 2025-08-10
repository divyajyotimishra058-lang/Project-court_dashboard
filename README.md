Delhi High Court Case Dashboard
A web dashboard for searching case details from the Delhi High Court website, built with FastAPI, BeautifulSoup, and pure HTML/CSS.
It enables users to select a case, solve the site's CAPTCHA, and view live case status—without visiting the official court portal.

Features:
Search for Delhi High Court cases using Case Type (dropdown), Case Number, and Filing Year.
Live CAPTCHA integration: User must solve a real CAPTCHA from the court site to fetch results.
Error Handling: If the CAPTCHA image can't be loaded, user sees a prominent error; if the CAPTCHA is wrong, user sees an alert after submission.
Real-Time Data Parsing: Parses real case details like Parties, Filing Date, Status, and related PDF documents from the official Delhi High Court HTML.
Modern, Minimal UI: Responsive, card-based interface using only HTML and CSS.

Project Workflow
1. User Browses to / (Home Page)
The server requests a fresh Delhi HC search page.
It parses the returned HTML to obtain:
The latest CAPTCHA image URL
The dynamic randomid (session token)

The form displays:
Case Type (dropdown), Case Number, Filing Year
CAPTCHA image (from the court site)
CAPTCHA input box for user entry
Hidden randomid field
Search and Refresh CAPTCHA buttons

2. User Fills in Details & CAPTCHA
User selects Case Type, enters Case Number and Filing Year.
User looks at the CAPTCHA image and enters the code seen.
User clicks “Fetch Details.”

3. Backend Form Submission
The server collects all form data.
It sends a POST request to the Delhi High Court search form endpoint including all entered values and the paired CAPTCHA/randomid.
If the backend cannot reach the court site or fails to get a new CAPTCHA image, a clear error appears above the form:
“CAPTCHA image not available. Please check your internet connection or try later.”

4. Result Handling
If the CAPTCHA is invalid (wrong or expired), a red alert appears below the form:
“Invalid CAPTCHA. Please try again.”
If case details are found, the dashboard displays:
Parties involved
Filed Date
Status
Download link for PDF (if any)

5. CAPTCHA Refresh
User can click “Refresh CAPTCHA” to reload a new image and randomid, allowing another search attempt.
Installation

Requirements:
Python 3.8+
FastAPI
Requests
BeautifulSoup4
Uvicorn (for running server)

Usage
Open http://127.0.0.1:8000 in your browser.
Search for cases using the dashboard!
