from playwright.sync_api import expect


def test_alert(page):

    page.goto("/javascript_alerts")

    # Alert 버튼 찾기
    button = page.get_by_role("button", name="Click for JS Alert")

    # Alert 처리
    page.on("dialog", lambda dialog: dialog.accept())

    # 버튼 클릭
    button.click()

    # 결과 확인
    result = page.locator("#result")

    expect(result).to_have_text("You successfully clicked an alert")

    print("JavaScript Alert 테스트 성공!")