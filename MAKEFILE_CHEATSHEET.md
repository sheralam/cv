# Makefile Cheat Sheet

## 🎯 Most Common Commands

```bash
make convert    # Convert MD → HTML
make clean      # Remove generated files  
make all        # Clean + Convert
make help       # Show all commands
```

## 📖 All Available Commands

### Basic Operations
| Command | What It Does |
|---------|--------------|
| `make convert` | Convert `khaja.md` to `khaja.html` |
| `make clean` | Remove generated HTML files and Python cache |
| `make all` | Clean everything, then convert |
| `make test` | Test the conversion script |
| `make help` | Show help message with all commands |

### Advanced Operations
| Command | What It Does |
|---------|--------------|
| `make convert-custom IN=file.md OUT=file.html` | Convert custom files |
| `make info` | Show file information (lines, size) |
| `make lint` | Check Python code quality |
| `make install` | Install Python dependencies |
| `make open` | Open generated HTML in browser (macOS) |
| `make watch` | Auto-convert on file changes (requires fswatch) |

## 🔧 Variables You Can Override

```bash
# Use custom input/output files
make convert INPUT_MD=mycv.md OUTPUT_HTML=mycv.html

# Use different Python interpreter
make convert PYTHON=python3.11
```

## 💡 Practical Examples

### Example 1: Quick Edit Workflow
```bash
# 1. Edit khaja.md
# 2. Convert
make convert
# 3. View
make open
```

### Example 2: Clean Build
```bash
make all
```

### Example 3: Convert Multiple Versions
```bash
make convert-custom IN=khaja.md OUT=khaja_v1.html
make convert-custom IN=khaja.md OUT=khaja_v2.html
```

### Example 4: Watch Mode for Active Editing
```bash
# Install fswatch (one time only)
brew install fswatch

# Start watching
make watch
# Now edit khaja.md and save - it auto-converts!
# Press Ctrl+C to stop
```

### Example 5: Before Committing to Git
```bash
make clean      # Clean generated files
make test       # Verify it works
make lint       # Check code quality
```

## 🎓 Understanding Makefile Targets

### `.PHONY` Targets
All targets in this Makefile are `.PHONY`, meaning they're commands, not files:
- They always run when called
- They don't check for file existence
- Perfect for automation tasks

### Dependency Chain
```
make all
  ├── make clean  (runs first)
  └── make convert (runs second)
```

## 🚀 Pro Tips

1. **Tab Completion**: Type `make` and press Tab to see available targets
2. **Dry Run**: Use `make -n convert` to see what would run without running it
3. **Parallel**: Most targets run quickly, but you can use `make -j4` for parallel execution
4. **Silent Mode**: Use `make -s convert` to suppress command echoing
5. **Keep Going**: Use `make -k` to continue even if one target fails

## 🔍 Debugging Makefile

```bash
# Show what make would do
make -n convert

# Show all variables
make -p

# Debug mode
make --debug convert
```

## 📝 Customizing the Makefile

Want to modify defaults? Edit these variables at the top:

```makefile
PYTHON := python3        # Python executable
INPUT_MD := khaja.md     # Default input file
OUTPUT_HTML := khaja.html # Default output file
SCRIPT := md_to_html.py  # Conversion script
```

## ❓ Common Issues

**Q: "make: command not found"**
```bash
# Install Xcode Command Line Tools
xcode-select --install
```

**Q: "No rule to make target"**
- Check spelling: `make help` to see available targets
- Make sure you're in the right directory

**Q: Conversion fails**
- Run: `make test` to diagnose
- Check: `python3 --version` (need 3.6+)
- Verify: `ls khaja.md` (file exists)

## 🔗 Related Files

- `README.md` - Full project documentation
- `QUICKSTART.md` - Quick start guide
- `md_to_html.py` - The actual conversion script
- `requirements.txt` - Python dependencies
