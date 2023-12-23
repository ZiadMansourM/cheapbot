FROM certbot/certbot:v2.8.0

LABEL org.opencontainers.image.source="https://github.com/ziadmmh/cheapbot"
LABEL maintainer="ziadmansour.4.9.2000@gmail.com"
ENV PYTHONIOENCODING="UTF-8"

RUN pip install -U pip && pip --version
RUN pip install zope.interface==6.1
RUN pip install dns-lexicon==3.17.0

COPY . src/cheapbot

RUN pip install --no-cache-dir src/cheapbot

ENTRYPOINT ["/usr/bin/env"]