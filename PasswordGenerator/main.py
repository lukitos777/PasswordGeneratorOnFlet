import flet, random, string


def main(page: flet.page):
    page.title = 'Password Generator'
    page.theme_mode = 'dark'
    page.window_width = 500
    page.window_height = 500
    page.window_resizable = False
    page.vertical_aligment = flet.MainAxisAlignment.CENTER

    use_a_z, use_A_Z, use_symbols, use_digits = False, False, False, False

    def checker_a_z(e):
        nonlocal use_a_z
        use_a_z = True if check_a_z.value else False

    def checker_A_Z(e):
        nonlocal use_A_Z
        use_A_Z = True if check_A_Z.value else False

    def checker_symbols(e):
        nonlocal use_symbols
        use_symbols = True if check_symbols.value else False

    def checker_digits(e):
        nonlocal use_digits
        use_digits = True if check_digits.value else False

    def generate(e):
        nonlocal use_a_z, use_A_Z, use_symbols, use_digits
        nonlocal generated_password, length_text_field

        try:
            password_length = int(length_text_field.value)
        except ValueError:
            generated_password.value = 'Invalid length. Please enter an integer from 8 to 16.'
            page.update()
            return

        if not (8 <= password_length <= 16) or not length_text_field.value.isdigit():
            generated_password.value = 'Invalid length. Please enter an integer from 8 to 16.'
            page.update()
            return

        lowercase_chars = string.ascii_lowercase if use_a_z else ''
        uppercase_chars = string.ascii_uppercase if use_A_Z else ''
        symbol_chars = '!@#$%^&*_' if use_symbols else ''
        digit_chars = string.digits if use_digits else ''

        all_chars = lowercase_chars + uppercase_chars + symbol_chars + digit_chars

        if not all_chars:
            generated_password.value = 'Please select at least one character set.'
            page.update()
            return

        password = ''.join(random.choice(all_chars) for _ in range(password_length))

        generated_password.value = password
        page.update()

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        theme_button.icon = flet.icons.SUNNY if page.theme_mode == 'dark' else flet.icons.SHIELD_MOON_ROUNDED
        page.update()

    generated_password = flet.Text()
    check_a_z = flet.Checkbox(label="a-z", value=False, on_change=checker_a_z)
    check_A_Z = flet.Checkbox(label="A-Z", value=False, on_change=checker_A_Z)
    check_symbols = flet.Checkbox(label="!@#$%^&*_", value=False, on_change=checker_symbols)
    check_digits = flet.Checkbox(label="0-9", value=False, on_change=checker_digits)
    length_text_field = flet.TextField(label='Enter any integer from 8 to 16')
    generate_button = flet.ElevatedButton('GENERATE PASSWORD', on_click=generate)
    theme_button = flet.IconButton(icon=flet.icons.SUNNY, on_click=change_theme)

    page.add(flet.Column(
        controls=[
            flet.Row(
                controls=[
                    check_a_z, check_A_Z, check_symbols, check_digits
                ],
                alignment=flet.MainAxisAlignment.CENTER
            ),
            flet.Row(
                controls=[
                    length_text_field,
                ],
                alignment=flet.MainAxisAlignment.CENTER
            ),
            flet.Row(
                controls=[
                    generate_button, theme_button
                ],
                alignment=flet.MainAxisAlignment.CENTER
            ),
            flet.Row(
                controls=[
                    generated_password
                ],
                alignment=flet.MainAxisAlignment.CENTER
            )
        ]
    ))


if __name__ == '__main__':
    flet.app(target=main)