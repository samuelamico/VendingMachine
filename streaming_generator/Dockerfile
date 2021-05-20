FROM tiangolo/uvicorn-gunicorn

COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt



RUN chgrp -R root /app  && \
    chmod -R 770 /app

ENV MPLCONFIGDIR="/app"

ENV PORT=8000
ENV MAX_WORKERS=1
ENV TIMEOUT=600

EXPOSE 8000

WORKDIR /app

CMD [ "uvicorn", "main:app", "--reload" , "--host" , "0.0.0.0"]   