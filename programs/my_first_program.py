from nada_dsl import *

def nada_main(op="add"):
    p = Party("Party1")
    a, b = SecretInteger(Input("my_int1", p)), SecretInteger(Input("my_int2", p))
    r = {"add": a + b, "sub": a - b, "mul": a * b, "div": a / b if b else float('inf')}.get(op)
    return [Output(r, "result_output", p)]

if __name__ == "__main__":
    for o in nada_main("add"):
        print(f"Output name: {o.name}, Value: {o.value}, Party: {o.party.name}")
