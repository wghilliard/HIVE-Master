# HIVE-Master
---
##### High Incantation Velocity for Experiments #####
*"Because whatever happens inside that container is black magic to me..." -anonymous*
___
### Description
HIVE is a user-friendly master-slave batch-queue system designed to be attached to docker images containing Fermilab experiment software. One method of implimenting this system is to put both the worker and master code into one image and depending how you invoke your Docker container will determine its role, however this may not be feasible for some implimentations.

Hive is built with:

    + Python-Flask
    + Docker
    + RabbitMQ
    + MongoDB
    + Kubernetes (optional)
    
### Install

1. Install the python dependecies

    `pip install -r requirements.txt` 

2. Modify the callback function in worker.py to perform your desired tasks.
3. Ensure paths are correct for the DATA_PATH and LOG_PATH in worker.py.
4. If the worker node is not on the same machine as the master, the auto-connect will fail. Therefore, use of the *--masterip* argument is neccessary when executing worker.py.
5. Create a file called HIVE-Master/secret_key.py with the variable `SECRET_KEY` set to a string of super secret characters.

### Resources
Slides: https://drive.google.com/open?id=1Zbezdlr00o3MSaXDqb9udY5M7igir-L30tGtF8w-eCI

Worker Github: https://github.com/wghilliard/HIVE-Worker

LARIATSoft Docker Image: https://hub.docker.com/r/wghilliard/jfw2/

Email: grsn.hilliard{at}gmail.com
