from playwright.sync_api import expect


def test_dropdown(page):

    page.goto("/dropdown")

    # Dropdown 찾기
    dropdown = page.locator("#dropdown")

    # Option 선택
    dropdown.select_option(label="Option 2")

    input("Dropdown 선택 확인 → Enter")

    # 선택 상태 확인
    expect(dropdown).to_have_value("2")

    print("Dropdown 테스트 성공!")