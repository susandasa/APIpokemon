# Use the official Python image
FROM python:3.12.2-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/requirements.txt

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 5000 to the outside world
EXPOSE 5000

# Run the application
CMD ["python", "pokemon.py"]
