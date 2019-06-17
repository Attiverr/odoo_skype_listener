import skpy
import threading

from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class MySkype(skpy.SkypeEventLoop):

    def send_notif_to_user(self, msg):
        _logger.warning(msg)
        
    def onEvent(self, event):
        if isinstance(event, skpy.SkypeNewMessageEvent):
            message = 'New message from user {} at {}: \'{} \''.format(event.msg.userId,
                                                                       event.msg.time.strftime('%H:%M dd. %d.%m.%Y'),
                                                                       event.msg.content)
            #you must add here functionality to pass the message to odoo user with id = 2 
            self.send_notif_to_user(message) # It is working, but only in console. I don't find how to send notifications or e-mails in odoo.
    
    
        
    # This code send e-mails to smtp server  
     
    # @api.multi
    # def send_mail(self):
      #  import smtplib

      #  receivers_email = self.user_target.login

      #  server = smtplib.SMTP('smtp.gmail.com', 587)
      #  server.starttls()
      #  server.login("your_email_address", "password")

      #  message = self.message_target
      #  server.sendmail("your_email_address", receivers_email, message)

      #  server.quit()               

class Skype_listener(models.Model):
    _name = 'test.model'    
    _auto = False
    _inherit = ['mail.thread']
    
    #@api.multi
    #@api.model_cr
    def init(self):
        from skpy import Skype
        # add your login and pass into skype profile
        # partner_id = self.env['res.users'].search([('id', '=', 2)]).partner_id.id        
        # print(partner_id)        
        client = Skype('attiverr', 'sdcsfrho22GSM10i', '.skype_token')
        sk = MySkype(tokenFile=".skype_token", autoAck=True)
        thread = threading.Thread(target=sk.loop)
        thread.start()
            
    
