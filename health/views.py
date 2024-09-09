from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def healthCheck(request):
    logger.warning('================================== START - Application Health =================================')
    response,exception,statusCode = {},False,200
    sysTimeNow = datetime.now().strftime('%d-%m-%Y, %I:%M:%S.%f %p')
    logger.info(f'Health Check API - System Local Time : >>>> {sysTimeNow}')
    output = {}
    output['Time'] = sysTimeNow
    output['Condition'] = "OK"
    output['DjangoApp'] = "Health App"
    try:
        check = request.GET.get('check')
        if check == 'true':
            output['Message'] = "Application is running."
        else:
            output['Message'] = "Not Authorized"
        response = output
    except Exception as e:
        logger.exception(e)
        output['Message'] = "Error Encountered."
        exception,response,statusCode = True,output,510
    finally:
        logger.warning('=================================== END - Application Health ==================================\n')
        return Response(status = statusCode, data = {"data":response,"exception":exception})
