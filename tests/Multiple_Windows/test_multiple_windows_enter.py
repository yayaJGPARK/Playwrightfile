from playwright.sync_api import expect


def test_multiple_windows(page):

    page.goto("/windows")

    # 새 창이 열리는 것을 기다림
    with page.expect_popup() as popup_info:

        # Click here 링크 클릭
        page.get_by_role(
            "link",
            name="Click Here"
        ).click()

    # 새 창 가져오기
    new_page = popup_info.value

    input("선택 확인 → Enter")

    # 새 창 로딩 대기
    new_page.wait_for_load_state()

    input("선택 확인 → Enter")

    # 새 창의 제목 확인
    expect(new_page).to_have_title("New Window")

    input("선택 확인 → Enter")

    print("Multiple Windows 테스트 성공!")