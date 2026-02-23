# Flask app for CI/CD with Argo CD
## Create python up with the following structre  
```text
     app/
    ├── .github/
    │   └── workflows/
    │       └── ci.yaml
    ├── .venv/
    ├── app/
    │   ├── __init__.py
    │   └── app.py
    ├── .dockerignore
    ├── .gitignore
    ├── Dockerfile
    ├── README.md
    └── requirements.txt
```

## Using Flask for basic Web application
```python
@app.route("/") - for default (INDEX.html)
@app.route("/health") - Check status of the web
Listen on port 8000 
```


```Dockerfile
FROM python:3.12-slim

WORKDIR /opt/simpleflaskapp

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8000

CMD ["python","-m","app.app"]
```

```yaml
CI using Github Action
Using github secrets for Dockerhub User/Token 
Github Token to Update helm-gitops-demo (Diffrent Repo)
Also updating tag based of Github Sha
```