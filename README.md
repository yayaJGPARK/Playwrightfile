# Playwright Web Automation Test

Python + Playwright + pytest 기반의 웹 UI 자동화 테스트 프로젝트입니다.

## 1. 프로젝트 목적

웹 서비스의 주요 UI 기능을 대상으로 자동화 테스트를 구현하고,
반복적으로 수행되는 기능 검증을 자동화하는 것을 목적으로 합니다.

주요 테스트 항목:

- Input 입력 검증
- Checkbox 선택 검증
- Dropdown 선택 검증
- JavaScript Alert / Confirm / Prompt
- Add / Remove Elements
- Dynamic Controls
- Dynamic Loading
- File Upload
- iFrame
- Multiple Windows

## 2. 테스트 환경

| 항목 | 환경 |
|---|---|
| Language | Python 3.14 |
| Test Framework | pytest |
| Automation | Playwright |
| Browser | Chromium |
| OS | Windows / Linux |
| CI | GitHub Actions |

## 3. 프로젝트 구조

```text
Playwrightfile/
├─ tests/
│  ├─ Dynamic_Controls/
│  ├─ Dynamic_Loading/
│  ├─ JavaScript_Alert/
│  ├─ Multiple_Windows/
│  ├─ add_Remove/
│  ├─ checkbox/
│  ├─ dropdown/
│  ├─ file_Upload/
│  ├─ iFrame/
│  └─ input/
├─ .github/
│  └─ workflows/
│     └─ playwright.yml
├─ conftest.py
├─ pytest.ini
├─ requirements.txt
└─ README.md
