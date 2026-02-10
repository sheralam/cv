#!/usr/bin/env python3
"""
Convert HTML CV to PDF using Pyppeteer (headless Chrome).
Preserves CSS and print media styles for professional PDF output.
"""

import asyncio
import sys
from pathlib import Path


def get_default_output(html_path: Path) -> Path:
    """Return PDF path with same stem as HTML file."""
    return html_path.with_suffix(".pdf")


async def html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    """Convert HTML file to PDF using Pyppeteer."""
    try:
        from pyppeteer import launch
    except ImportError:
        print("Error: pyppeteer is not installed. Run: pip install pyppeteer", file=sys.stderr)
        sys.exit(1)

    html_path = html_path.resolve()
    pdf_path = pdf_path.resolve()

    if not html_path.exists():
        print(f"Error: HTML file not found: {html_path}", file=sys.stderr)
        sys.exit(1)

    # Use file:// URL for local HTML so relative paths and styles work
    file_url = html_path.as_uri()

    browser = await launch(
        headless=True,
        args=["--no-sandbox", "--disable-setuid-sandbox"],
    )
    try:
        page = await browser.newPage()
        await page.goto(file_url, waitUntil="networkidle0")
        await page.pdf(
            path=str(pdf_path),
            format="A4",
            printBackground=True,
            margin={
                "top": "0.5in",
                "right": "0.5in",
                "bottom": "0.5in",
                "left": "0.5in",
            },
        )
    finally:
        await browser.close()


def main() -> None:
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python html_to_pdf.py <input.html> [output.pdf]")
        print("Example: python html_to_pdf.py khaja.html khaja.pdf")
        sys.exit(1)

    html_path = Path(sys.argv[1])
    pdf_path = Path(sys.argv[2]) if len(sys.argv) > 2 else get_default_output(html_path)

    asyncio.run(html_to_pdf(html_path, pdf_path))
    print(f"Successfully converted {html_path} to {pdf_path}")


if __name__ == "__main__":
    main()
