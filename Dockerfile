FROM python:3.7

ADD main2.py .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["main2.py"]