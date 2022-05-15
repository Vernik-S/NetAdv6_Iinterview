'''
Мы устроились на новую работу. Бывший сотрудник начал разрабатывать модуль для работы с почтой, но не успел доделать его. Код рабочий. Нужно только провести рефакторинг кода.

1. Создать класс для работы с почтой;
2. Создать методы для отправки и получения писем;
3. Убрать "захардкоженный" код. Все значения должны определяться как аттрибуты класса, либо аргументы методов;
4. Переменные должны быть названы по стандарту PEP8;
5. Весь остальной код должен соответствовать стандарту PEP8;
6. Класс должен инициализироваться в конструкции.
```python
if __name__ == '__main__'
```
'''

# Скрипт для работы с почтой.
# ```python
import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class GmailMessenger:
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def send_message(self, subject, recipients, message):
        # send message
        def create_msg():
            msg = MIMEMultipart()
            msg['From'] = self.login
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject
            msg.attach(MIMEText(message))
            return True

        def send_smtp(message_internal):
            ms = smtplib.SMTP(GmailMessenger.GMAIL_SMTP, 587)
            # identify ourselves to smtp gmail client
            ms.ehlo()
            # secure our email with tls encryption
            ms.starttls()
            # re-identify ourselves as an encrypted connection
            ms.ehlo()

            ms.login(self.login, self.password)
            ms.sendmail(self.login, ms, message_internal.as_string())
            ms.quit()
            # send end
            return True

        message = create_msg()
        send_smtp(message)

    def receive(self, header=None):
        # recieve

        def init_mail():
            mail_internal = imaplib.IMAP4_SSL(GmailMessenger.GMAIL_IMAP)
            mail_internal.login(self.login, self.password)
            mail_internal.list()
            mail_internal.select("inbox")
            return mail_internal

        def get_mail():
            criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
            result, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_string(raw_email)
            mail.logout()
            # end recieve
            return email_message

        mail = init_mail()
        return get_mail()


if __name__ == "__main__":
    login_t = 'login@gmail.com'
    password_t = 'qwerty'
    subject_t = 'Subject'
    recipients_t = ['vasya@email.com', 'petya@email.com']
    message_t = 'Message'

    messenger = GmailMessenger(login_t, password_t)
    messenger.send_message(subject_t, recipients_t, message_t)
    print(messenger.receive())
