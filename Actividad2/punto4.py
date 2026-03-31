def mail_validator (mail):
    if(mail.__contains__("@") == False):
        return False
    if(mail[0] == "@" or mail[-1] == "@"):
        return False
    mail_splited = mail.split("@")
    if (mail_splited[0] == 0):
        return False
    if(mail_splited[0].__contains__(".") == False):
        return False
    mail_splited_point = mail.split(".")
    if(mail_splited_point[-1] < 2):
        return False
    return True

