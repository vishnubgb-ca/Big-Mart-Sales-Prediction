import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
# from IPython.display import Image
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.io as pio
import plotly.graph_objects as go
import io
from PIL import Image
from datapreprocessing import data_preprocessing

a =[]
def data_visualization():
    dataset = data_preprocessing()
    categ = []
    numer = []
    for col in dataset.columns:
        if dataset[col].dtypes == object:
            categ.append(col)
        else:
            numer.append(col)

    col=list(dataset.columns)
    col.remove("Item_Outlet_Sales")
    print(col)

    for i in col:
        fig = px.box(dataset, y=i)
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor = "plotly_dark")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        # fig.show()
        fig.write_image(f"box_{i}.jpg")
        # a.append(fig)
    for i in col:
        fig = px.histogram(dataset, y=i, marginal="box")
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False)
        # fig.show()
        fig.write_image(f"histogram_{i}.jpg")
        # a.append(fig)

    df = dataset[numer]
    print("DFGHJKLPOIUYTR-------------",df)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark')
    # fig.show()
    fig.write_image("heatmap.jpg")
    
    return dataset


data_visualization()
