# Define default target
.PHONY: all
all: update

# Define variables
n ?= 0

# Define targets
.PHONY: update
update:
	python PyMDwriter.py
	git add .
	git commit -m "update $(n)"
	git push