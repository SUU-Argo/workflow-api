from hera.workflows import DAG, Parameter, Workflow, script
from hera.workflows.models import ValueFrom


@script()
def generate(count: int, text: str):
    import json
    import sys
    lines = text.split("\n")
    values=[[] for _ in range(count)]
    for i, line in enumerate(lines):
        values[i % count].append(line)
    json.dump([{"value": "\n".join(values[i])} for i in range(count)], sys.stdout)


@script(outputs=[Parameter(name="value", value_from=ValueFrom(path="/tmp/value"))])
def count_words(object: dict):
    from collections import defaultdict
    import json
    print("Received object: {object}!".format(object=object))
    # Output the content of the "value" key in the object
    value = object["value"]
    words = value.split()
    counts = defaultdict(int)
    for word in words:
        counts[word] += 1
    with open("/tmp/value", "w") as f:
        f.write(json.dumps(counts))


@script()
def sum_counts(values: list):
    import json
    from collections import defaultdict

    total_counts = defaultdict(int)
    for value in values:
        parsed_val=json.loads(value)
        for word, count in parsed_val.items():
            total_counts[word] += count
    print("Counted values: ", json.dumps(total_counts))



def map_reduce_workflow(num_workers: int, text: str):
    with Workflow(generate_name="map-reduce", entrypoint="d") as w:
        with DAG(name="d"):
            g = generate(arguments={"count":num_workers, "text":text})
            cnt = count_words(with_param=g.result)
            fin = sum_counts(arguments=cnt.get_parameter("value").with_name("values"))
            g >> cnt >> fin
        w.create()
        return {"workflow_name": w.name}

