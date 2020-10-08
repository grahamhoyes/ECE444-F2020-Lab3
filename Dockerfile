FROM python:3.8-buster

WORKDIR /usr/src/app

# Install requirements
RUN pip install --upgrade pip
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy project files
COPY app/ /usr/src/app/

# Run the app
CMD ["python", "app.py"]