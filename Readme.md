This Project involves the steps to deploy custom containers in Vertex AI

1. Build a scikit learn model
2. Extract the pickle file for the model
3. Use Kserve to serve the model
     1. _kserve should have **load()** method with ready = True. Using this health check will be performed from url '_
**/v2/health/live**
     2. _use predict() method to send payload. To predict inference will be sent using url '**/v1/models/test_model:predict**'_

4. Test locally and push the container to the Docker 
    1. docker build -t first_ml_model:latest . 
    2. docker run -it -p 8082:8082 first_ml_model:latest
5. Run docker in interative mode and 
    1. docker run -it -p 8082:8082 first_ml_model:latest /bin/bash
    2. test the model by sending sample payload using <b>test.py</b>
6. Once everything runs fine. Copy the files to cloud storage location and push them to container registry
    1. docker build -t gcr.io/<project_name>/<model_name>:v1 -f Dockerfile .
    2. docker push gcr.io/<project_name>/<model_name>:v1
7. Using this image, create a model in model registry in vertex AI
8. Use appropriate health and prediction route
9. Create an endpoint and deploy the model in GCP