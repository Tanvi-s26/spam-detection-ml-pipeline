FROM python:3.9

# Set working directory inside container
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy app code
COPY app/ .

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]