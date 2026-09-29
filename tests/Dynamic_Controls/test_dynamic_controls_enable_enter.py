from playwright.sync_api import expect


def test_enable_input(page):

    page.goto("/dynamic_controls")

    # Input 찾기
    input_box = page.locator(
        "#input-example input"
    )

    # 처음에는 비활성화 상태인지 확인
    expect(input_box).to_be_disabled()

    input("선택 확인 → Enter")

    # Enable 버튼 클릭
    enable_button = page.get_by_role(
        "button",
        name="Enable"
    )

    enable_button.click()

    input("선택 확인 → Enter")

    # Input이 활성화됐는지 확인
    expect(input_box).to_be_enabled()

    input("선택 확인 → Enter")

    # 실제 입력
    input_box.fill("Hello Playwright")

    input("선택 확인 → Enter")

    # 입력값 확인
    expect(input_box).to_have_value(
        "Hello Playwright"
    )

    input("선택 확인 → Enter")

    print("Input Enable 테스트 성공!")