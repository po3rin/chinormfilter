build:
	poetry build

format:
	poetry run black chinormfilter/*.py

publish:
	twine upload dist/*