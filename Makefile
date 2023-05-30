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

.PHONY: plot
plot:
	python scripts/plot_user_contest_history.py

# Usage
# make select INPUT=1
# make update INPUT="update question 1"