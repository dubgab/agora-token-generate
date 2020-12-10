import sys
import os
import time
from random import randint
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from .RtcTokenBuilder import RtcTokenBuilder,Role_Attendee

def get_tokenrtc(appID , appCertificate , channelName , uid , roles ,expireTimeInSeconds , currentTimestamp ,privilegeExpiredTs ):
    token = RtcTokenBuilder.buildTokenWithUid(appID, appCertificate, channelName, uid, roles, privilegeExpiredTs)
    return token
