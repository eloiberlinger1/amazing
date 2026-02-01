MAIN = a_maze_ing.py
PYTHON = python3

args = $(filter-out $@,$(MAKECMDGOALS))

all:
	@echo "Usage: make run <config_file>"

run:
	@if [ -z "$(args)" ]; then \
		echo "Error: No configuration file specified!"; \
		echo "Usage: make run <config_file>"; \
		exit 1; \
	fi
	$(PYTHON) $(MAIN) $(args)

lint:
	flake8 ./
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

install:
	echo install

debug:
	echo debug

lint-strict:
	echo lint_strict

clean:
	rm -rf ./__pycache__
	rm -rf */__pycache__
	rm -rf .mypy_cache

.PHONY: all run lint install debug lint-strict clean
