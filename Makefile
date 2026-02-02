MAIN = a_maze_ing.py
PYTHON = python3
VENV = .venv
VENV_PYTHON = $(VENV)/bin/python3
VENV_PIP = $(VENV)/bin/pip

ARGS := $(wordlist 2, 999, $(MAKECMDGOALS))

.PHONY: all run install lint debug clean re

all: install
	@echo "Usage: make run <config_file>"

install: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	@echo "Creating venv..."
	$(PYTHON) -m venv $(VENV)
	@echo "Installing depedencies..."
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install -r requirements.txt
	@touch $(VENV)/bin/activate

run: install
	@if [ -z "$(ARGS)" ]; then echo "Error: No config file | make run <ex: config.txt>"; exit 1; fi
	$(VENV_PYTHON) $(MAIN) $(ARGS)

lint: clean
	$(PYTHON) -m flake8 ./
	$(PYTHON) -m mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs .

lint-strict: clean
	mypy . --strict
	flake8 .


debug: install
	$(VENV_PYTHON) -m pdb $(MAIN) $(ARGS)

clean:
	rm -rf ./__pycache__
	rm -rf */__pycache__
	rm -rf .mypy_cache
	rm -rf $(VENV)

re: clean install

# Catch-all
%:
	@:
