import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff


_color_palette = [
            '#005AD6',
            '#62A4FF',
            '#757575',
            '#02BE6D',
            '#FF6F69',
            '#00132E']

_font_family = 'Helvetica'


def plot_series(
                series,
                title='Titulo',
                suptitle='Subtitulo',
                ylabel='ylabel',
                xlabel='xlabel',
                imgname='fintualistic',
                save=True,
                marker=False,
                title_size=35,
                label_size=22,
                showlegend=True,
                legend_size=30,
                tick_size=20
                ):
    """
    Plots a pandas Serie or Dataframe as a line chart,
    columns are going to be displayed as legend.
    :param series: dataframe
        pandas dataframe or series with timeseries,
        each column represents a serie
    :param title: str, default: 'Titulo'
        title of the chart
    :param suptitle: str, default: 'Subtitulo'
        suptitle of the chat
    :param ylabel: str, default: 'ylabel'
        y label of the chat
    :param xlabel: str, default: 'xlabel'
        x label of the chat
    :param imgname: str, default: 'fintualistic'
        name of the html file
    :param save: boolean, default: True
        True if you want to save an html file
    :param marker: boolean, default: False
        True if you want circle markers on the line
    :param title_size: int, default: 35
        Title font size
    :param lavel_size: int, default: 22
        Axis labels font size
    :param showlegend: boolean, default: True
        True if you want to show the legend
    :param legend_size: int, default: 30
        Legend font size
    :param tick_size: int, default: 30
        Ticks font size
    """

    if isinstance(series, pd.Series):
        is_series = True
        data = series.to_frame(series.name)
    else:
        is_series = False
        data = series.copy()

    n = data.shape[1]
    x = data.index

    if marker:
        mode = 'lines+markers'
    else:
        mode = 'lines'

    fig = go.Figure()

    for i in range(n):
        serie = data.iloc[:, i]
        name = serie.name
        color = _color_palette[i % len(_color_palette)]
        fig.add_trace(
                    go.Scatter(
                                x=x,
                                y=serie,
                                name=name,
                                mode=mode,
                                line=dict(
                                    color=color,
                                    width=3)))

    header = '<b>{}</b> <br><sup>{}</sup>'.format(title, suptitle)
    fig.update_layout(
                    title={'text': header, 'font_size': title_size},
                    xaxis_title={'text': xlabel, 'font_size': label_size},
                    yaxis_title={'text': ylabel, 'font_size': label_size},
                    font_family=_font_family,
                    plot_bgcolor='#F3F6FA',
                    paper_bgcolor='#F3F6FA',
                    legend={'font': {'size': legend_size}},
                    margin=dict(l=100, r=100, t=120, b=100),
                    title_yanchor='top'
                   )

    fig.update_xaxes(
                    zeroline=False,
                    gridcolor='lightgray',
                    tickfont={"size": tick_size})
    fig.update_yaxes(
                    zeroline=False,
                    gridcolor='lightgray',
                    tickfont={"size": tick_size})
    if is_series or showlegend is False:
        fig.update_layout(showlegend=False)

    if save:
        fig.write_html(imgname + '.html')

    fig.show()


def plot_bar(
            data,
            title='Titulo',
            suptitle='Subtitulo',
            ylabel='ylabel',
            xlabel='xlabel',
            imgname='fintualistic',
            save=True,
            title_size=35,
            label_size=22,
            legend_size=30,
            tick_size=20,
            stacked=False,
            bar_labels=True
            ):
    """
    Plots a pandas Serie or Dataframe as a bar chart,
    columns are going to be displayed as legend.
    :param data: pandas dataframe or series
        dataframe or series with the data to plot
    :param title: str, default: 'Titulo'
        title of the chart
    :param suptitle: str, default: 'Subtitulo'
        suptitle of the chat
    :param ylabel: str, default: 'ylabel'
        y label of the chat
    :param xlabel: str, default: 'xlabel'
        x label of the chat
    :param imgname: str, default: 'fintualistic'
        name of the html file
    :param save: boolean, default: True
        True if you want to save an html file
    :param title_size: int, default: 35
        Title font size
    :param lavel_size: int, default: 22
        Axis labels font size
    :param legend_size: int, default: 30
        Legend font size
    :param tick_size: int, default: 30
        Ticks font size
    :param stacked: boolean, default: False
        True for stacked bars, False for group
    :param bar_labels: boolean, default: False
        True for showing bar labels, False for group
    """

    if stacked:
        barmode = 'relative'
    else:
        barmode = 'group'

    if bar_labels:
        bar_label_text = '.3s'
    else:
        bar_label_text = False

    if isinstance(data, pd.Series):
        is_series = True
        data = data.to_frame(data.name)
    else:
        is_series = False

    fig = px.bar(
                data,
                barmode=barmode,
                color_discrete_sequence=_color_palette,
                text_auto=bar_label_text
                )
    header = '<b>{}</b> <br><sup>{}</sup>'.format(title, suptitle)
    fig.update_layout(
                    title={
                            'text': header,
                            'font_size': title_size
                            },
                    xaxis_title={'text': xlabel, 'font_size': label_size},
                    yaxis_title={'text': ylabel, 'font_size': label_size},
                    font_family=_font_family,
                    plot_bgcolor='#F3F6FA',
                    paper_bgcolor='#F3F6FA',
                    legend={'font': {'size': legend_size}, 'title': None},
                    margin=dict(l=100, r=100, t=120, b=100),
                    title_yanchor='top'
                   )
    if is_series:
        fig.update_layout(showlegend=False)

    fig.update_traces(textfont_size=label_size)

    fig.update_xaxes(
                    zeroline=False,
                    gridcolor='lightgray',
                    tickfont={"size": tick_size})
    fig.update_yaxes(
                    zeroline=False,
                    gridcolor='lightgray',
                    tickfont={"size": tick_size}
                    )
    if save:
        fig.write_html(imgname + '.html')
    fig.show()


def plot_combo_series(
                serie_1,
                serie_2,
                title='Titulo',
                suptitle='Subtitulo',
                ylabel1=None,
                ylabel2=None,
                xlabel='xlabel',
                imgname='fintualistic',
                save=True,
                marker=False,
                title_size=35,
                label_size=22,
                tick_size=20
                ):
    """
    Plots two pandas Series as line charts, both in differente axis.
    :param serie_1: pandas serie
        serie with the first timeseries to plot
    :param serie_2: pandas serie
        serie with the second timeseries to plot
    :param title: str, default: 'Titulo'
        title of the chart
    :param suptitle: str, default: 'Subtitulo'
        suptitle of the chat
    :param ylabel1: str, default: None
        y label of the first timeserie,
        if None, the name of the pandas serie is used
    :param ylabel2: str, default: None
        y label of the second timeserie,
        if None, the name of the pandas serie is used
    :param xlabel: str, default: 'xlabel'
        x label of the chat
    :param imgname: str, default: 'fintualistic'
        name of the html file
    :param save: boolean, default: True
        True if you want to save an html file
    :param marker: boolean, default: False
        True if you want circle markers on the line
    :param title_size: int, default: 35
        Title font size
    :param label_size: int, default: 22
        Axis labels font size
    :param tick_size: int, default: 30
        Ticks font size
    """

    if marker:
        mode = 'lines+markers'
    else:
        mode = 'lines'

    if ylabel1 is None:
        ylabel1 = serie_1.name

    if ylabel2 is None:
        ylabel2 = serie_2.name

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
                go.Scatter(
                    x=serie_1.index,
                    y=serie_1,
                    mode=mode,
                    line=dict(
                            color=_color_palette[0],
                            width=3)),
                secondary_y=False
                )

    fig.add_trace(
                go.Scatter(
                    x=serie_1.index,
                    y=serie_2,
                    mode=mode,
                    line=dict(
                            color=_color_palette[1],
                            width=3)),
                secondary_y=True
                )

    header = '<b>{}</b> <br><sup>{}</sup>'.format(title, suptitle)

    fig.update_layout(
                    title={'text': header, 'font_size': title_size},
                    xaxis_title={'text': xlabel, 'font_size': label_size},
                    yaxis=dict(
                                title=ylabel1,
                                titlefont=dict(
                                        color=_color_palette[0],
                                        size=tick_size),
                                tickfont=dict(color=_color_palette[0])),
                    yaxis2=dict(
                                title=ylabel2,
                                titlefont=dict(
                                        color=_color_palette[1],
                                        size=tick_size),
                                tickfont=dict(color=_color_palette[1])),
                    font_family=_font_family,
                    plot_bgcolor='#F3F6FA',
                    paper_bgcolor='#F3F6FA',
                    showlegend=False,
                    margin=dict(l=100, r=100, t=120, b=100),
                    title_yanchor='top')

    fig.update_xaxes(
                    zeroline=False,
                    gridcolor='lightgray',
                    tickfont={"size": tick_size})
    fig.update_yaxes(
                    zeroline=False,
                    gridcolor='lightgray',
                    zerolinecolor='#F3F6FA',
                    tickfont={"size": tick_size})

    fig['layout']['yaxis2']['showgrid'] = False

    if save:
        fig.write_html(imgname + '.html')

    fig.show()


