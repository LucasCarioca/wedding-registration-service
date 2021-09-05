.PHONY := all

start: 
	uvicorn app.main:app --reload --port 8080