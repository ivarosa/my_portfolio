# Portfolio Data Analyst

A Streamlit-based portfolio web application showcasing data analysis projects and visualizations.

## Python Compatibility

This project is tested and compatible with **Python 3.11.x** and **Python 3.12+**. 

### Dependency Notes

**NumPy Version Constraint**: The project uses `numpy>=1.25,<2` instead of a strict version pin. This change was made to ensure compatibility with Python 3.12+ deployments (including Streamlit Cloud running Python 3.13). 

**Background**: NumPy versions prior to 1.25 do not provide pre-built binary wheels for Python 3.12+, causing pip to attempt building from source. However, the build process for numpy <1.25 depends on `distutils`, which was removed from Python's standard library in version 3.12. Using `numpy>=1.25` ensures pip installs a compatible binary wheel without requiring a build step.

**Runtime Pin**: The `runtime.txt` file pins the Python version to 3.11.6 for Streamlit Cloud deployments to maintain stability. If you need to use Python 3.12+ specifically, the numpy constraint already supports that scenario.

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
streamlit run app.py
```

## Deployment

This application is designed to be deployed on Streamlit Cloud. The `runtime.txt` file specifies the Python version used in the deployment environment.