def plot_pie(
                serie,
                title='Titulo',
                suptitle='Subtitulo',
                imgname='fintualistic',
                save=True,
                title_size=35,
                label_size=22,
                ):
    """
    Plots a pandas Serie as a pie chart with labels.
    :param series: dataframe
        dataframe with series, each column represents a serie
    :param title: str, default: 'Titulo'
        title of the chart
    :param suptitle: str, default: 'Subtitulo'
        suptitle of the chat
    :param imgname: str, default: 'fintualistic'
        name of the html file
    :param save: boolean, default: True
        True if you want to save an html file
    :param title_size: int, default: 35
        Title font size
    :param label_size: int, default: 22
        Axis labels font size
    """

    fig = go.Figure(
                    data=[
                            go.Pie(
                                    labels=serie.index,
                                    values=serie.round(2),
                                    hole=.5)])
    fig.update_traces(
                    hoverinfo='label+percent',
                    textfont_size=label_size,
                    marker=dict(
                            colors=_color_palette,
                            line=dict(
                                    color='#000000',
                                    width=0.25)),
                    textposition='outside',
                    textinfo='value+label')

    header = '<b>{}</b> <br><sup>{}</sup>'.format(title, suptitle)

    fig.update_layout(
                    title={'text': header, 'font_size': title_size},
                    font_family=_font_family,
                    plot_bgcolor='#F3F6FA',
                    paper_bgcolor='#F3F6FA',
                    showlegend=False,
                    margin=dict(l=100, r=100, t=120, b=100),
                    title_yanchor='top')

    if save:
        fig.write_html(imgname + '.html')

    fig.show()


def plot_scatter(
                serie_1,
                serie_2,
                regression_line=True,
                title='Titulo',
                suptitle='Subtitulo',
                ylabel=None,
                xlabel=None,
                imgname='fintualistic',
                save=True,
                title_size=35,
                label_size=22,
                tick_size=20
                ):
    """
    Plots two pandas Series in a scatter plot, regression line is optional.
    :param serie_1: pandas serie
        serie with the first series to plot, axis x
    :param serie_2: pandas serie
        serie with the second series to plot, axis y
    :param regression_line: bool, default: True
        True for plotting the regression line
    :param title: str, default: 'Titulo'
        title of the chart
    :param suptitle: str, default: 'Subtitulo'
        suptitle of the chat
    :param ylabel: str, default: None
        y label of the first variable,
        if None, the name of the pandas serie is used
    :param xlabel: str, default: 'xlabel'
        x label of the se variable,
        if None, the name of the pandas serie is used
    :param imgname: str, default: 'fintualistic'
        name of the html file
    :param save: boolean, default: True
        True if you want to save an html file
    :param title_size: int, default: 35
        Title font size
    :param label_size: int, default: 22
        Axis labels font size
    :param tick_size: int, default: 30
        Ticks font size
    """

    if xlabel is None:
        xlabel = serie_1.name

    if ylabel is None:
        ylabel = serie_2.name

    if regression_line:
        regression_line = 'ols'
    else:
        regression_line = None

    df = pd.DataFrame([serie_1, serie_2])
    df = df.T

    fig = px.scatter(
                    df,
                    x=serie_1.name,
                    y=serie_2.name,
                    trendline=regression_line,
                    trendline_color_override=_color_palette[0],
                    opacity=0.3)

    header = '<b>{}</b> <br><sup>{}</sup>'.format(title, suptitle)

    fig.update_layout(
                    title={'text': header, 'font_size': title_size},
                    xaxis=dict(
                                title=xlabel,
                                titlefont=dict(size=label_size)),
                    yaxis=dict(
                                title=ylabel,
                                titlefont=dict(size=label_size)),
                    font_family=_font_family,
                    plot_bgcolor='#F3F6FA',
                    paper_bgcolor='#F3F6FA',
                    showlegend=False,
                    margin=dict(l=100, r=100, t=120, b=100),
                    title_yanchor='top')
    fig.update_traces(marker=dict(color=_color_palette[0]))

    fig.update_xaxes(
                    showline=False,
                    gridcolor='lightgray',
                    zeroline=False,
                    tickfont={"size": tick_size})
    fig.update_yaxes(
                    showline=False,
                    gridcolor='lightgray',
                    zeroline=False,
                    tickfont={"size": tick_size})

    if save:
        fig.write_html(imgname + '.html')

    fig.show()


