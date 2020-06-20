FROM python:3.8-slim as package

RUN pip install poetry \
    && mkdir -p /build/slides_workspace
COPY pyproject.toml /build/
COPY slides_workspace/ /build/slides_workspace/
RUN cd /build && poetry build

FROM python:3.8-slim as work
LABEL maintainer="Kazuya Takei <myself@attakei.net>"

# Add apt packages
RUN apt-get update && apt-get install -y \
    git \
    zsh \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN chsh -s /usr/bin/zsh

COPY --from=package /build/dist/slides_workspace-*-py3-none-any.whl /
RUN pip install /slides_workspace-*-py3-none-any.whl

