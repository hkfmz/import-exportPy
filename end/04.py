import resources

class formatNumResource(resources.ModelResource):

    class Meta:
        model = formatNum

class checkUsagerResource(resources.ModelResource):

    class Meta:
        model = checkUsager

class Demande_ProfilResource(resources.ModelResource):

    class Meta:
        model = Demande_Profil

class MailModelResource(resources.ModelResource):

    class Meta:
        model = MailModel

class Param_NotificationResource(resources.ModelResource):

    class Meta:
        model = Param_Notification

class SendMailResource(resources.ModelResource):

    class Meta:
        model = SendMail

class SendSMSResource(resources.ModelResource):

    class Meta:
        model = SendSMS

class smtpnonSSLResource(resources.ModelResource):

    class Meta:
        model = smtpnonSSL

class PasserelGSMResource(resources.ModelResource):

    class Meta:
        model = PasserelGSM

