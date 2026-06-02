# TopoGPT3 Documentation

This directory contains HTML documentation and visual resources for the TopoGPT3 project.

## Contents

### index.html

HTML documentation page generated for the project. It provides a web interface to explore model documentation, architecture details, and results.

## How to View

Open `index.html` directly in your browser:

```bash
# From the repository root
open docs/index.html        # macOS
xdg-open docs/index.html    # Linux
start docs/index.html       # Windows
```

Or serve the directory with a local server:

```bash
cd docs
python -m http.server 8080
# Visit http://localhost:8080
```

## Generating Documentation

To regenerate the HTML documentation (if the project supports it):

```bash
pip install -e ".[dev]"
# Run the specific documentation generation command
```

## Recommended Structure

```
docs/
├── index.html          # Main documentation page
├── assets/             # Images, CSS, JS
│   ├── css/
│   ├── js/
│   └── images/
└── api/                # API documentation (future)
```

## Additional Resources

- [Project README](../README.md)
- [Tutorial](../tutorial.md)
- [Quick Start](../quickstart.md)

---

Back to the [main README](../README.md)
