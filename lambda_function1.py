import json
import numpy
import PIL.Image as Image
from io import BytesIO

def lambda_handler(event, context):
    # TODO implement
    image = event['data']
    image = numpy.array(Image.open(BytesIO(image))).astype(numpy.float32)
    return {
        'statusCode': 200,
        'body': json.dumps(image.shape)
    }
