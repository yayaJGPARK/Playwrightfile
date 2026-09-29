from playwright.sync_api import expect


def test_iframe(page):

    page.goto("/iframe")

    # iframe 안으로 접근
    frame = page.frame_locator("#mce_0_ifr")

    input("선택 확인 → Enter")

    # iframe 내부의 편집 영역 확인
    editor = frame.locator("body")

    input("선택 확인 → Enter")

    expect(editor).to_be_visible()

    print("iFrame 확인 테스트 성공!")