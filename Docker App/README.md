# Instructions

## building docker image : 

Move to `app` directory

`$ cd ../app/` 

Build a docker image :  

`$ docker build -f Dockerfile -t fishdetector:v1 .`

## Execute the container

`$ docker run -p 8501:8501 fishdetector:v1`

> Note : These instructions haven't been tested at my end as building the docker image was taking up my all RAM and disk memory, if you face any errors or have any improvements then please create a pull request for the same )
