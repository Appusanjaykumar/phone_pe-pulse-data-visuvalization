import os
import json
import pandas as pd
import sqlite3
import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px

# Connect to the SQLite database
conn = sqlite3.connect('phonepe.db')
cursor = conn.cursor()

# Specify the root directory where your data is located
root_dir = r'C:\Users\ELCOT\Desktop\phone\data\aggregated\transaction\country\india\state'

# Initialize an empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)
    if os.path.isdir(state_path):
        
        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):
                
                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)
                            
                            # Extract the data we're interested in
                            for transaction_data in data['data']['transactionData']:
                                row_dict = {
                                    'States': state_dir,
                                    'Transaction_Year': year_dir,
                                    'Quarters': int(json_file.split('.')[0]),
                                    'Transaction_Type': transaction_data['name'],
                                    'Transaction_Count': transaction_data['paymentInstruments'][0]['count'],
                                    'Transaction_Amount': transaction_data['paymentInstruments'][0]['amount']
                                }
                                data_list.append(row_dict)

# Convert the list of dictionaries to a DataFrame
df1 = pd.DataFrame(data_list)

# Now you can work with the DataFrame 'df' to analyze and manipulate the data
print(df1)





import os
import json
import pandas as pd

# Specify the root directory where your JSON files are located
root_dir = r'C:\Users\ELCOT\Desktop\phone\data\aggregated\user\country\india\state'

# Initialize an empty list to hold extracted data
data_list = []

# Loop over all state folders in the root directory
for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)

    # Check if it's a directory (representing a state)
    if os.path.isdir(state_path):
        
        # Loop over all year folders in the state directory
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            
            # Check if it's a directory (representing a year)
            if os.path.isdir(year_path):
                
                # Loop over all JSON files in the year directory
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file), 'r') as f:
                            json_data = json.load(f)
                            
                            # Extract data from the JSON as needed
                            if 'data' in json_data:
                                data = json_data['data']
                                
                                # Extract brand data from usersByDevice if it exists
                                users_by_device = data.get('usersByDevice')
                                if users_by_device:
                                    for device_data in users_by_device:
                                        brand = device_data.get('brand', 'N/A')
                                        count = device_data.get('count', 0)
                                        percentage = device_data.get('percentage', 0.0)
                                        
                                        # Extract the quarter number from the JSON file name
                                        quarters = int(json_file.split('.')[0])
                                        
                                        # Create a dictionary with the extracted data
                                        row_dict = {
                                            'State': state_dir,
                                            'Transaction_Year': year_dir,
                                            'Quarters': int(json_file.split('.')[0]),
                                            'Brand': brand,
                                            'Transaction_Count': count,
                                            'Percentage': percentage
                                        }
                                        data_list.append(row_dict)

# Convert the list of dictionaries to a Pandas DataFrame
df2 = pd.DataFrame(data_list)



# Now you have the quarter numbers in the "Quarters" column
print(df2)  # Display the first few rows of the DataFrame



import os
import json
import pandas as pd

# Specify the root directory where your JSON files are located
root_dir = r'C:\Users\ELCOT\Desktop\phone\data\map\transaction\hover\country\india\state'

# Initialize an empty list to hold extracted data
data_list = []

# Loop over all state folders in the root directory
for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)

    # Check if it's a directory (representing a state)
    if os.path.isdir(state_path):
        
        # Loop over all year folders in the state directory
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            
            # Check if it's a directory (representing a year)
            if os.path.isdir(year_path):
                
                # Loop over all JSON files in the year directory
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file), 'r') as f:
                            json_data = json.load(f)
                            
                            # Extract data from the JSON as needed
                            if 'data' in json_data:
                                data = json_data['data']
                                
                                # Extract data from 'hoverDataList' or 'hoverData' if it exists
                                hover_data_list = data.get('hoverDataList')
                                if hover_data_list:
                                    for item in hover_data_list:
                                        name = item.get('name', 'N/A')
                                        metrics = item.get('metric')
                                        if metrics and isinstance(metrics, list) and len(metrics) > 0:
                                            metric = metrics[0]
                                            metric_type = metric.get('type', 'N/A')
                                            count = metric.get('count', 0)
                                            amount = metric.get('amount', 0.0)
                                            
                                            # Extract the quarter number from the JSON file name
                                            quarters = int(json_file.split('.')[0])
                                            
                                            # Create a dictionary with the extracted data
                                            row_dict = {
                                                'State': state_dir,
                                                'Year': year_dir,
                                                'Quarter': quarters,
                                                'District_Name': name,
                                                'Metric_Type': metric_type,
                                                'Transaction_Count': count,
                                                'Transaction_Amount': amount,
                                            }
                                            data_list.append(row_dict)

