FROM python:3.12.2

COPY pokemon.py/app/pokemon.py

COPY API-Pokemon.py/app/API-Pokemon.py

CMD [ "python","run","/app/pokemon.go" ]

CMD ["API.py", "RUN", "/app/API-Pokemon.py"]

