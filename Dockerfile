FROM ubuntu:22.04

RUN apt-get update && apt install -y \ 
    cmake build-essential libboost-all-dev python3-dev unzip git 

RUN mkdir -p /app

COPY ./cryptopro_packages /tmp/cryptopro

COPY ./main.py /app/

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

RUN cp -r /tmp/cryptopro/pycades-main/build/ /app/

RUN rm -rf /tmp/*

WORKDIR /app

ENV PYTHONPATH="/app/build"

CMD ["python3", "main.py"]