# Convert the list of dictionaries to a Pandas DataFrame
df3 = pd.DataFrame(data_list)

# Now you have the extracted data in the DataFrame 'df'
print(df3)  # Display the first few rows of the DataFrame


import os
import json
import pandas as pd

# Specify the root directory where your JSON files are located
root_dir = r'C:\Users\ELCOT\Desktop\phone\data\map\user\hover\country\india\state'

# Initialize an empty list to hold extracted data
data_list = []

# Loop over all state folders in the root directory
for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)

    # Check if it's a directory (representing a state)
    if os.path.isdir(state_path):
        
        # Loop over all years in the state directory (assuming years are 2018, 2019, etc.)
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)

            # Check if it's a directory (representing a year)
            if os.path.isdir(year_path):
                
                # Loop over all JSON files in the year directory
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file), 'r') as f:
                            json_data = json.load(f)
                            
                            # Extract data from the JSON as needed
                            if 'data' in json_data:
                                data = json_data['data']
                                
                                # Extract data from 'hoverData' if it exists
                                hover_data = data.get('hoverData')
                                if hover_data:
                                    for district, district_data in hover_data.items():
                                        registered_users = district_data.get('registeredUsers', 0)
                                        app_opens = district_data.get('appOpens', 0)
                                        
                                        # Extract quarter from the JSON file name
                                        quarter = json_file.split('.')[0]  # Assuming the file format is "quarter.json"
                                        
                                        # Create a dictionary with the extracted data
                                        row_dict = {
                                            'State': state_dir,
                                            'Year': year_dir,
                                            'Quarter': quarter,
                                            'District': district,
                                            'Registered_Users': registered_users,
                                            'App_Opens': app_opens,
                                        }
                                        data_list.append(row_dict)

# Convert the list of dictionaries to a Pandas DataFrame
df4 = pd.DataFrame(data_list)

# Now you have the extracted data in the DataFrame 'df'
print(df4)  # Display the first few rows of the DataFrame


import os
import json
import pandas as pd

# Specify the root directory where your JSON files are located
root_dir = r'C:\Users\ELCOT\Desktop\phone\data\top\transaction\country\india\state'

# Initialize an empty list to hold extracted data
data_list = []

# Loop over all state folders in the root directory
for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)

    # Check if it's a directory (representing a state)
    if os.path.isdir(state_path):
        
        # Loop over all years in the state directory (assuming years are 2018, 2019, etc.)
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)

            # Check if it's a directory (representing a year)
            if os.path.isdir(year_path):
                
                # Loop over all JSON files in the year directory
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file), 'r') as f:
                            json_data = json.load(f)
                            
                            # Extract data from the JSON as needed
                            if 'data' in json_data:
                                data = json_data['data']

                                quarter = json_file.split('.')[0]
                                
                                # Extract data from 'districts' if it exists
                                districts = data.get('districts', [])
                                for district_data in districts:
                                    entity_name = district_data.get('entityName', '')
                                    metric = district_data.get('metric', {})
                                    transaction_type = metric.get('type', '')
                                    transaction_count = metric.get('count', 0)
                                    transaction_amount = metric.get('amount', 0)
                                    
                                    # Create a dictionary with the extracted data
                                    row_dict = {
                                        'State': state_dir,
                                        'Year': year_dir,
                                        'Quarter': quarter,
                                        'EntityName': entity_name,
                                        'TransactionType': transaction_type,
                                        'TransactionCount': transaction_count,
                                        'TransactionAmount': transaction_amount
                                    }
                                    data_list.append(row_dict)

# Convert the list of dictionaries to a Pandas DataFrame
df5 = pd.DataFrame(data_list)
# Now you have the extracted data in the DataFrame 'df'
print(df5)  # Display the first few rows of the DataFrame


import os
import json
import pandas as pd

