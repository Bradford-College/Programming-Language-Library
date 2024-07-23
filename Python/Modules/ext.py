# External module via pip
'''
    External Modules via pip
    These are third-party modules that are not included with Python by default and need to be installed using the package manager pip.

    Example:
    - Install the requests module via pip:
        pip install requests

    - Using the requests module to make an HTTP request:
        import requests

        response = requests.get('https://api.github.com')
        print(response.status_code)  # Output: 200 (if successful)
        print(response.json())       # Output: JSON response content
'''