def saveTimeCollectMethod(request):
    request.DATA.update(request.DATA['value'])
    del request.DATA['value']

    errors = False

    if request.method == 'PUT':
        response = TimeCollectResponse.objects.get(pk=request.DATA['id'])
        serializer = TimeCollectResponseSerializer(response, data = request.DATA)
    elif request.method == 'POST':
        serializer = TimeCollectResponseSerializer(data = request.DATA)

    if serializer.is_valid():
        serializer.save()
        question_id = serializer.data['id']

    else:
        errors = True
        request.DATA['errors'] = serializer.errors

    if errors:
        return Response(request.DATA, status=status.HTTP_400_BAD_REQUEST)

    question = QuestionResponse.objects.get(pk=question_id)
    return Response(QuestionResponseReadSerializer(question).data)

