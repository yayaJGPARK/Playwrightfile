def test_web(page):

    page.goto("/")

    print(page.title())

    assert "The Internet" in page.title()