from matplotlib import pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def graphRepresent(testNames, studentScores, topperScore, name):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))

    yAxesValue = [x for x in range(0, 101, 5)]

    width = 0.2
    p = [x for x in range(0, len(testNames))]
    p1 = [j + width for j in p]
    plt.xlabel("test", fontsize=18)
    plt.ylabel("Score", fontsize=18)
    plt.title('Test Result Graph')
    # plt.plot(testNames, studentScores)

    plt.bar(p, topperScore, width, color="b", label="Topper")
    plt.bar(p1, studentScores, width, color="r", label=name)

    plt.xticks([x+width for x in p], testNames, rotation=20)
    plt.yticks(yAxesValue)

    plt.legend()
    graph = get_graph()
    return graph


# plt.bar(p, y, width, color="r", label="Topper")


# plt.savefig('m.pdf')
# plt.show()
