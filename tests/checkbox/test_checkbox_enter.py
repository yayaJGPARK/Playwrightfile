from playwright.sync_api import expect


def test_checkbox(page):

    page.goto("/checkboxes")

    # 1. Checkbox 찾기
    checkbox = page.locator("input[type='checkbox']").nth(0)

    # 2. Checkbox 선택
    checkbox.check()

    input("Checkbox 선택 확인 → Enter")

    # 3. 선택 상태 확인
    expect(checkbox).to_be_checked()

    print("Checkbox 테스트 성공!")