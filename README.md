# Markdown CV to HTML Converter

This Python script converts a markdown CV file (`khaja.md`) to an HTML file while preserving the professional design template.

Generate My CV : https://sheralam.github.io/cv/khaja.html

## Features

- Parses structured markdown CV format
- Maintains the existing professional HTML/CSS design template
- Automatically formats sections (Impact Summary, Technical Expertise, Experience, Education)
- Handles markdown formatting (bold, italic) and converts to proper HTML
- Generates clean, readable HTML output

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Installation

```bash
# Optional: Install dependencies (currently none required)
make install

# Or with pip directly
pip install -r requirements.txt
```

## Usage

### Using Makefile (Recommended)

The easiest way to use the converter is through the Makefile:

```bash
# Show all available commands
make help

# Convert markdown to HTML (khaja.md → khaja.html)
make convert

# Clean generated files
make clean

# Test the conversion
make test

# Clean and convert in one command
make all

# Show file information
make info

# Convert custom files
make convert-custom IN=input.md OUT=output.html

# Open generated HTML in browser (macOS)
make open

# Watch for changes and auto-convert (requires fswatch)
make watch
```

### Direct Python Usage

You can also run the script directly:

```bash
# Basic usage (creates khaja.html)
python3 md_to_html.py khaja.md

# Specify custom output
python3 md_to_html.py khaja.md output.html

# Make the script executable and run it directly
chmod +x md_to_html.py
./md_to_html.py khaja.md custom_name.html
```

## Markdown Format Requirements

The script expects the markdown file to follow this structure:

```markdown
## Name
**Title/Role** Location | [email](mailto:email) | [LinkedIn](url)

---

### Staff-Level Impact Summary
* Point 1
* Point 2

---

### Core Technical Expertise
* Category: Details
* Category: Details

---

### Professional Experience

#### **Company Name** | Job Title
*Location | Date Range*
* Achievement 1
* Achievement 2

---

### Education
* Degree 1
* Degree 2
```

## Output

The script generates a complete HTML file with:
- Professional styling (matching the existing template)
- Responsive design
- Print-friendly CSS
- Properly formatted sections and typography
- Clean, semantic HTML structure

## Customization

To modify the design template, edit the CSS section in the `generate_html()` function within the script. The current template uses:
- Font: Segoe UI
- Max width: 900px
- Color scheme: Navy blue (#2c3e50) headers with professional grays
- Highlight box for Impact Summary section
- Flexbox layout for skills section
