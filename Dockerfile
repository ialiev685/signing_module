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
RUN mkdir -p /app/src/

RUN cp -r /tmp/cryptopro/pycades-main/build/* /app/lib/pycades

RUN rm -rf /tmp/*

WORKDIR /app

COPY src/ ./src/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="/app/lib/pycades"
# для dev режима
# CMD ["fastapi", "run", "src/main.py"]
# для prod режима
CMD ["fastapi", "dev", "src/main.py", "--host", "0.0.0.0", "--port", "8000"]
