FROM hseling/hseling-api-base:python3.6-alpine3.7 as hseling_api_build

LABEL maintainer="Kirill Konovalov <konovalovkirill27@gmail.com>"

RUN mkdir /dependencies
COPY ./hseling-api-midrusnlp/requirements.txt /dependencies/requirements.txt
COPY ./hseling-api-midrusnlp/setup.py /dependencies/setup.py

RUN pip install -r /dependencies/requirements.txt

FROM hseling/hseling-api-base:python3.6-alpine3.7 as production

COPY --from=hseling_api_build /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=hseling_api_build /usr/lib/python3.6/site-packages /usr/lib/python3.6/site-packages

COPY --from=hseling_api_build /dependencies /dependencies

COPY ./hseling-lib-midrusnlp /dependencies/hseling-lib-midrusnlp
RUN pip install /dependencies/hseling-lib-midrusnlp

COPY ./hseling-api-midrusnlp/hseling_api_midrusnlp /app/hseling_api_midrusnlp
COPY ./hseling-api-midrusnlp/main.py /app/main.py

RUN mkdir -p /data

ENV HSELING_API_MIDRUSNLP_SETTINGS="/app/hseling_api_midrusnlp/default_settings.py"

HEALTHCHECK CMD curl --fail http://localhost:5000/api/healthz || exit 1

