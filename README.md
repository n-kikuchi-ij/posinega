# posinega

## How to start dockerimage
RUN `docker build . -t XXXXXXX:version`

RUN `docker run -it -p 5000:5000 XXXXXXX:version /bin/bash`

## After you enter docker container
`cd workdir`

RUN `python3 app.py`
Access http://0.0.0.0:5000/