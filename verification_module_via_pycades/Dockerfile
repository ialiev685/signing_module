FROM ubuntu:22.04

RUN apt-get update && apt install -y \ 
    cmake build-essential libboost-all-dev python3-dev unzip git python3-pip 

COPY ./cryptopro_packages /tmp/cryptopro

WORKDIR /tmp/cryptopro

RUN tar xvf linux-amd64_deb.tgz && \
    cd linux-amd64_deb && \
    chmod +x ./install.sh && \
    ./install.sh && \
    apt install ./lsb-cprocsp-devel_5.0*.deb && \
    apt install ./cprocsp-pki-cades*.deb

RUN unzip pycades-main.zip && \
    cd pycades-main && \
    NEW_PATH=$(python3 -c "import sysconfig; print(sysconfig.get_path('include'))") && \
    sed -i "s|SET(Python_INCLUDE_DIR \"/usr/include/python3\.12\")|SET(Python_INCLUDE_DIR \"$NEW_PATH\")|" CMakeLists.txt && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j4

RUN mkdir -p /app/lib/pycades/
RUN mkdir -p /app/trusted_certificates/

RUN cp -r /tmp/cryptopro/pycades-main/build/* /app/lib/pycades

RUN rm -rf /tmp/*

WORKDIR /app

COPY trusted_certificates ./trusted_certificates
COPY . .
COPY requirements.txt .

# Доверенные промежуточные сертификаты
RUN /opt/cprocsp/bin/amd64/certmgr -install -cert -store uCA -file /app/trusted_certificates/ca.p7b -all
# Корневые сертификаты
RUN /opt/cprocsp/bin/amd64/certmgr -inst -store mRoot -f /app/trusted_certificates/certnew.p7b -all



RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="/app/lib/pycades"

# для dev режима
# CMD ["fastapi", "run", "main.py"]

# для prod режима
CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]
