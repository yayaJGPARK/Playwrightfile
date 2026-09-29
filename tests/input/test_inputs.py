from playwright.sync_api import expect


def test_input(page):

    page.goto("/inputs")

    # 숫자 입력
    input_box = page.locator("input")
    input_box.fill("12345")

    # 입력값 확인
    expect(input_box).to_have_value("12345")

    print("Input 테스트 성공!")