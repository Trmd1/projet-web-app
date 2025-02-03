# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./script.py /app
COPY ./assets/Pokemon /app/Pokemon

# Run the command to install any necessary dependencies
RUN pip install pymongo

# Run script.py when the container launches
CMD ["python", "script.py"]