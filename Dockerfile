FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit","run","streamlit_app/app.py","--server.address=0.0.0.0"]



# Docker Containerization

Docker is used to package the entire application along with its dependencies.

## Steps

1. Copy project files into container
2. Install required dependencies
3. Expose Streamlit port
4. Launch Streamlit application

## Benefits

- Portable deployment
- Consistent environment
- Easy scaling
- Simplified dependency management