# Specify the root directory where your JSON files are located
root_dir = r'C:\Users\ELCOT\Desktop\phone\data\top\user\country\india\state'

# Initialize an empty list to hold extracted data
data_list = []

# Loop over all state folders in the root directory
for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)

    # Check if it's a directory (representing a state)
    if os.path.isdir(state_path):
        
        # Loop over all years in the state directory (assuming years are 2018, 2019, etc.)
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)

            # Check if it's a directory (representing a year)
            if os.path.isdir(year_path):
                
                # Loop over all JSON files in the year directory
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file), 'r') as f:
                            json_data = json.load(f)
                            
                            # Extract data from the JSON as needed
                            if 'data' in json_data:
                                data = json_data['data']
                                
                                # Extract data from 'districts' if it exists
                                districts = data.get('districts', [])
                                for district_data in districts:
                                    name = district_data.get('name', '')
                                    registered_users = district_data.get('registeredUsers', 0)
                                    
                                    # Extract quarter from the JSON file name
                                    quarter = json_file.split('.')[0]  # Assuming the file format is "quarter.json"
                                    
                                    # Create a dictionary with the extracted data
                                    row_dict = {
                                        'State': state_dir,
                                        'Year': year_dir,
                                        'Quarter': quarter,
                                        'Name': name,
                                        'RegisteredUsers': registered_users,
                                    }
                                    data_list.append(row_dict)

# Convert the list of dictionaries to a Pandas DataFrame
df6 = pd.DataFrame(data_list)

# Now you have the extracted data in the DataFrame 'df'
print(df6)  # Display the first few rows of the DataFrame
#--------------------------------------------------------------------------------------------------------------------------------------------
# Data transformation on file1
# Drop any duplicates
d1 = df1.drop_duplicates()
d2 = df2.drop_duplicates()
d3 = df3.drop_duplicates()
d4 = df4.drop_duplicates()
d5 = df5.drop_duplicates()
d6 = df6.drop_duplicates()

#checking Null values
null_counts = d1.isnull().sum()
print(null_counts)

null_counts = d2.isnull().sum()
print(null_counts)

null_counts = d3.isnull().sum()
print(null_counts)

null_counts = d4.isnull().sum()
print(null_counts)

null_counts = d5.isnull().sum()
print(null_counts)

null_counts = d6.isnull().sum()
print(null_counts)

#converting all dataframes in to csv
d1.to_csv('agg_trans.csv', index=False)
df2.to_csv('agg_user.csv', index=False)
d3.to_csv('map_tran.csv', index=False)
d4.to_csv('map_user.csv', index=False)
d5.to_csv('top_tran.csv', index=False)
d6.to_csv('top_user.csv', index=False)

# Assuming your CSV files are in the same directory as your Python script
Agg_trans = pd.read_csv('agg_trans.csv')
Agg_user = pd.read_csv('agg_user.csv')
Map_tran = pd.read_csv('map_tran.csv')
Map_user = pd.read_csv('map_user.csv')
Top_tran = pd.read_csv('top_tran.csv')
Top_user = pd.read_csv('top_user.csv')
#-------------------------------------------------------------------------------------------------------------------------------------------


# Specify your custom directory path
custom_dir = r'C:\Users\ELCOT\Desktop\phone'

# Create the custom directory if it doesn't exist
if not os.path.exists(custom_dir):
    os.makedirs(custom_dir)

# Save CSV files in the custom directory
Agg_trans.to_csv(os.path.join(custom_dir, 'agg_trans.csv'), index=False)
Agg_user.to_csv(os.path.join(custom_dir, 'agg_user.csv'), index=False)
Map_tran.to_csv(os.path.join(custom_dir, 'map_tran.csv'), index=False)
Map_user.to_csv(os.path.join(custom_dir, 'map_user.csv'), index=False)
Top_tran.to_csv(os.path.join(custom_dir, 'top_tran.csv'), index=False)
Top_user.to_csv(os.path.join(custom_dir, 'top_user.csv'), index=False)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd

# Load your CSV data
agg_trans = pd.read_csv('agg_trans.csv')
agg_user = pd.read_csv('agg_user.csv')
map_tran = pd.read_csv('map_tran.csv')
map_user = pd.read_csv('map_user.csv')
top_tran = pd.read_csv('top_tran.csv')
top_user = pd.read_csv('top_user.csv')

