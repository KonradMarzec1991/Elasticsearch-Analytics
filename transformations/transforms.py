def transform_filter_names(es_input):
    from transformations.models import Employee
    result = []
    for emp in es_input:
        emp = emp['_source']
        result.append(Employee(
            FirstName=emp['FirstName'],
            LastName=emp['LastName'],
            Address=emp['Address'],
            MaritalStatus=emp['MaritalStatus'],
            Gender=emp['Gender'],
            Salary=emp['Salary'],
            Age=emp['Age'],
            Interests=emp['Interests'],
            DateOfJoining=emp['DateOfJoining'],
            Designation=emp['Designation'],
        ))
    return result