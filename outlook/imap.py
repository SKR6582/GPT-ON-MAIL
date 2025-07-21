import imaplib
import email
from email.header import decode_header

def receive_emails_outlook(email_address, app_password, folder="INBOX", limit=5):
    mail = imaplib.IMAP4_SSL("outlook.office365.com")
    mail.login(email_address, app_password)
    mail.select(folder)

    result, data = mail.search(None, "ALL")
    mail_ids = data[0].split()

    print(f"{len(mail_ids)}개의 메일이 검색됨")

    for i in mail_ids[-limit:]:
        result, msg_data = mail.fetch(i, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8")
        print(f"제목: {subject}")
        print(f"보낸 사람: {msg.get('From')}")
        print("-" * 30)

    mail.logout()