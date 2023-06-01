import lightrdf


def is_literal(node: str) -> bool:
    return node.startswith('"') and node.endswith('"')


def process_document(file_path: str) -> dict:
    doc = lightrdf.RDFDocument(file_path)

    entities = list()
    properties = list()
    literals = list()
    classes = list()

    for triple in doc.search_triples(None, None, None):
        sub = triple[0]
        prop = triple[1]
        obj = triple[2]

        entities.append(sub)

        if "type" in prop.lower() or "a" == prop.lower():
            classes.append(obj)
            continue

        properties.append(prop)

        if is_literal(obj):
            literals.append(obj)
        else:
            entities.append(obj)

    return {
        "entities": entities,
        "properties": properties,
        "literals": literals,
        "classes": classes,
    }


if __name__ == "__main__":
    res = process_document("datasets/15243/en.rdf")
    res = process_document("datasets/21023/2016-allievi-partecipanti.nt")

    # print(res)
