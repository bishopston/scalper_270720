def JSChartView1(request, tradesymbol):
    labels = []
    data = []

    option = Option.objects.filter(optionsymbol=tradesymbol).order_by('date')
    opt = option.all()

    for entry in opt:
        labels.append(json.dumps(entry.date.strftime("%d-%m-%Y")))
        data.append(entry.closing_price)

    print(data)
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })