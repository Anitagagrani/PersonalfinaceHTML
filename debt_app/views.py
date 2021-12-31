from django.shortcuts import render
from django.http import HttpResponse 
from debt_app.models import debt_item
from django.db.models import Sum
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.plotting import figure
from math import pi
import pandas as pd
from bokeh.io import output_file, show
from bokeh.palettes import Greys
from bokeh.plotting import figure
from bokeh.transform import cumsum

# Create your views here.
def debt(request):
              
       ##TABLE##
       debt_table = debt_item.objects.all()
       total_debt = debt_item.objects.aggregate(Sum('debt_balance'))
       total_debt = round(total_debt.get('debt_balance__sum'), 2)

       #INTEREST PER MONTH
       debt_table_dict = debt_table.values()

       debt_balance_list = [a_dict['debt_balance'] for a_dict in debt_table_dict]
       debt_interest_list = [a_dict['debt_interest_rate'] for a_dict in debt_table_dict]
       debt_im_list = []

       #for i in debt_balance_list:
       #   debt_im_list[i] = debt_balance_list[i]
       
       

       print(debt_balance_list)
       print(debt_interest_list)

       ##CHART##
       piechart_data = list(debt_item.objects.all().values())
       names_list = [i["debt_name"] for i in piechart_data]
       balance_list = [i["debt_balance"] for i in piechart_data]
       piechart_data_dict = dict(zip(names_list, balance_list))

       data = pd.Series(piechart_data_dict).reset_index(name='value').rename(columns={'index':'category'})
       data['angle'] = data['value']/data['value'].sum() * 2*pi
       data['color'] = Greys[len(piechart_data_dict)]

       p = figure(plot_height=400, plot_width=400, title="", toolbar_location=None,
              tools="hover", tooltips="@category: @value", x_range=(-0.5, 1.0))
       #p.sizing_mode = "scale_both"
       p.min_border = 0

       p.wedge(x=0, y=1, radius=0.4,
       start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
       line_color="black", fill_color='color', legend_field='category', source=data)

       p.axis.axis_label=None
       p.axis.visible=False
       p.grid.grid_line_color = None
       p.legend.location = "right"
       p.legend.background_fill_color = None
       p.outline_line_color = None
       p.border_fill_color = None
       p.background_fill_color = None

       #p.x_range.range_padding = 0.02

       script, div = components(p, CDN)

       return render(request, "debt.html", locals())