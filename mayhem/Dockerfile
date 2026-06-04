FROM python:3.11-slim

# Install build dependencies for atheris
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        clang \
        python3-dev \
        git \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Install atheris
RUN CC=clang CXX=clang++ pip install atheris

ADD . /mail-parser

# Build
WORKDIR /mail-parser
RUN pip install .

CMD ["/mail-parser/mayhem/fuzz_mail_parsing.py"]
