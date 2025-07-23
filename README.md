Sample python web framework using Python and pytest

Implementations:
- Cross browser runs on firefox and chrome using selenium manager
- Page object model pattern 
- Global fixtures across conftest.py
- Python logger at root and file level
- Log decorators for driver events i.e. click
- Event listener

Installation:
- Requirements: python3, pip
- pip install -r requirements.txt

Run pytest src/tests/TestLogin.py --browser=chrome at the root level


