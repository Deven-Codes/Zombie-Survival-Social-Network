from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from zssn.serializers import Survivor, Location, SurvivorSerializer, LocationSerializer

@api_view(['GET', 'POST'])
def survivors(request):

    # if request in GET method
    if request.method == 'GET':

        try:
            # get all non infected survivors
            all_survivors = Survivor.objects.filter(is_infected=False)

            # serialize all_survivors query set 
            serializer = SurvivorSerializer(all_survivors, many=True)

            # prepare data to send
            data = {
                'status': 200,
                'survivors': serializer.data
            }

            # return repsonse with status 200
            return Response(data = data, status=status.HTTP_200_OK)
        
        # if some exception occurs
        except Exception as e:

            print(f'Error while processing /survivors request(GET): {e}')

            # prepare data accordingly
            data = {
                'status': 500,
                'error': 'Internal Server Error',
            }

            # return repsonse with status 500
            return Response(data = data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        survivor_location = None
        survivor = None

        try:
            # Serialize request data
            serializer = SurvivorSerializer(data=request.data)

            # Check if data is valid
            if serializer.is_valid():
                
                # save data 
                serializer.save()

                # prepare response data to send 
                data = {
                    'status': 200,
                    'message': 'Successfully created',
                    'data': serializer.data
                }

                # return repsonse with status 200
                return Response(data = data, status=status.HTTP_200_OK)

            # data is not valid
            else:

                # prepare response data to send 
                data = {
                    'status': 400,
                    'message': 'Bad Request',
                    'data': serializer.errors
                }

                # return repsonse with status 400
                return Response(data = data, status=status.HTTP_400_BAD_REQUEST)


        # Some exception have occured
        except Exception as e:
            print(f'Exception: {e}')

            data = {
                'status': 500,
                'error': 'Internal Server Error',
            }

            return Response(data = data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)