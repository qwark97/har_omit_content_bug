FROM mcr.microsoft.com/playwright
CMD [ "python", "run.py" ]
WORKDIR /app
VOLUME /app
COPY --chown=pwuser:pwuser . /app/

RUN chown pwuser:pwuser . && pip install playwright
