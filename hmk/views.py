from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib
import json
from datetime import datetime
import requests
import os


@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:

            data = request.POST

            if data and data.get('dtmfDigits') == None and data.get('recordingUrl') == None:
                print(data)
                # Compose the XML response
                response = '<?xml version="1.0" encoding="UTF-8"?>'
                response += '<Response>'
                #response += '<Say>Welcome to H.M.K Clinic: A virtual clinic made to connect rural communities to quality healthcare</Say>'
                response += '<Play url="https://atary.pythonanywhere.com/media/for_hausa_press_1.mp3"/>'
                response += '<Say>For English press 5 then hash after the beep.</Say>'
                response += '<GetDigits timeout="30" finishOnKey="#" numDigits="1">'
                response += '<Play url="https://atary.pythonanywhere.com/media/beep.mp3"/>'
                response += '</GetDigits>'
                response += '</Response>'
                return HttpResponse(response, content_type='text/plain')

            elif data.get('recordingUrl') != None:
                current_time = datetime.now()
                formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
                current_dir = os.path.dirname(os.path.abspath(__file__))
                media_dir = os.path.join(current_dir, '../media')
                urllib.request.urlretrieve(data['recordingUrl'], media_dir +"/"+ f'{data["callerNumber"]}_{formatted_time}.mp3')
                response = '<?xml version="1.0" encoding="UTF-8"?>'
                response += '<Response>'
                response += '<Say>Thank you for your report. We value your diligence and commitment as a patriotic citizen</Say>'
                response += '</Response>'
                return HttpResponse(response, content_type='text/plain')

            elif int(data['dtmfDigits']) == 1:
                response = '<?xml version="1.0" encoding="UTF-8"?>'
                response += '<Response>'
                response += '<Play url="https://atary.pythonanywhere.com/media/welcome.mp3"/>'
                response += '<GetDigits timeout="30" finishOnKey="#" numDigits="1">'
                response += '<Play url="https://atary.pythonanywhere.com/media/to_speak_to_update_hausa.mp3"/>'
                response += '</GetDigits>'
                #response += '<Say>Please Hold a Healthcare professional will be with you shortly</Say>'
                #response += '<Dial phoneNumbers="+2348037568761" ringbackTone="https://atary.pythonanywhere.com/media/a_music.mp3" record="true" maxDuration="120" sequential="true" />'
                response += '</Response>'
                return HttpResponse(response, content_type='text/plain')

            elif int(data['dtmfDigits']) == 2:
                response  = '<?xml version="1.0" encoding="UTF-8"?>'
                response += '<Response>'
                response += '<Play url="https://atary.pythonanywhere.com/media/please_hold.mp3"/>'
                #response += '<Say>Please Hold a Healthcare professional will be with you shortly</Say>'
                response += '<Dial phoneNumbers="+2349084512241" ringbackTone="https://atary.pythonanywhere.com/media/a_music.mp3" record="true" maxDuration="120" sequential="true" />'
                #response += '<Record finishOnKey="#" maxLength="10" trimSilence="true" playBeep="true" callbackUrl="https://atary.pythonanywhere.com/">'
                #response += '<Say>Tell us everything about the unusual illness after this message. To end your report press hash.</Say>'
                #response += '</Record>'
                response += '</Response>'
                return HttpResponse(response, content_type='text/plain')

            elif int(data['dtmfDigits']) == 3:
                response  = '<?xml version="1.0" encoding="UTF-8"?>'
                response += '<Response>'
                response += '<Record finishOnKey="#" maxLength="10" trimSilence="true" playBeep="true" callbackUrl="https://atary.pythonanywhere.com/">'
                response += '<Play url="https://atary.pythonanywhere.com/media/tell_us_everything_hausa.mp3"/>'
                response += '</Record>'
                #response += '<Record finishOnKey="#" maxLength="120" trimSilence="true" playBeep="true" callbackUrl="https://atary.pythonanywhere.com/">'
                #response += '<Say>Pls tell describe to us your location in detail. To end your request press hash.</Say>'
                #response += '</Record>'
                response += '</Response>'
                return HttpResponse(response, content_type='text/plain')

            elif int(data['dtmfDigits']) == 4:
                response  = '<?xml version="1.0" encoding="UTF-8"?>'
                response += '<Response>'
                response += '<Record finishOnKey="#" maxLength="10" trimSilence="true" playBeep="true" callbackUrl="https://atary.pythonanywhere.com/">'
                response += '<Play url="https://atary.pythonanywhere.com/media/tell_your_location_in_detail.mp3"/>'
                response += '</Record>'
                #response += '<Record finishOnKey="#" maxLength="120" trimSilence="true" playBeep="true" callbackUrl="https://atary.pythonanywhere.com/">'
                #response += '<Say>Pls tell describe to us your location in detail. To end your request press hash.</Say>'
                #response += '</Record>'
                response += '</Response>'
                return HttpResponse(response, content_type='text/plain')

            elif int(data['dtmfDigits']) == 5:
                response  = '<?xml version="1.0" encoding="UTF-8"?>'
                response += '<Response>'
                response += '<Say>Welcome to H.M.K Clinic: A virtual clinic made to connect rural communities to quality healthcare</Say>'
                response += '<GetDigits timeout="30" finishOnKey="#" numDigits="1">'
                response += '<Say>To speak to a Healthcare Professional Press 6 followed by hash. To report an unusual illness Press 7 followed by hash. To request for an ambulance Press 8 followed by hash</Say>'
                response += '</GetDigits>'
                #response += '<Record finishOnKey="#" maxLength="120" trimSilence="true" playBeep="true" callbackUrl="https://atary.pythonanywhere.com/">'
                #response += '<Say>Pls tell describe to us your location in detail. To end your request press hash.</Say>'
                #response += '</Record>'
                response += '</Response>'
                return HttpResponse(response, content_type='text/plain')

            elif int(data['dtmfDigits']) == 6:
                response  = '<?xml version="1.0" encoding="UTF-8"?>'
                response += '<Response>'
                response += '<Say>Please Hold a Healthcare professional will be with you shortly</Say>'
                response += '<Dial phoneNumbers="+2349084512241" ringbackTone="https://atary.pythonanywhere.com/media/a_music.mp3" record="true" maxDuration="120" sequential="true" />'
                response += '</Response>'
                return HttpResponse(response, content_type='text/plain')

            elif int(data['dtmfDigits']) == 7:
                response  = '<?xml version="1.0" encoding="UTF-8"?>'
                response += '<Response>'
                response += '<Record finishOnKey="#" maxLength="10" trimSilence="true" playBeep="true" callbackUrl="https://atary.pythonanywhere.com/">'
                response += '<Say>Tell us everything about the unusual illness after this message. To end your report press hash.</Say>'
                response += '</Record>'
                response += '</Response>'
                return HttpResponse(response, content_type='text/plain')

            elif int(data['dtmfDigits']) == 8:
                response  = '<?xml version="1.0" encoding="UTF-8"?>'
                response += '<Response>'
                response += '<Record finishOnKey="#" maxLength="10" trimSilence="true" playBeep="true" callbackUrl="https://atary.pythonanywhere.com/">'
                response += '<Say>Pls tell describe to us your location in detail. To end your request press hash.</Say>'
                response += '</Record>'
                response += '</Response>'
                return HttpResponse(response, content_type='text/plain')

            elif int(data['dtmfDigits']) not in [1, 2, 3, 4, 5, 6, 7, 8]:
                response = '<?xml version="1.0" encoding="UTF-8"?>'
                response += '<Response>'
                response += '<Say>You entered an invalid input. Please wait for all the options to be said before responding to an input</Say>'
                response += '</Response>'
                return HttpResponse(response, content_type='text/plain')

            else:
                response_data = {
                    'duration': data.get('durationInSeconds'),
                    'currencyCode': data.get('currencyCode'),
                    'amount': data.get('amount'),
                }
                return JsonResponse(response_data)

        except json.JSONDecodeError:
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<Say>You entered an invalid input. Please wait for all the options to be said before responding to an input</Say>'
            response += '</Response>'
            return HttpResponse(response, content_type='text/plain')

        except ValueError:
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<Say>You entered an invalid input. Please wait for all the options to be said before responding to an input</Say>'
            response += '</Response>'
            return HttpResponse(response, content_type='text/plain')

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
