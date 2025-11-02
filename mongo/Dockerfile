FROM mongo:7.0

# Set root credentials
ENV MONGO_INITDB_ROOT_USERNAME=admin
ENV MONGO_INITDB_ROOT_PASSWORD=admin123

# Copy init scripts into the container
COPY init-mongo /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/*.sh

EXPOSE 27017

# Default command runs mongod
CMD ["mongod"]
