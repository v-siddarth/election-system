import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
excel_file = 'output1.xlsx'
df.to_excel(excel_file, index=False)  # index=False to omit the DataFrame index





# import pandas as pd

# # Create a sample DataFrame
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [24, 27, 22, 32],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
# }
# df = pd.DataFrame(data)

# # Write the DataFrame to an Excel file with additional options
# excel_file = 'output.xlsx'
# with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
#     df.to_excel(writer, sheet_name='Sheet1', index=False)
    
#     # You can write additional DataFrames to different sheets
#     df.to_excel(writer, sheet_name='Sheet2', index=False)




# import pandas as pd

# # Create a sample DataFrame
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [24, 27, 22, 32],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
# }
# df = pd.DataFrame(data)

# # Write the DataFrame to an Excel file with xlsxwriter for formatting
# excel_file = 'output_with_formatting.xlsx'
# with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
#     df.to_excel(writer, sheet_name='Sheet1', index=False)
    
#     # Get the xlsxwriter workbook and worksheet objects
#     workbook  = writer.book
#     worksheet = writer.sheets['Sheet1']
    
#     # Add a format for the header cells
#     header_format = workbook.add_format({
#         'bold': True,
#         'text_wrap': True,
#         'valign': 'top',
#         'fg_color': '#D7E4BC',
#         'border': 1
#     })
    
#     # Write the column headers with the defined format
#     for col_num, value in enumerate(df.columns.values):
#         worksheet.write(0, col_num, value, header_format)
