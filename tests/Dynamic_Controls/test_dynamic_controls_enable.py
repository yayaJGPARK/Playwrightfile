from playwright.sync_api import expect


def test_enable_input(page):

    page.goto("/dynamic_controls")

    # Input 찾기
    input_box = page.locator(
        "#input-example input"
    )

    # 처음에는 비활성화 상태인지 확인
    expect(input_box).to_be_disabled()

    # Enable 버튼 클릭
    enable_button = page.get_by_role(
        "button",
        name="Enable"
    )

    enable_button.click()

    # Input이 활성화됐는지 확인
    expect(input_box).to_be_enabled()

    # 실제 입력
    input_box.fill("Hello Playwright")

    # 입력값 확인
    expect(input_box).to_have_value(
        "Hello Playwright"
    )

    print("Input Enable 테스트 성공!")