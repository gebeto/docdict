from DocString2Json import DocString2Json2


def generate_for(scope):
    # json_docs = []
    # for function_name, function in scope.items():
    #     doc = function.__doc__
    #     if doc and doc.find("@json") == 0:
    #         json_docs.append(DocString2Json2(doc.replace("@json", "")))

    json_docs = (
        DocString2Json2(function.__doc__.replace("@json", ""))
        for function_name, function
        in scope.items()
        if function.__doc__ and function.__doc__.find("@json") == 0
    )

    # return (dict(doc) for doc in json_docs)
    for doc in json_docs:
        print dict(doc)
    return []


def test():
    """@json
        @category hello world
        @name LOL
        @name LOL2
    """
    pass

gen = generate_for(globals())
res = {}
print [g for g in gen]
# for g in gen:
#     category = g.get("category")
#     if not category: continue
#     if not res.get(category): res[category] = []
#     res[category].append(g)

# print res