FROM python:3.9
ADD api_integration.py .
RUN pip install requests beautifulsoup4
CMD ["python","./api_integration.py"]