# Multithreaded Python HTTP Server Primer

This is a simple multithreaded HTTP server written in Python that can handle multiple incoming connections simultaneously. The purpose of this project is to showcase a simple implementation og multithreading in the context of an HTTP server using Python.

## Features

- Supports HTTP/1.1 requests
- Handles multiple connections using threads
- Parses and constructs HTTP requests and responses
- Returns a simple "Hello, world!" response to GET requests

## Usage

To start the server, run the `server.py` script with Python 3:

```python3 server.py```

The server will start listening on `127.0.0.1:8080`. To test the server, open a web browser and navigate to `http://127.0.0.1:8080`. You should see a "Hello, world!" message.