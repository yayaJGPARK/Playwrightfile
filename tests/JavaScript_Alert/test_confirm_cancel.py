from playwright.sync_api import expect

def test_confirm_cancel(page):

    page.goto("/javascript_alerts")

    # Confirm 버튼 찾기
    button = page.get_by_role(
        "button",
        name="Click for JS Confirm"
    )

    # Confirm → Cancel
    page.on("dialog", lambda dialog: dialog.dismiss())

    # 버튼 클릭
    button.click()

    # 결과 확인
    result = page.locator("#result")

    expect(result).to_have_text("You clicked: Cancel")

    print("Confirm Cancel 테스트 성공!")