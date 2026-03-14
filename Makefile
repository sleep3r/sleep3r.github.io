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

latex-tex:
	@if [ -z "$(file)" ] || [ -z "$(name)" ]; then \
		echo "Usage: make latex-tex file=<name-without-tex> name=<output-name>"; \
		echo "Example: make latex-tex file=information name=Теория_информации"; \
		exit 1; \
	fi
	cd presentations/t-ai/latex && \
	xelatex -interaction=nonstopmode -output-directory=../pdf "$(file).tex" && \
	xelatex -interaction=nonstopmode -output-directory=../pdf "$(file).tex"
	cd presentations/t-ai/pdf && mv "$(file).pdf" "$(name).pdf"
	cd presentations/t-ai/pdf && rm -f $(file).aux $(file).log $(file).out $(file).toc
	make pdf-manifest