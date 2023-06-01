import lightrdf
from statistics import mean
from collections import defaultdict


def is_literal(node: str) -> bool:
    return node.startswith('"') and node.endswith('"')


def process_document(file_path: str) -> dict:
    doc = lightrdf.RDFDocument(file_path)

    entities = list()
    properties = list()
    literals = list()
    classes = list()

    number_of_connections = 0
    vertices_count_literals = defaultdict(int)

    for triple in doc.search_triples(None, None, None):
        sub = triple[0]
        prop = triple[1]
        obj = triple[2]

        entities.append(sub)

        if "type" in prop.lower() or "a" == prop.lower():
            classes.append(obj)
            continue

        properties.append(prop)

        is_obj_literal = is_literal(obj)

        if is_obj_literal:
            literals.append(obj)

        if not is_obj_literal:
            entities.append(obj)
            number_of_connections += 1

        if sub not in vertices_count_literals:
            vertices_count_literals[sub] = 0

        vertices_count_literals[sub] += 1

    connected_vertices = len(vertices_count_literals.keys())
    average_literals_per_vertex = mean(vertices_count_literals.values())

    return {
        "entities": entities,
        "properties": properties,
        "literals": literals,
        "classes": classes,
        "numberOfConnections": number_of_connections,
        "connectedVertices": connected_vertices,
        "literalsPerVertex": average_literals_per_vertex,
    }


if __name__ == "__main__":
    res = process_document("datasets/15243/en.rdf")
    # res = process_document("datasets/21023/2016-allievi-partecipanti.nt")

    # print(res)
