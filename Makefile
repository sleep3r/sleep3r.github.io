.PHONY: latex latex-%

pdf-manifest:
	cd presentations/t-ai && ./generate-manifest.js

latex:
	@if [ -z "$(file)" ]; then \
		echo "Usage: make latex file=<name-without-md>"; \
		echo "Example: make latex file=1_Разбор_региона"; \
		exit 1; \
	fi
	cd presentations/t-ai/latex && \
	quarto render "$(file).md" \
		--to beamer \
		--pdf-engine xelatex \
		--output-dir "../pdf" \
		--output "$(file).pdf"
	make pdf-manifest

latex-%:
	cd presentations/t-ai/latex && \
	quarto render "$*.md" \
		--to beamer \
		--pdf-engine xelatex \
		--output-dir "../pdf" \
		--output "$*.pdf"
	make pdf-manifest