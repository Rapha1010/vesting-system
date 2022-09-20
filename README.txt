- This system architecture was designed using repository and service patterns 
what breaks up in layers.Both work properly through dependency injection, the 
repository handle getting data out of the store (CSV) the service handle business 
constraints. I believe in this way with separeted layers is easily-modified and maintainable.

It was designed in Python, so execute in /app folder with :
    agrs (csvfile, date, digits)
    - python main.py tests/vestingfile-stage4.csv 2021-01-01 2

I wrote some unit tests, if necessary run the code in /app folder :
    python -m py.test