def plot_dist(
                series,
                show_curve=True,
                show_bars=True,
                title='Titulo',
                suptitle='Subtitulo',
                ylabel=None,
                xlabel=None,
                imgname='fintualistic',
                save=True,
                title_size=35,
                label_size=22,
                tick_size=20,
                legend_size=30
                ):
    """
    Plots a pandas Dataframe or Serie as a distribution plot.
    :param series: pandas dataframe o serie
        dataframe with the distributions,
        every column is a distribution, also a serie can be passed
    :param show_curve: bool, default: True
        True for plotting the histogram line
    :param show_bars: bool, default: True
        True for plotting the histogram bars
    :param title: str, default: 'Titulo'
        title of the chart
    :param suptitle: str, default: 'Subtitulo'
        suptitle of the chat
    :param ylabel: str, default: None
        y label of the chart
    :param xlabel: str, default: 'xlabel'
        x label of the chart
    :param imgname: str, default: 'fintualistic'
        name of the html file
    :param save: boolean, default: True
        True if you want to save an html file
    :param title_size: int, default: 35
        Title font size
    :param label_size: int, default: 22
        Axis labels font size
    :param tick_size: int, default: 30
        Ticks font size
    :param legend_size: int, default: 30
        Legend font size
    """

    if isinstance(series, pd.Series):
        is_series = True
        data = series.to_frame(series.name)
    else:
        is_series = False
        data = series.copy()

    fig = ff.create_distplot(
                [data[c] for c in data.columns],
                data.columns,
                show_rug=False,
                colors=_color_palette,
                bin_size=data.std()/8,
                show_hist=show_bars,
                show_curve=show_curve)

    header = '<b>{}</b> <br><sup>{}</sup>'.format(title, suptitle)

    fig.update_layout(
                    title={'text': header, 'font_size': title_size},
                    xaxis=dict(
                                title=xlabel,
                                titlefont=dict(size=label_size)),
                    yaxis=dict(
                                title=ylabel,
                                titlefont=dict(size=label_size)),
                    font_family=_font_family,
                    plot_bgcolor='#F3F6FA',
                    paper_bgcolor='#F3F6FA',
                    showlegend=True,
                    legend={'font': {'size': legend_size}},
                    margin=dict(l=100, r=100, t=120, b=100),
                    title_yanchor='top')

    fig.update_xaxes(
                    showline=False,
                    gridcolor='lightgray',
                    zeroline=False,
                    tickfont={"size": tick_size})
    fig.update_yaxes(
                    showline=False,
                    gridcolor='lightgray',
                    zeroline=False,
                    tickfont={"size": tick_size})
    if is_series:
        fig.update_layout(showlegend=False)

    if save:
        fig.write_html(imgname + '.html')

    fig.show()


def plot_area(
                series,
                title='Titulo',
                suptitle='Subtitulo',
                ylabel='ylabel',
                xlabel='xlabel',
                imgname='fintualistic',
                save=True,
                title_size=35,
                label_size=22,
                legend_size=30,
                tick_size=20
                ):
    """
    Plots a pandas Serie or Dataframe as an area chart. Stacking is optional.
    :param series: dataframe
        pandas dataframe or series with timeseries,
        each column represents a serie
    :param title: str, default: 'Titulo'
        title of the chart
    :param suptitle: str, default: 'Subtitulo'
        suptitle of the chat
    :param ylabel: str, default: 'ylabel'
        y label of the chat
    :param xlabel: str, default: 'xlabel'
        x label of the chat
    :param imgname: str, default: 'fintualistic'
        name of the html file
    :param save: boolean, default: True
        True if you want to save an html file
    :param title_size: int, default: 35
        Title font size
    :param lavel_size: int, default: 22
        Axis labels font size
    :param legend_size: int, default: 30
        Legend font size
    :param tick_size: int, default: 30
        Ticks font size
    """

    if isinstance(series, pd.Series):
        is_series = True
        data = series.to_frame(series.name)
    else:
        is_series = False
        data = series.copy()

    n = data.shape[1]
    x = data.index

    fig = go.Figure()

    for i in range(n):
        serie = data.iloc[:, i]
        name = serie.name
        color = _color_palette[i % len(_color_palette)]
        fig.add_trace(
                    go.Scatter(
                        x=x,
                        y=serie,
                        name=name,
                        stackgroup='one',
                        line=dict(
                            color=color,
                            width=0.1)
                            ))

    header = '<b>{}</b> <br><sup>{}</sup>'.format(title, suptitle)
    fig.update_layout(
                    title={'text': header, 'font_size': title_size},
                    xaxis_title={'text': xlabel, 'font_size': label_size},
                    yaxis_title={'text': ylabel, 'font_size': label_size},
                    font_family=_font_family,
                    plot_bgcolor='#F3F6FA',
                    paper_bgcolor='#F3F6FA',
                    legend={'font': {'size': legend_size}},
                    margin=dict(l=100, r=100, t=120, b=100),
                    title_yanchor='top'
                   )

    fig.update_xaxes(
                    showline=False,
                    gridcolor='lightgray',
                    zeroline=False,
                    tickfont={"size": tick_size})
    fig.update_yaxes(
                    showline=False,
                    gridcolor='lightgray',
                    zeroline=False,
                    tickfont={"size": tick_size})
    if save:
        fig.write_html(imgname + '.html')
    fig.show()
