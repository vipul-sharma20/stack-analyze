import plotly
import plotly.graph_objs as go


def plot_data(model_objects):
    x = []
    y = []
    y_post_count = []
    y_u_count = []
    for tag in model_objects:
        x.append(tag.tag)
        total_count = tag.post_count
        u_count = tag.unanswered_count
        y.append((float(u_count)/float(total_count))*100)
        y_post_count.append(total_count)
        y_u_count.append(u_count)

    # percentage unanswered
    trace0 = [go.Bar(x=x, y=y)]

    # total vs unanswered
    trace1 = go.Bar(x=x, y=y_post_count, name='Tagged Posts')
    trace2 = go.Bar(x=x, y=y_u_count, name='Unanswered Posts')

    trace_group = [trace1, trace2]

    layout_percent = go.Layout(title='Percentage Unanswered')
    layout_group = go.Layout(
        barmode='group',
        title='Tagged Posts vs Unanswered Posts'
    )

    fig_percent = go.Figure(data=trace0, layout=layout_percent)
    percentage_plot = plotly.offline.plot(fig_percent, auto_open=False, output_type='div')

    fig_group = go.Figure(data=trace_group, layout=layout_group)
    group_plot = plotly.offline.plot(fig_group, auto_open=False, output_type='div')

    return percentage_plot, group_plot
