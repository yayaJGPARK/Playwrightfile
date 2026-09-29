from playwright.sync_api import expect


def test_add_element(page):

    page.goto("/add_remove_elements/")

    # Add Element 버튼 찾기
    add_button = page.get_by_role(
        "button",
        name="Add Element"
    )

    input("선택 확인 → Enter")

    # 버튼 클릭
    add_button.click()

    input("선택 확인 → Enter")

    # Delete 버튼 확인
    delete_button = page.get_by_role(
        "button",
        name="Delete"
    )

    expect(delete_button).to_be_visible()

    print("Element 추가 테스트 성공!")

def test_delete_element(page):

    page.goto("/add_remove_elements/")

    # Add Element 버튼
    add_button = page.get_by_role(
        "button",
        name="Add Element"
    )

    input("선택 확인 → Enter")

    # Element 생성
    add_button.click()

    # Delete 버튼
    delete_button = page.get_by_role(
        "button",
        name="Delete"
    )

    input("선택 확인 → Enter")

    # 생성된 Element 삭제
    delete_button.click()

    input("선택 확인 → Enter")

    # Delete 버튼이 사라졌는지 확인
    expect(delete_button).not_to_be_visible()

    print("Element 삭제 테스트 성공!")