def calculate_totals(df):
    total_transaction = df['Transaction_Count'].sum()
    
    # Check if 'Transaction_Amount' column is available in the DataFrame
    if 'Transaction_Amount' in df.columns:
        if df['Transaction_Amount'].dtype != 'string':
            # Convert the column to string if it's not already
            df['Transaction_Amount'] = df['Transaction_Amount'].astype(str)
            
        try:
            df['Transaction_Amount'] = df['Transaction_Amount'].str.replace(',', '', regex=True).astype(float)
            total_amount = df['Transaction_Amount'].sum()
        except ValueError:
            st.warning("Unable to process 'Transaction_Amount' column as a numeric value. Check your data.")
            total_amount = None
    else:
        total_amount = None

    return total_transaction, total_amount


# Function to calculate and display total transaction count and total transaction amount
def display_totals(df, show_total_amount=True):
    total_transaction, total_amount = calculate_totals(df)
    st.write(f'Total Transaction Count: {total_transaction}')
    if show_total_amount and total_amount is not None:
        st.write(f'Total Transaction Amount: {total_amount:,.2f}')
    elif show_total_amount:
        st.write('Total Transaction Amount: N/A')

# Function to display serial numbers starting from 1 for a DataFrame
def display_serial_numbers(df):
    df.insert(0, 'Serial Number', range(1, len(df) + 1))
    return df

# Set page layout to wide mode
st.set_page_config(layout="wide")

# Create a Streamlit app
st.title("Explore Data")

