from django.shortcuts import render, HttpResponse
from . import utils

def map_field_values(fields_dict):
    result = {k: utils.FieldTypes.get_type(v) for k, v in fields_dict.items()}
    return result


def load_templates():
    pass


def parse_request(request):
    if request.method == "POST":
        result = handle_request(request)
        return HttpResponse(result)
        # return HttpResponse('Hello')


def is_equal(field_types, template_field_types):
    pass


def handle_request(request):
    fields_dict = request.POST
    field_types = map_field_values(fields_dict)
    templates = load_templates()  # {template_name : {field_name1 : field_type1}}
    for templateKeyValue in templates.items():
        template_name, template_field_types = templateKeyValue[0], templateKeyValue[1]
        if is_equal(field_types, template_field_types):
            return template_name
    return field_types
