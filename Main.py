import streamlit as st
import pandas as pd
import io


st.set_page_config( page_title = "Dashboard", page_icon = '📊' )


File = st.file_uploader("Pic Excel")



raw_df = pd.read_excel(File)
df = raw_df.iloc[1:]

# Remove all blanks from Start_time
df['Start_time'] = df['Start_time'].str.strip()

# Replace empty strings with NaN (optional)
df['Start_time'].replace('', pd.NA, inplace=True)

df['Start_time'] = pd.to_datetime(df['Start_time'], format="%d-%m-%Y %I:%M %p")
df = df.sort_values(by='Start_time', ascending=False)
latest_status = df.groupby('id').first()

df = latest_status



df = st.data_editor(df)

st.write(df)


# Function to convert DataFrame to Excel
def convert_df_to_excel(df):
    output = io.BytesIO()  # Create a bytes buffer to hold the Excel file
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')  # Write DataFrame to the buffer
    return output.getvalue()  # Return the bytes value



# Convert DataFrame to Excel
excel = convert_df_to_excel(df)

# Add a download button
st.download_button(
    label='Download Excel',
    data=excel,
    file_name='dataframe.xlsx',
    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
)