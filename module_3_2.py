def send_email(message, recipient, *, sender="university.help@gmail.com"):
    check_email = [".com", ".ru", ".net"]

    def email_check(email):
        return "@" in email and any(email.endswith(domain) for domain in check_email)

    if not email_check(sender) or not email_check(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if sender == recipient:
        print("Невозможно отправить письмо самому себе")
    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса ", sender, "на адрес ", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, "на адрес ", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
