VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

$(VENV):
	python3 -m venv $(VENV)

 install: $(VENV)
	$(PYTHON) -m pip install --upgrade pip 
	$(PYTHON) install -r requirements.txt
run: $(VENV)
	$(PYTHON) a_maze_ing.py config.txt

debug: $(VENV)
	$(PYTHON) -m pdb a_maze_ing.py config.txt

clean:
	rm -rf __pychace__ .mypy_cache

lint: $(VENV)
	$(VENV)/bin/flake8 .
	$(VENV)/bin/mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs