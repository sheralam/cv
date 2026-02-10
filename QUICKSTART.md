# Quick Start Guide

## 🚀 Getting Started (30 seconds)

### Option 1: Using Makefile (Easiest)
```bash
make convert
```
Done! Your `khaja.html` is ready.

### Option 2: Using Python Directly
```bash
python3 md_to_html.py khaja.md
```

---

## 📋 Common Commands

| Command | Description |
|---------|-------------|
| `make convert` | Convert markdown to HTML |
| `make clean` | Remove generated files |
| `make test` | Test the conversion |
| `make all` | Clean and convert |
| `make info` | Show file information |
| `make open` | Open HTML in browser (macOS) |
| `make help` | Show all commands |

---

## 🔄 Typical Workflow

1. **Edit your CV** in `khaja.md`
2. **Convert to HTML**: `make convert`
3. **View in browser**: `make open`
4. **Iterate** as needed

---

## 📝 Custom Files

Convert different files:
```bash
# Using Makefile
make convert-custom IN=myfile.md OUT=myfile.html

# Using Python
python3 md_to_html.py myfile.md myfile.html
```

---

## 🔍 Watch Mode (Auto-convert on save)

Install fswatch first:
```bash
brew install fswatch
```

Then run:
```bash
make watch
```

Now every time you save `khaja.md`, it will automatically convert to HTML!

---

## ✅ Testing

Verify everything works:
```bash
make test
```

---

## 📦 Project Structure

```
.
├── md_to_html.py      # Main conversion script
├── Makefile           # Build automation
├── requirements.txt   # Python dependencies (none currently)
├── README.md          # Full documentation
├── QUICKSTART.md      # This file
├── khaja.md           # Your CV in markdown
└── khaja.html         # Generated HTML output
```

---

## 💡 Pro Tips

1. **Keep it simple**: Just edit `khaja.md` and run `make convert`
2. **Test first**: Run `make test` after making changes to the script
3. **Auto-convert**: Use `make watch` during active editing
4. **Clean builds**: Run `make all` for a fresh conversion

---

## 🆘 Troubleshooting

**Q: Command not found: make**
- Install Xcode Command Line Tools: `xcode-select --install`

**Q: Python script not executable**
- Run: `chmod +x md_to_html.py`

**Q: Conversion failed**
- Check markdown format matches the expected structure
- Run `python3 md_to_html.py khaja.md` to see detailed error

---

## 📖 Need More Help?

See the full `README.md` for:
- Detailed markdown format requirements
- Customization options
- Design template details
