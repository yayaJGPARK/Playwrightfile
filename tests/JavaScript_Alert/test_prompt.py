from playwright.sync_api import expect


def test_prompt(page):

    page.goto("/javascript_alerts")

    # Prompt 버튼 찾기
    button = page.get_by_role(
        "button",
        name="Click for JS Prompt"
    )

    # Prompt에 입력할 값
    input_text = "Hello Playwright"

    # Prompt 처리
    page.on(
        "dialog",
        lambda dialog: dialog.accept(input_text)
    )

    # 버튼 클릭
    button.click()

    # 결과 확인
    result = page.locator("#result")

    expect(result).to_have_text(
        f"You entered: {input_text}"
    )

    print("JavaScript Prompt 테스트 성공!")