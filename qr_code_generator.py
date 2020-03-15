import siaskynet
import pyinputplus as pyip
import qrcode
import pathlib
from datetime import datetime
import time
import webbrowser

blurb_prompt = 'Please enter your text or standard URL for your QR code: '
blurb_generating_qr = 'Generating your QR code...'
blurb_saved_locally = 'Your QR code has been saved locally as: '
blurb_current_directory = 'You will find it at the current directory: '
blurb_uploading_qr = 'Now uploading the QR to Skynet...'
blurb_description = 'This is the Skylink that you can share with anyone to retrieve the file on any Skynet Webportal:'
blurb_url = 'Please check at the follow link: '
blurb_host = 'https://siasky.net/'

blurb = pyip.inputStr(prompt=blurb_prompt)
print(blurb_generating_qr)
qr = qrcode.make(blurb)

# current date and time
now = datetime.now()
timestamp = str(int(datetime.timestamp(now)))

qr.save('qr' + '_' + timestamp + '.png')
print(blurb_saved_locally + 'qr' + '_' + timestamp + '.png')
path_to_qr = pathlib.Path().absolute()
print(blurb_current_directory + str(path_to_qr))
print()
print(blurb_uploading_qr)
print(blurb_description)
skylink = siaskynet.Skynet.UploadFile('qr' + '_' + timestamp + '.png', None)
print(skylink)
print()
url_link = blurb_host + skylink[6:]
print(blurb_url + url_link)
time.sleep(2)
webbrowser.open_new(url_link)
