from playwright.sync_api import expect


def test_iframe(page):

    page.goto("/iframe")

    # iframe 안으로 접근
    frame = page.frame_locator("#mce_0_ifr")

    # iframe 내부의 편집 영역 확인
    editor = frame.locator("body")

    expect(editor).to_be_visible()

    print("iFrame 확인 테스트 성공!")