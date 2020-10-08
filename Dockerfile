FROM python:3.8-buster

WORKDIR /usr/src/app

# Install requirements
RUN pip install --upgrade pip
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy project files
COPY app/ /usr/src/app/

# Copy the entrypoint
COPY entrypoint.sh /usr/src/entrypoint.sh
RUN chmod +x /usr/src/entrypoint.sh
ENTRYPOINT ["/usr/src/entrypoint.sh"]