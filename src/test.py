from py_simple_email import Email



email = Email( 
    EMAIL_HOST = 'email-smtp.ap-south-1.amazonaws.com', 
    EMAIL_HOST_USER = 'xxxxxxxxxxxxx', 
    EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxxxxxxxxxxxxx', 
    EMAIL_PORT= 587,
    EMAIL_USE_TLS = True,
    DEFAULT_FROM_EMAIL = 'Sanjay <info@sanjaysikdar.dev>',
)

# email.send(
#     to_email='sanjay@sanjaysikdar.dev',
#     subject='test mail 1',
#     msg='hello world 1',
# )

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://read.sanjaysikdar.dev">Sanjay Sikdar</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

email.send(
    to_email='sanjay@sanjaysikdar.dev',
    subject='htssml test mail 1',
    msg=html,
    is_html=True
)