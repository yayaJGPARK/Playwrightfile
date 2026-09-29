from playwright.sync_api import expect


def test_dynamic_loading(page):

    page.goto("/dynamic_loading/1")

    # Start 버튼 찾기
    start_button = page.get_by_role(
        "button",
        name="Start"
    )

    input("선택 확인 → Enter")

    # Start 클릭
    start_button.click()

    input("선택 확인 → Enter")

    # 로딩 후 나타나는 Hello World 확인
    result = page.get_by_text("Hello World!")

    input("선택 확인 → Enter")

    expect(result).to_be_visible()

    print("Dynamic Loading 테스트 성공!")

def test_dynamic_loading_example2(page):

    page.goto("/dynamic_loading/2")

    # Start 버튼
    start_button = page.get_by_role(
        "button",
        name="Start"
    )

    start_button.click()

    input("선택 확인 → Enter")

    # Hello World 확인
    result = page.get_by_text("Hello World!")

    input("선택 확인 → Enter")

    expect(result).to_be_visible()

    input("Hello World 확인 → Enter")

    print("Dynamic Loading Example 2 테스트 성공!")