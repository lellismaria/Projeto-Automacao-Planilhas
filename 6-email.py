import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

# 1 - Dados do E-mail

password = open('senha', 'r').read().strip()
from_email = 'meslellis@gmail.com'
to_email = 'meslellis@gmail.com'
subject = 'Automação Planilha de Vendas'
body = """
Olá! Segue em anexo a automação da planilha de vendas
para a empresa XYZ Automação.

Qualquer dúvida estou à disposição.
"""

# 2 - Montando a estrutura do E-mail

message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body)
safe = ssl.create_default_context()

# 3 - Adicionar Anexo

anexo = 'test.xlsx'
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split("/") if mimetypes.guess_type(anexo)[0] else ('application', 'octet-stream')

with open(anexo, 'rb') as a:
    message.add_attachment(
        a.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anexo
    )

# 4 - Envio de E-mail

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
        smtp.login(from_email, password)
        smtp.sendmail(
            from_email,
            to_email,
            message.as_string()
        )
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar o e-mail: {e}")
