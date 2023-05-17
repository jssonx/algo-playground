# Define default target
.PHONY: all
all: update

# Define variables
INPUT :=

# Define targets
.PHONY: update
update:
	python ./scripts/write_readme.py
	git add .
	git commit -m "$(INPUT)"
	git push

.PHONY: select
select:
	python ./scripts/get_question_by_id.py $(INPUT)
