VENV := .venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip

.PHONY: install run run-two-sum run-remove-duplicates run-remove-element run-move-zeroes clean

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PIP) install -e .

run: run-two-sum run-remove-duplicates run-remove-element run-move-zeroes

run-two-sum: install
	$(PYTHON) examples/example.py

run-remove-duplicates: install
	$(PYTHON) examples/example_remove_duplicates.py

run-remove-element: install
	$(PYTHON) examples/example_remove_element.py

run-move-zeroes: install
	$(PYTHON) examples/example_move_zeroes.py

clean:
	rm -rf $(VENV) *.egg-info tui_pointer.egg-info two_pointer.egg-info __pycache__
