.PHONY: help convert clean install test lint all

# Variables
PYTHON := python3
INPUT_MD := khaja.md
OUTPUT_HTML := khaja.html
SCRIPT := md_to_html.py

# Default target
help:
	@echo "CV Markdown to HTML Converter - Available targets:"
	@echo ""
	@echo "  make convert     - Convert markdown CV to HTML"
	@echo "  make clean       - Remove generated HTML files"
	@echo "  make install     - Install Python dependencies"
	@echo "  make test        - Test the conversion script"
	@echo "  make lint        - Check Python code quality"
	@echo "  make all         - Clean and convert"
	@echo "  make help        - Show this help message"
	@echo ""
	@echo "Variables:"
	@echo "  INPUT_MD=$(INPUT_MD)"
	@echo "  OUTPUT_HTML=$(OUTPUT_HTML)"

# Convert markdown to HTML
convert:
	@echo "Converting $(INPUT_MD) to $(OUTPUT_HTML)..."
	@$(PYTHON) $(SCRIPT) $(INPUT_MD) $(OUTPUT_HTML)
	@echo "✓ Conversion complete!"

# Convert with custom input/output
convert-custom:
	@if [ -z "$(IN)" ] || [ -z "$(OUT)" ]; then \
		echo "Error: Please specify IN and OUT variables"; \
		echo "Usage: make convert-custom IN=input.md OUT=output.html"; \
		exit 1; \
	fi
	@echo "Converting $(IN) to $(OUT)..."
	@$(PYTHON) $(SCRIPT) $(IN) $(OUT)
	@echo "✓ Conversion complete!"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	@rm -f $(OUTPUT_HTML)
	@rm -f khaja_generated.html
	@rm -f *.pyc
	@rm -rf __pycache__
	@echo "✓ Clean complete!"

# Install dependencies
install:
	@echo "Installing dependencies..."
	@if [ -s requirements.txt ]; then \
		$(PYTHON) -m pip install -r requirements.txt; \
	else \
		echo "No dependencies to install (using standard library only)"; \
	fi
	@echo "✓ Installation complete!"

# Test the conversion
test:
	@echo "Testing conversion script..."
	@$(PYTHON) $(SCRIPT) $(INPUT_MD) test_output.html
	@if [ -f test_output.html ]; then \
		echo "✓ Test passed! Generated test_output.html"; \
		rm -f test_output.html; \
	else \
		echo "✗ Test failed!"; \
		exit 1; \
	fi

# Check code quality
lint:
	@echo "Checking Python code quality..."
	@if command -v pylint >/dev/null 2>&1; then \
		pylint $(SCRIPT); \
	elif command -v flake8 >/dev/null 2>&1; then \
		flake8 $(SCRIPT); \
	else \
		echo "No linter found. Install pylint or flake8 for code quality checks."; \
		echo "Performing basic syntax check..."; \
		$(PYTHON) -m py_compile $(SCRIPT); \
		echo "✓ Syntax check passed!"; \
	fi

# Clean and convert
all: clean convert

# Open the generated HTML in browser (macOS)
open:
	@if [ ! -f $(OUTPUT_HTML) ]; then \
		echo "HTML file not found. Running conversion first..."; \
		$(MAKE) convert; \
	fi
	@echo "Opening $(OUTPUT_HTML) in browser..."
	@open $(OUTPUT_HTML)

# Watch mode (requires fswatch on macOS)
watch:
	@if ! command -v fswatch >/dev/null 2>&1; then \
		echo "Error: fswatch not found. Install it with: brew install fswatch"; \
		exit 1; \
	fi
	@echo "Watching $(INPUT_MD) for changes..."
	@fswatch -o $(INPUT_MD) | while read; do \
		echo "File changed, converting..."; \
		$(MAKE) convert; \
	done

# Show file info
info:
	@echo "File Information:"
	@echo "================="
	@if [ -f $(INPUT_MD) ]; then \
		echo "Input:  $(INPUT_MD) (exists)"; \
		wc -l $(INPUT_MD) | awk '{print "        Lines:", $$1}'; \
	else \
		echo "Input:  $(INPUT_MD) (not found)"; \
	fi
	@if [ -f $(OUTPUT_HTML) ]; then \
		echo "Output: $(OUTPUT_HTML) (exists)"; \
		wc -l $(OUTPUT_HTML) | awk '{print "        Lines:", $$1}'; \
		ls -lh $(OUTPUT_HTML) | awk '{print "        Size:", $$5}'; \
	else \
		echo "Output: $(OUTPUT_HTML) (not generated yet)"; \
	fi
