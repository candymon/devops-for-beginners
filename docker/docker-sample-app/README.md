
# Containerize a python app using docker

### Write Dockerfile
- Go to the project directory. 
- Create/locate the python file(s). In this case we have 'main.py'.
- Create a Dockerfile, based on the needs of your project file.
- For our sample app, the Dockerfile's content is the following-
```bash
  FROM python:3.8
  ADD main.py .
  CMD [ "python", "./main.py" ]
```

### Build an image
- To build the image for your application, run the following command in the project directory containing the Dockerfile
- Make sure docker daemon is running😸
```bash
  docker build -t vignere-cipher . 
```
- The 'vignere-cipher' is name of the image.
- '.' represents the current folder.

### Run the Container
```bash
  docker run -t -i vignere-cipher
```