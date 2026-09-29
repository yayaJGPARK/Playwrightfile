from playwright.sync_api import expect


def test_confirm_ok(page):

    page.goto("/javascript_alerts")

    # Confirm 버튼 찾기
    button = page.get_by_role(
        "button",
        name="Click for JS Confirm"
    )

    # Confirm → OK
    page.on("dialog", lambda dialog: dialog.accept())

    # 버튼 클릭
    button.click()

    # 결과 확인
    result = page.locator("#result")

    expect(result).to_have_text("You clicked: Ok")

    print("Confirm OK 테스트 성공!")