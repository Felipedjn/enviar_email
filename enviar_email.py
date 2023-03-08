import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#email remetente
username = "emailremetente@gmail.com"

#senha do app - https://myaccount.google.com/u/1/apppasswords
password = "senhaapp"

#email remetente
mail_from = "emailremetente@gmail.com"

#email destinarário
mail_to = "emaildestinatario@gmail.com"

#assunto do email
mail_subject = "assunto"

#mensagem do email
mail_body = "mensagem do email"

#conexão
mimemsg = MIMEMultipart()
mimemsg['From']=mail_from
mimemsg['To']=mail_to
mimemsg['Subject']=mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
connection.starttls()
connection.login(username,password)
connection.send_message(mimemsg)
connection.quit()

print(f"""\nEmail enviado:\n
De: {mail_from}
Para: {mail_to}
Assunto: {mail_subject}
Texto: {mail_body}\n""")

