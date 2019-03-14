def simple_xml_object(tag, value):
    return xml_object_with_attributes(tag, value, [])


def xml_object_with_attributes(tag, value, attr_list):
    attr_str = get_attribute_list_from_dict(attr_list)

    return "<" + tag + attr_str + ">" + value + "</" + tag + ">"


def get_attribute_list_from_dict(attr_dict):
    if len(attr_dict) == 0:
        return ""

    attr_str = " "

    for attr in attr_dict:
        attr_dict += "" + attr.key + "=\"" + attr.value + "\" "

    return attr_str
