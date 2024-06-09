from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer, QuestionSerializer
from rest_framework.permissions import IsAuthenticated
from .common.paginate import CommonPagination
from .service.bot import Bot

# Create your views here.
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = CommonPagination

    def ask_bot(self, request):
        # validation
        serializer = QuestionSerializer(data=request.data)
        if(serializer.is_valid() == False): 
            return Response({'status': f'input wrong'}, status=status.HTTP_400_BAD_REQUEST)
        
        q = serializer.validated_data['question']
        bot = Bot()
        answer = bot.ask(q)
        return Response({'answer': f'{answer}'}, status=status.HTTP_200_OK)


    def censor_message(self, request, pk=None):
        print(pk)
        return Response({'status': f'message {pk} censored'}, status=status.HTTP_200_OK)

        try:
            message = self.get_object()
            message = '***********'
            message.save()
            return Response({'status': f'message {pk} censored'}, status=status.HTTP_200_OK)
        except Message.DoesNotExist:
            return Response({'error': f'message {pk} censored'}, status=status.HTTP_404_NOT_FOUND)
