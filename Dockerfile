
FROM python:3.9
WORKDIR /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install openai
# Make port 80 available to the world outside this container
EXPOSE 88
ENV OPENAI_API_KEY =$API_KEY
CMD ["python", "app.py"]



