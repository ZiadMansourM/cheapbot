FROM certbot/certbot
LABEL org.opencontainers.image.source="https://github.com/ziadmmh/cheapbot"
LABEL maintainer="ziadmansour.4.9.2000@gmail.com"
ENV PYTHONIOENCODING="UTF-8"

RUN pip install -U pip && pip --version
RUN pip install zope.interface
RUN pip install dns-lexicon

COPY . src/cheapbot

RUN pip install --no-cache-dir src/cheapbot

ENTRYPOINT ["/usr/bin/env"]