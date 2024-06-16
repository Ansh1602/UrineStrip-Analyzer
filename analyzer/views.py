# analyzer/views.py

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
import cv2
import numpy as np

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_image(request):
    file = request.FILES['file']
    npimg = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    
    # Process the image to extract RGB values for the 10 colors
    # Here we just mock the response for demonstration purposes
    result = {
        'URO': [206, 193, 187],
        'BIL': [202, 185, 164],
        'KET': [193, 171, 153],
        'BLD': [204, 159, 54],
        'PRO': [191, 172, 130],
        'NIT': [203, 189, 170],
        'LEU': [194, 175, 164],
        'GLU': [128, 173, 163],
        'SG': [191, 159, 76],
        'PH': [206, 152, 106]
    }
    
    return JsonResponse(result)
