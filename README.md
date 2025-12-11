# Portfolio Data Analyst

A Streamlit-based portfolio application showcasing data analysis projects and visualizations.

## Python Compatibility

This application is tested and compatible with **Python 3.11.x**.

### Dependency Notes

The numpy version constraint was updated from a strict pin (`numpy==1.24.3`) to a flexible range (`numpy>=1.25,<2`) to ensure compatibility with modern Python versions, particularly Python 3.12 and 3.13. NumPy 1.24.3 requires building from source on Python 3.12+, which fails because the build process depends on `distutils` (removed in Python 3.12). By allowing numpy 1.25+, pip can install prebuilt binary wheels that are compatible with newer Python versions, avoiding the build-from-source path entirely.

For Streamlit Cloud deployments, this project pins Python to version 3.11.6 via `runtime.txt` to ensure maximum compatibility and stability with all dependencies.

## Installation

1. Ensure you have Python 3.11.x installed
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
streamlit run app.py
```

## Deployment

This application is configured for deployment on Streamlit Cloud with:
- Python 3.11.6 (specified in `runtime.txt`)
- All dependencies managed in `requirements.txt`
