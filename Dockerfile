FROM python:3.8-slim-buster
WORKDIR .

# Setup timezone
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy and configure app
COPY  . .

# Good luck, gave fun :)
CMD ["python", "main.py"]
