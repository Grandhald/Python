ls = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, 
{" VIII":" S007 "}] 

uni_elem = set([value.replace(" ", "") for item in ls for value in item.values() ])

print(uni_elem)