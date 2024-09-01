# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and the application code into the container
COPY . .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "main.py"]