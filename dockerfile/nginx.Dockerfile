FROM nginx:latest
USER root
RUN apt update && apt upgrade -y && apt install -y nano apt-utils certbot python3-certbot-nginx