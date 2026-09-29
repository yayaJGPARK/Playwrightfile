def test_google(page):
    page.goto("/")

    print(page.title())

    assert "Google" in page.title()