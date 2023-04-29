# 20220507-devops-tp1

### Prerequisities
- Docker installed
- API key provided by OpenWeather

### Running the Docker image:
- Open a terminal and run:
```
docker run --env LAT="<your-latitude>" --env LON="<your-longitude>" --env API_KEY=<your-api-key> dzung17/devops-openweather:0.0.2
```