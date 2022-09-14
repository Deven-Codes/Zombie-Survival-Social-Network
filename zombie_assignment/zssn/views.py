from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from zssn.serializers import Survivor, Location, SurvivorSerializer, LocationSerializer

@api_view(['GET', 'POST'])
def survivors(request):

    if request.method == 'GET':

        try:
            all_survivors = Survivor.objects.filter(is_infected=False)
            serializer = SurvivorSerializer(all_survivors, many=True)

            data = {
                'status': 200,
                'survivors': serializer.data
            }

            return Response(data = data, status=status.HTTP_200_OK)
        
        except Exception as e:
            data = {
                'status': 500,
                'error': 'Internal Server Error',
            }

            return Response(data = data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)