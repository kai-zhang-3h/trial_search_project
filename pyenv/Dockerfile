FROM python:3.9.16-alpine

ARG dir=/workdir

WORKDIR $dir

COPY . .

RUN pip install -U pip && \
    pip install --no-cache-dir -r /workdir/src/requirement.txt

RUN apk update \
        && apk upgrade \
        && apk add --no-cache bash \
        bash-doc \
        bash-completion \
        && rm -rf /var/cache/apk/* \
        && rm -rf /share \
        && mkdir /share \
        && /bin/bash

VOLUME $dir

CMD [ "/bin/bash", "-c", "cd src/trial_search_crawler; scrapy crawl jrct --logfile /share/jrctlog.json" ]