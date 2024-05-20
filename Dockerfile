# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml file to the working directory
COPY pyproject.toml .

# Install the dependencies specified in pyproject.toml
RUN python -m pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

# Copy the rest of the current folder to the working directory
COPY . .

# Expose the Jupyter Notebook port
EXPOSE 8888

# Launch Jupyter Lab as the entry point
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
