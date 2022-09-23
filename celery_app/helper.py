from django.core.mail import send_mail


def send_mail_without_celery():
    # send_mail('CELERY WORKED YEAH', "CELERY IS COOL",
    #           "samruddhi.talekar@thinkitive.com", ["talekarsamruddhi2000@gmail.com"], fail_silently=False)
    print("hello sam")
    return None
