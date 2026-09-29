from playwright.sync_api import expect


def test_alert(page):

    page.goto("/javascript_alerts")

    button = page.get_by_role(
        "button",
        name="Click for JS Alert"
    )

    page.on("dialog", lambda dialog: dialog.accept())

    button.click()

    input("Alert 처리 확인 → Enter")

    result = page.locator("#result")

    expect(result).to_have_text(
        "You successfully clicked an alert"
    )

    print("JavaScript Alert 테스트 성공!")