# 🛒 E-Commerce Automation Framework

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white" alt="Playwright" />
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/CI%2FCD-Passing-brightgreen?style=for-the-badge&logo=github" alt="CI Status" />
</p>

<p align="center">
  <b>A robust, scalable, and fast test automation framework built from scratch to validate critical e-commerce user journeys.</b>
</p>

---

## 📖 About The Project

This project is a production-grade automated testing framework designed to validate the core functionalities of an e-commerce web application (using [SauceDemo](https://www.saucedemo.com/) as the target). It is built using **Python**, **Playwright**, and **Pytest**, and is fully integrated with **GitHub Actions** for Continuous Integration.

### 🚀 Key Features

*   🏗️ **Page Object Model (POM):** Clean separation of test logic and page locators for high maintainability.
*   ⚡ **Auth Seeding (Storage State):** Bypasses the UI login flow by saving and reusing session cookies, drastically reducing test execution time.
*   🛡️ **Iframe Handling:** Successfully interacts with secure embedded payment gateways (e.g., Stripe/PayPal iframes).
*   🔄 **CI/CD Integration:** Automated test execution on every push via GitHub Actions.
*   📊 **HTML Reporting:** Generates beautiful, self-contained HTML dashboards for test results.
*   🌐 **Cross-Browser Ready:** Configured to run on Chromium, Firefox, and WebKit.

---

## 🛠️ Tech Stack

| Tool | Purpose |
| :--- | :--- |
| 🐍 **Python** | Core programming language. |
| 🎭 **Playwright** | Fast, reliable browser automation. |
| 🧪 **Pytest** | Test runner and fixture management. |
| 📦 **Faker** | Dynamic test data generation. |
| 🐙 **GitHub Actions** | Cloud CI/CD pipeline. |

---

## 📂 Project Structure

```text
ecommerce-automation/
├── .github/workflows/     # CI/CD pipeline configuration
│   └── playwright.yml
├── pages/                 # Page Object Model (POM)
│   ├── base_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── product_page.py
├── tests/                 # Test cases
│   ├── conftest.py        # Pytest fixtures (Auth Seeding)
│   ├── test_checkout.py   # Checkout flow tests
│   ├── test_payment.py    # Iframe payment tests
│   └── test_smoke.py      # Smoke and negative tests
├── pytest.ini             # Pytest configuration
└── README.md
