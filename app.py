
import pandas as pd
#from PIL import Image
import numpy as np
import streamlit as st



st.title('Training and Placement Cell Updates:')

st.subheader('Progress of IIIT Bhopal')
x=pd.DataFrame({
    'Name': ["Nayan Verma" ,"Aniruddh Singh"],
    'Branch': ["IT","CSE"],
    'Placed Date':["02-09-2020","09-09-2020"],
    'Companys Name': ["Saggezza" ,"GEP"]
})

st.write("Number of Student Placed from Final Year 2020-2021:{}".format(len(x)))
st.write(x)
dateRange = pd.date_range('8/15/2020', '10/28/2020', freq='D')
randomInts = [ 1 if  (i==18 or i==25) else 0 for i in range(len(dateRange))  ]
df = pd.DataFrame({'RandomValues' : randomInts}, index=dateRange)



st.area_chart(df ,width=800, height=400, use_container_width=False)
#st.line_chart(df)

#st.image(image, caption='Think something by Yourself.....',use_column_width=True)

st.write("© All right")