# SauceDemo QA Automation Project

## ℹ️ About the Project
This project serves as a portfolio demonstration of automated and manual testing for the e-commerce website [SauceDemo](https://www.saucedemo.com/).

## 📂 Project Structure
- **[manual_tests/](manual_tests/)** - Detailed Test Cases (Checkout, Inventory flows)
- **[automation/](automation/)** - Python Playwright automated tests
- **[bug_reports/](bug_reports/found_bugs.md)** - 🐞 List of found defects (Bug Reports)

## 🛠️ Technologies Used
- **Language:** Python 3.13.5
- **Automation Framework:** Playwright
- **Testing Framework:** Pytest
- **Other:** Git, GitHub

## 🚀 How to Run
Follow these steps to set up the project locally:

1. **Clone the repository:**
```bash
    
git clone [https://github.com/kratochvilo/saucedemo_qa_demoproject.git](https://github.com/kratochvilo/saucedemo_qa_demoproject.git)
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/Scripts/activate  # (On Windows Git Bash)
```

3. **Install dependencies:**
```bash
pip install pytest playwright pytest-playwright
playwright install
```

4. **Run tests:**
```bash
pytest
```