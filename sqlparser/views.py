from django.db import connection
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def parse_sql(request):
    """ takes SQL and returns slack response """
    if request.method == 'POST':
        query = request.POST['text']
        cursor = connection.cursor()

        response = ""
        for row in xrange(cursor.execute(query)):
            response += ' '.join([str(x) for x in cursor.fetchone()]) + "\n"
        return HttpResponse(response)
    else:
        return HttpResponse("Something went wrong...")
