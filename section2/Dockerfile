FROM postgres
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD password
ENV POSTGRES_DB car_sales
COPY ./sql-scripts/  /docker-entrypoint-initdb.d/
