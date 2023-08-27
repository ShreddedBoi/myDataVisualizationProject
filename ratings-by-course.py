import justpy as jp
import pandas as pd

data = pd.read_csv("reviews.csv", parse_dates=["Timestamp"])
share = data.groupby(['Course Name'])['Rating'].count()

chart_def="""
{
  chart: {
    plotBackgroundColor: null,
    plotBorderWidth: null,
    plotShadow: false,
    type: 'pie'
  },
  title: {
    text: 'Browser market shares in May, 2020',
  },
  tooltip: {
    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
  },
  accessibility: {
    point: {
      valueSuffix: '%'
    }
  },
  plotOptions: {
    pie: {
      allowPointSelect: true,
      cursor: 'pointer',
      dataLabels: {
        enabled: true,
        format: '<b>{point.name}</b>: {point.percentage:.1f} %'
      }
    }
  },
  series: [{}]
}
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Rewiews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis",classes="text-h4 text-center")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Distribution of Ratings by course"

    hc_data = [{"name": v1, "y": v2} for v1, v2 in zip(share.index, share)]
    hc.options.series[0].data = hc_data
    return wp


jp.justpy(app)