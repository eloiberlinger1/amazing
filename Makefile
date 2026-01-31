MAIN = a_maze_ing.py
PYTHON = python3

all:
	@echo "Usage: make run <config_file>"

run:
ifndef ARGS
		@echo "Error: No configuration file specified!"
		@echo "Usage: make run <ex: config.txt>"
		@exit 1
endif
	$(PYTHON) $(MAIN) $(ARGS)

lint:
	flake8 ./

install:
	echo install

debug:
	echo debug

lint-strict:
	echo lint_strict

clean:
	rm -rf __pycache__

.PHONY: all run lint install debug lint-strict clean
