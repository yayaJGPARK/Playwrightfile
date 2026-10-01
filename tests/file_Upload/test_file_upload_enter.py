from playwright.sync_api import expect


def test_file_upload(page):

    page.goto("/upload")

    # 파일 선택
    file_input = page.locator("#file-upload")

    file_input.set_input_files(
        "tests/file_Upload/test.txt"
    )

    input("선택 확인 → Enter")

    # Upload 버튼 클릭
    upload_button = page.get_by_role(
        "button",
        name="Upload"
    )

    input("선택 확인 → Enter")

    upload_button.click()

    # 업로드 결과 확인
    result = page.get_by_text("test.txt")

    input("선택 확인 → Enter")

    expect(result).to_be_visible()

    print("File Upload 테스트 성공!")