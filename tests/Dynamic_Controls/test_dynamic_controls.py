from playwright.sync_api import expect


def test_remove_checkbox(page):

    page.goto("/dynamic_controls")

    # Checkbox 확인
    checkbox = page.locator("#checkbox")

    expect(checkbox).to_be_visible()

    # Remove 버튼 클릭
    remove_button = page.get_by_role(
        "button",
        name="Remove"
    )

    remove_button.click()

    # Checkbox가 사라졌는지 확인
    expect(checkbox).not_to_be_visible()

    print("Checkbox 제거 테스트 성공!")

def test_add_checkbox(page):

    page.goto("/dynamic_controls")

    # 먼저 Remove 버튼 클릭
    remove_button = page.get_by_role(
        "button",
        name="Remove"
    )

    remove_button.click()

    # Checkbox가 제거됐는지 확인
    checkbox = page.locator("#checkbox")

    expect(checkbox).not_to_be_visible()

    # Add 버튼 찾기
    add_button = page.get_by_role(
        "button",
        name="Add"
    )

    # Checkbox 추가
    add_button.click()

    # Checkbox 찾기
    checkbox = page.locator("#checkbox")

    # Checkbox가 나타났는지 확인
    expect(checkbox).to_be_visible()

    print("Checkbox 추가 테스트 성공!")