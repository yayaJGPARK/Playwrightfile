from playwright.sync_api import expect


def test_dynamic_loading(page):

    page.goto("/dynamic_loading/1")

    # Start 버튼
    start_button = page.get_by_role(
        "button",
        name="Start"
    )

    # Start 클릭
    start_button.click()

    # 로딩 후 나타나는 Hello World 확인
    result = page.get_by_text("Hello World!")

    expect(result).to_be_visible(timeout=10000)

    print("Dynamic Loading Example 1 테스트 성공!")


def test_dynamic_loading_example2(page):

    page.goto("/dynamic_loading/2")

    # Start 버튼
    start_button = page.get_by_role(
        "button",
        name="Start"
    )

    # Start 클릭
    start_button.click()

    # 로딩 후 생성되는 Hello World 확인
    result = page.get_by_text("Hello World!")

    expect(result).to_be_visible(timeout=10000)

    print("Dynamic Loading Example 2 테스트 성공!")