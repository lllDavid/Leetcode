import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    
    return employees

data = {
    "name": ["John", "Alice", "Bob"],
    "salary": [1000, 1500, 2000]
}

df = pd.DataFrame(data)

modified_df = modifySalaryColumn(df)

print(modified_df)
