# CSRF Scanner

This project includes a CSRF (Cross-Site Request Forgery) vulnerability scanner and a proof of concept HTML file to demonstrate how a CSRF attack can be executed.

## Files in This Project

1. `csrf_crawler.py` - A Python script that scans web applications for CSRF vulnerabilities.
2. `csrf_poc.html` - An HTML file that demonstrates a CSRF attack.

## Installation

### Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library

### Installing Dependencies

Before running the scanner script, you need to install the required Python libraries. You can do this using `pip`.

```bash
pip install requests beautifulsoup4
```
### Usage

#### CSRF Vulnerability Scanner (csrf_crawler.py)
- Save the csrf_crawler.py script to your local machine.

- Open a terminal or command prompt and navigate to the directory where the script is saved.

- Run the script by executing:

```bash
python csrf_crawler.py
```
- Enter the URL of the website you want to scan for CSRF vulnerabilities when prompted.

The script will output whether each form on the page has CSRF protection or not.

#### CSRF Proof of Concept (csrf_poc.html)
- Save the csrf_poc.html file to your local machine.

- Open the HTML file in a text editor and modify the action attribute of the form to point to the target URL that you have permission to test.

```bash
<form id="csrf_form" action="http://targetsite.com/change_email" method="POST">
```
- Save your changes and open the csrf_poc.html file in a web browser.

- The form will automatically submit, demonstrating the CSRF attack by sending a POST request to the target URL.