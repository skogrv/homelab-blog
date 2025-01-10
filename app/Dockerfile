FROM python:3.12.8-alpine3.21
RUN addgroup -S app && adduser -S -G app app
WORKDIR /usr/src/app/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g'  /usr/src/app/entrypoint.sh
COPY . .
RUN chmod +x  /usr/src/app/entrypoint.sh
RUN chown -R app:app /usr/src/app
USER app
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
