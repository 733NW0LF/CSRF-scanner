import requests
from bs4 import BeautifulSoup

def get_forms(url):
    """Fetch and parse all forms from the given URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find_all('form')

def form_has_csrf(form):
    """Check if the form contains a CSRF token."""
    inputs = form.find_all('input')
    for input in inputs:
        if input.get('type') == 'hidden' and 'csrf' in input.get('name').lower():
            return True
    return False

def scan_for_csrf(url):
    """Scan the given URL for forms without CSRF protection."""
    forms = get_forms(url)
    for form in forms:
        if not form_has_csrf(form):
            print(f"Form action {form.get('action')} at {url} is missing CSRF protection.")
        else:
            print(f"Form action {form.get('action')} at {url} has CSRF protection.")

# Example usage:
if __name__ == "__main__":
    url_to_scan = input("Enter the URL to scan for CSRF vulnerabilities: ")
    scan_for_csrf(url_to_scan)
