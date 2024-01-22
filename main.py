import graphviz

def edges_to_dot(edges, directed=True):
    dot_code = "digraph G {\n" if directed else "graph G {\n  graph [directed=false];\n"
    dot_code += "  rankdir=LR;\n"
    dot_code += "  node[shape = circle, style = filled, color = lightblue];\n"
    dot_code += "  edge[color = black, fontcolor = blue];\n"

    for edge, labels in edges.items():
        u, v = edge
        for label in labels:
            edge_definition = f'  "{u}" {"->" if directed else "--"} "{v}"'
            if label and label != 'none':
                edge_definition += f' [label="{label}"]'
            edge_definition += ";\n"
            dot_code += edge_definition

    dot_code += "}\n"
    return dot_code


def read_from_file(file_path):
    edge_labels = {}
    with open(file_path, 'r') as file:
        for line in file:
            elements = line.strip().split()
            u, v = elements[:2]
            label = elements[2] if len(elements) > 2 else None
            edge = (u, v)
            if edge in edge_labels:
                edge_labels[edge].append(label)
            else:
                edge_labels[edge] = [label] if label else ['none']  # 处理label为空的情况
    return edge_labels


file_path = 'edges.txt'
edge_labels = read_from_file(file_path)

dot_code = edges_to_dot(edge_labels, directed=False)

print(dot_code)

graph = graphviz.Source(dot_code, format='png')
graph.render(filename='output_graph', cleanup=True, view=True)
