run:
	python -m grpc_tools.protoc -I proto --python_out=. --pyi_out=. --grpc_python_out=. proto/*.proto
	fastapi run ./src/main.py

dev:
	python -m grpc_tools.protoc -I proto --python_out=. --pyi_out=. --grpc_python_out=. proto/*.proto
	fastapi dev main.py