# Apply custom CSS styles
custom_css = """
<style>
/* Add background color */
body {
    background-color:#e3e8e6;
    color: #333333; /* Text color */
}
/* Increase text size for specific elements */
.stMarkdown, .stTextInput, .stSelectbox, .stRadio, .stTable, .stDataFrame {
    font-size: 25px;
}
/* Style the headers */
h1, h2, h3 {
    color: #337ab7; /* Header text color */
}
/* Style the tables */
table.dataframe {
    background-color: transparent; /* Make the background transparent */
    color: #333333; /* Table text color */
}
th {
    background-color: #337ab7; /* Table header background color */
    color: white; /* Table header text color */
}
/* Style text color and font size for result text */
.stText {
    color: #337ab7;
    font-size: 25px;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar with options
selected_state = st.sidebar.selectbox("Select State", agg_trans['States'].unique())
selected_year = st.sidebar.selectbox("Select Year", agg_trans['Transaction_Year'].unique())
selected_quarter = st.sidebar.selectbox("Select Quarter", agg_trans['Quarters'].unique())
selected_option = st.sidebar.radio("Select Data Option", ["Users", "Transactions"])

# Filter data based on selections
filtered_agg_trans = agg_trans[
    (agg_trans['States'] == selected_state) &
    (agg_trans['Transaction_Year'] == selected_year) &
    (agg_trans['Quarters'] == selected_quarter)
]

filtered_agg_user = agg_user[
    (agg_user['State'] == selected_state) &
    (agg_user['Transaction_Year'] == selected_year) &
    (agg_user['Quarters'] == selected_quarter)
]

filtered_map_tran = map_tran[
    (map_tran['State'] == selected_state) &
    (map_tran['Year'] == selected_year) &
    (map_tran['Quarter'] == selected_quarter)
]

filtered_map_user = map_user[
    (map_user['State'] == selected_state) &
    (map_user['Year'] == selected_year) &
    (map_user['Quarter'] == selected_quarter)
]

filtered_top_tran = top_tran[
    (top_tran['State'] == selected_state) &
    (top_tran['Year'] == selected_year) &
    (top_tran['Quarter'] == selected_quarter)
]

filtered_top_user = top_user[
    (top_user['State'] == selected_state) &
    (top_user['Year'] == selected_year) &
    (top_user['Quarter'] == selected_quarter)
]

# Calculate the total transaction amount for the selected state, year, and quarter
total_transaction_amount = filtered_agg_trans['Transaction_Amount'].sum()

# Display total transaction count and total transaction amount at the top
st.subheader("Total Transaction Summary")
if selected_option == "Users":
    display_totals(filtered_agg_user, show_total_amount=False)
elif selected_option == "Transactions":
    # Check if total_transaction_amount is not None before formatting
    if total_transaction_amount is not None:
        st.write(f'Total Transaction Amount for Transactions: {total_transaction_amount:.2f}')
    else:
        st.write('Total Transaction Amount for Transactions: N/A')
    # Call display_totals with show_total_amount set to False
    display_totals(filtered_agg_trans, show_total_amount=False)

# Display data based on selected option
if selected_option == "Users":
    st.subheader(f"Users in {selected_state} - Q{selected_quarter} {selected_year}")
    filtered_agg_user_with_serial = display_serial_numbers(filtered_agg_user)
    st.table(filtered_agg_user_with_serial)

    filtered_map_user_with_serial = display_serial_numbers(filtered_map_user)
    st.table(filtered_map_user_with_serial)

    filtered_top_user_with_serial = display_serial_numbers(filtered_top_user)
    st.table(filtered_top_user_with_serial)

elif selected_option == "Transactions":
    st.subheader(f"Transactions in {selected_state} - Q{selected_quarter} {selected_year}")
    filtered_agg_trans_with_serial = display_serial_numbers(filtered_agg_trans)
    st.table(filtered_agg_trans_with_serial)

    filtered_map_tran_with_serial = display_serial_numbers(filtered_map_tran)
    st.table(filtered_map_tran_with_serial)

    filtered_top_tran_with_serial = display_serial_numbers(filtered_top_tran)
    st.table(filtered_top_tran_with_serial)

#------------------------------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import plotly.express as px

# Load your CSV data
agg_user = pd.read_csv('agg_user.csv')

# Sidebar navigation
selected_option = st.sidebar.radio("Select Data Option", ["Explore Data", "Data Visualization"])

if selected_option == "Data Visualization":
    st.title("Data Visualization")

    # Visualize data from 'agg_user.csv' (You can modify this section as needed)
    st.subheader("Visualization of agg_user.csv")

    # Example: create a pie chart of user percentages by State using Plotly Express
    fig = px.pie(agg_user, names='State', values='Percentage', title="User Percentages by State")
    st.plotly_chart(fig)

    # Check if 'agg_trans' dataframe exists and is not empty
    if 'agg_trans' in locals() and not agg_trans.empty:
        fig2 = px.bar(agg_trans, x='States', y='Transaction_Amount', title="Total Transaction Amount by State")
        st.plotly_chart(fig2)

        fig4 = px.pie(agg_trans, names='Transaction_Type', title="Transaction Type Distribution")
        st.plotly_chart(fig4)

    # Check if 'map_user' dataframe exists and is not empty
# Check if 'map_user' dataframe exists and is not empty
    if 'map_user' in locals() and not map_user.empty:
        fig5 = px.bar(map_user, x='District', y='Registered_Users', title="Registered Users by District")
        st.plotly_chart(fig5)

    # Check if 'df3' dataframe exists and is not empty
    if 'df3' in locals() and not df3.empty:
        fig6 = px.line(df3, x='Quarter', y='Transaction_Amount', color='State', title="Transaction Amount by Quarter")
        st.plotly_chart(fig6)

    # Check if 'df2' dataframe exists and is not empty
    if 'df2' in locals() and not df2.empty:
        fig7 = px.bar(df2, x='Brand', y='Transaction_Count', title="User Brand Preference")
        st.plotly_chart(fig7)

    # Check if 'df3' dataframe exists and is not empty
    if 'df3' in locals() and not df3.empty:
        top_10_districts = df3.groupby('District_Name')['Transaction_Count'].sum().nlargest(10)
        fig8 = px.bar(top_10_districts, x=top_10_districts.index, y=top_10_districts.values, title="Top 10 Districts by Transactions")
        st.plotly_chart(fig8)

    # Check if 'agg_trans' dataframe exists and is not empty
    if 'agg_trans' in locals() and not agg_trans.empty:
        fig9 = px.histogram(agg_trans, x='Transaction_Amount', title="Transaction Amount Distribution")
        st.plotly_chart(fig9)

    # Check if 'df2' dataframe exists and is not empty
    if 'df2' in locals() and not df2.empty:
        fig10 = px.line(df2, x='Quarters', y='Percentage', color='State', title="User Percentage Change Over Quarters")
        st.plotly_chart(fig10)










    # Visualize other dataframes as needed












   



























































