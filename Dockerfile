FROM python:3.7

ADD CIPHER_D2.py .
RUN pip install streamlit

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["CIPHER_D2.py"]
