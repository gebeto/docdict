from docdict import generate_for


def function_1():
    """@json
        @category hello world
        @name Duck #2
        @second_name Rubber
    """
    pass

def function_2():
    """@json
        @category hello
        @name LOL
        @name LOL2
    """
    pass




def test_generate():
	generated = generate_for(globals())
	assert len(generated) == 2
