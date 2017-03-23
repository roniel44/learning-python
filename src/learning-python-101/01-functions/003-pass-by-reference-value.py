# passing by reference - variable passed also changes value when the value is changed on the called function

def pass_by_reference_dict(my_dict):
    "This changes a passed list into this function"

    print("Values before", my_dict);
    my_dict["age"] = 25
    print("Values after", my_dict);

    return my_dict;


mah_dict = {"name": "Roniel", "age": 24}
pass_by_reference_dict(mah_dict)
print("value outside after calling the function", mah_dict);

print("\n");
print("\n");
print("\n");


# passing by value - variable passed does not change value when the value is changed on the called function

def pass_by_value_dict(my_dict):
    "some description here"

    print("Values before", my_dict);
    my_dict = [12, 12]
    print("Values after", my_dict);

    return;


diz_dict = {"name": "Roniel", "age": 24}
pass_by_value_dict(diz_dict)
print("value outside after calling the function", diz_dict);
