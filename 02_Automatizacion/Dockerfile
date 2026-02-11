FROM python:3.10-slim
WORKDIR /app
RUN pip install requests
COPY monitor_red.py .
CMD ["python","monitor_red.py"]
