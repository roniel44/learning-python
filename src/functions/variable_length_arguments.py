#if you have multiple/dynamic arguments  specified while defining the function
def my_dict_printer(*my_dict): 
	
	print ("Whole list/dict is", my_dict);
	
	for var in my_dict:
		print (var);
	return;
	
my_dict_printer({"hero": "Naga Siren", "type":"Carry"});
my_dict_printer(1, 2, 3 ,4, 5);