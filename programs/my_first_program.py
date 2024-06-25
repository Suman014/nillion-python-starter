from nada_dsl import *

def nada_main():
    # Define the party and inputs
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform a computation on the inputs (example: addition)
    result = my_int1 + my_int2

    # Return the result as output
    return [Output(result, "result_output", party1)]

# Run the function to see the output (assuming a testing environment)
if __name__ == "__main__":
    outputs = nada_main()
    for output in outputs:
        print(f"Output name: {output.name}, Value: {output.value}, Party: {output.party.name}")
