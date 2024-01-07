FROM odoo:16.0
USER root
RUN apt update && apt upgrade -y && apt install -y curl python3-pandas nano
RUN python3 -m pip install unicode pycryptodome paramiko python-barcode