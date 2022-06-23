# This file is used to generate secret key for hmac, not to be used, secret key should be preserved, just to display how key was made

import secrets

text_file = open("secret_key.txt", "w")
n = text_file.write(secrets.token_hex(16))
text_file.close()
