import re

my_regex = re.compile(
    r"^\s*(It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.)$",
    re.MULTILINE
)
phone_number = r""
phone_regex = re.compile(phone_number)

email_address = r""
email_regex = re.compile(email_address)
