from enum import Enum
from lxml import etree


class TripleType(Enum):
    SUBJECT_PREDICATE_OBJECT = 0
    PREDICATE_OBJECT = 1
    OBJECT = 2


def parse_TTL(path_to_file: str) -> dict:
    classes = list()
    entities = list()
    properties = list()
    literals = list()

    with open(path_to_file, "r", encoding="utf-8") as file:
        # read all the prefixes
        while True:
            line = file.readline()
            if "@prefix" not in line:
                break

        last_subject = None
        last_predicate = None
        next_triple = TripleType.SUBJECT_PREDICATE_OBJECT

        while True:
            line = file.readline()

            if not line:
                break

            # check if the line is empty (only \n in it)
            if line != "\n":
                object = None

                if next_triple == TripleType.SUBJECT_PREDICATE_OBJECT:
                    split = line.split(" ")
                    last_subject = split[0]
                    last_predicate = split[1]
                    object = split[2]

                if next_triple == TripleType.PREDICATE_OBJECT:
                    i = 0
                    while line[i] == " ":
                        i += 1

                    # read the predicate
                    j = i
                    while line[j] != " ":
                        j += 1

                    last_predicate = line[i:j]

                    # read the object
                    object = line[j + 1 : len(line)]

                if next_triple == TripleType.OBJECT:
                    j = 0
                    while line[j] == " ":
                        j += 1

                    object = line[j + 1 : len(line)]

                # check the type of the next triple
                if ",\n" in object:
                    next_triple = TripleType.OBJECT

                if ";\n" in object:
                    next_triple = TripleType.PREDICATE_OBJECT

                if ".\n" in object:
                    next_triple = TripleType.SUBJECT_PREDICATE_OBJECT

                # categorize entities and classes
                if last_predicate == "a" or last_predicate == "rdfs:type":
                    entities.append(last_subject)
                    if "." in object:
                        classes.append(object.strip(".\n"))
                    if ";" in object:
                        classes.append(object.strip(";\n"))

                # add property
                properties.append(last_predicate)

                # add literals
                if '"' in object:
                    if ".\n" in object:
                        literals.append(object.strip(".\n"))
                    if ";\n" in object:
                        literals.append(object.strip(";\n"))
                    if ",\n" in object:
                        literals.append(object.strip(";\n"))

    return {
        "entities": entities,
        "classes": classes,
        "properties": properties,
        "literals": literals,
    }


def parse_as_XML(file_path: str) -> dict:
    classes = list()
    entities = list()
    literals = list()
    properties = list()

    parser = etree.XMLParser(recover=True)

    try:
        tree = etree.parse(file_path, parser)

        root = tree.getroot()

        if root == None:
            raise Exception("File cannot be parsed as XML")

        for element in root.iter():
            # print(f"Tag: {str(element.tag)} Text:{str(element.text)}")

            tag = element.tag.lower()
            keys = (
                [x.lower() for x in element.attrib.keys()[0]]
                if len(element.attrib.keys()) > 0
                else None
            )

            if "description" in tag:
                if keys != None:
                    if "about" in keys:
                        entities.append(element.get(keys))

            elif "type" in tag:
                if keys != None:
                    if "resource" in keys:
                        classes.append(element.get(keys))

            elif "}" in tag:
                split = element.tag.split("}")
                property = split[1].lower()
                if property != "rdf" and property != "description":
                    properties.append(property)

            else:
                properties.append(element.tag)

            if element.text != None and element.text.strip():
                literals.append(element.text)

    except Exception as e:
        print(f"{file_path} EXCEPTION: {str(e)}")

    return {
        "entities": entities,
        "classes": classes,
        "properties": properties,
        "literals": literals,
    }
