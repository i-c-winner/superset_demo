from django.shortcuts import render
from django.http import HttpResponse
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta


def dashboard_home(request):
    """Главная страница dashboard с продающим контентом."""
    context = {
        'page_title': 'Главная страница',
        'features': [
            {
                'title': 'Интуитивный конструктор',
                'description': 'Создавайте впечатляющие дашборды без единой строчки кода.',
                'icon': 'bi-puzzle'
            },
            {
                'title': 'Поддержка множества БД',
                'description': 'Подключайтесь к любым источникам данных: PostgreSQL, MySQL, MongoDB и другим.',
                'icon': 'bi-hdd-stack'
            },
            {
                'title': 'Богатая библиотека визуализаций',
                'description': 'Более 50 типов графиков и диаграмм: от простых столбцов до сложных геокарт.',
                'icon': 'bi-bar-chart-line'
            },
            {
                'title': 'Enterprise-безопасность',
                'description': 'Продвинутая система разграничения доступа и аудит действий.',
                'icon': 'bi-shield-check'
            }
    ]
    }
    return render(request, 'dashboard/index.html', context)


def dashboards_view(request):
    """Страница дашбордов с 8 профессиональными финансовыми графиками в консервативном стиле."""
    
    # ЕДИНАЯ СТРОГАЯ ЦВЕТОВАЯ СХЕМА
    color_primary = '#1f4b99'  # Темно-синий (основной)
    color_secondary = '#2ca02c' # Темно-зеленый
    color_tertiary = '#8b0000'  # Бордовый
    color_grey = '#404040'      # Темно-серый для текста
    plot_bgcolor = 'white'      # Фон графиков
    grid_color = '#e6e6e6'      # Цвет сетки

    # ЕДИНЫЙ ШАБЛОН ДЛЯ НАСТРОЙКИ ЛАЙАУТА
    layout_template = {
        'font': {'family': 'Roboto, Arial, sans-serif', 'color': color_grey, 'size': 12},
        'title': {'x': 0.5, 'xanchor': 'center', 'font': {'size': 16, 'color': color_grey}},
        'plot_bgcolor': plot_bgcolor,
        'paper_bgcolor': 'rgba(0,0,0,0)', # Прозрачный фон для легкой интеграции в сайт
        'xaxis': {
            'showgrid': True,
            'gridcolor': grid_color,
            'gridwidth': 1,
            'zeroline': False,
            'showline': True,
            'linecolor': color_grey,
            'linewidth': 1,
            'tickfont': {'size': 11}
        },
        'yaxis': {
            'showgrid': True,
            'gridcolor': grid_color,
            'gridwidth': 1,
            'zeroline': False,
            'showline': True,
            'linecolor': color_grey,
            'linewidth': 1,
            'tickfont': {'size': 11},
            'tickprefix': '₽', # Добавляем символ рубля для финансовых графиков
        },
        'legend': {
            'orientation': 'h',
            'yanchor': 'bottom',
            'y': 1.02,
            'xanchor': 'right',
            'x': 1
        },
        'hoverlabel': {
            'bgcolor': 'white',
            'font_size': 11,
            'font_family': 'Roboto, Arial, sans-serif'
        },
        'margin': {'l': 50, 'r': 20, 't': 60, 'b': 50},
        'height': 400,
    }

    # 1. ГРАФИК 1: Динамика ключевых показателей (Линейный)
    dates = pd.date_range(start='2024-01-01', periods=6, freq='ME')
    revenue = [45.2, 48.5, 52.1, 49.8, 55.3, 58.9] # млн руб.
    profit = [12.1, 13.0, 14.5, 13.2, 15.8, 17.2]  # млн руб.

    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(x=dates, y=revenue, mode='lines+markers', name='Выручка', line=dict(color=color_primary, width=3)))
    fig_trend.add_trace(go.Scatter(x=dates, y=profit, mode='lines+markers', name='Чистая прибыль', line=dict(color=color_secondary, width=3)))
    fig_trend.update_layout(layout_template)
    fig_trend.update_layout(title='Динамика выручки и прибыли (млн руб.)')

    # 2. ГРАФИК 2: Структура расходов (Круговая)
    expenses_labels = ['ФОТ', 'Закупка сырья', 'Маркетинг', 'Налоги', 'Аренда', 'Прочие']
    expenses_values = [45, 25, 10, 8, 7, 5]

    fig_expenses = go.Figure(data=[go.Pie(
        labels=expenses_labels,
        values=expenses_values,
        hole=.4,
        marker=dict(colors=[color_primary, color_secondary, color_tertiary, '#7f7f7f', '#17becf', '#bcbd22']),
        textinfo='label+percent',
        textfont_size=13
    )])
    fig_expenses.update_layout(layout_template)
    fig_expenses.update_layout(title='Структура операционных расходов (%)', showlegend=False)

    # 3. ГРАФИК 3: Плановые vs Фактические показатели (Столбчатый с группойми)
    months = ['Янв', 'Фев', 'Мар', 'Апр']
    planned = [22, 25, 23, 28]
    actual = [20, 26, 25, 30]

    fig_plan_vs_fact = go.Figure()
    fig_plan_vs_fact.add_trace(go.Bar(name='План', x=months, y=planned, marker_color=color_primary, opacity=0.9))
    fig_plan_vs_fact.add_trace(go.Bar(name='Факт', x=months, y=actual, marker_color=color_secondary, opacity=0.9))
    fig_plan_vs_fact.update_layout(layout_template)
    fig_plan_vs_fact.update_layout(
        title='Выполнение плана по месяцам (млн руб.)',
        barmode='group',
        yaxis={'tickprefix': '₽'}
    )

    # 4. ГРАФИК 4: Воронка продаж
    funnel_labels = ['Лиды', 'Квалифицированные', 'Предложение', 'Переговоры', 'Сделка']
    funnel_values = [1000, 600, 400, 250, 150]

    fig_funnel = go.Figure(go.Funnel(
        y=funnel_labels,
        x=funnel_values,
        textinfo = "value+percent initial",
        marker={"color": [color_primary, '#3d72a4', '#5a93cb', '#87bcde', '#b4d4e7']},
        textfont={"size": 12}
    ))
    fig_funnel.update_layout(layout_template)
    fig_funnel.update_layout(title='Воронка продаж')

    # 5. ГРАФИК 5: Динамика просроченной задолженности (Область)
    debt_dates = pd.date_range(start='2024-01-01', periods=5, freq='ME')
    debt_1_30 = [1.2, 1.5, 1.0, 1.8, 1.3]
    debt_31_60 = [0.5, 0.7, 0.4, 0.9, 0.6]
    debt_60_90 = [0.2, 0.3, 0.1, 0.4, 0.2]

    fig_debt = go.Figure()
    fig_debt.add_trace(go.Scatter(x=debt_dates, y=debt_1_30, mode='none', name='1-30 дней', stackgroup='one', fillcolor='#ff9999'))
    fig_debt.add_trace(go.Scatter(x=debt_dates, y=debt_31_60, mode='none', name='31-60 дней', stackgroup='one', fillcolor='#ff6666'))
    fig_debt.add_trace(go.Scatter(x=debt_dates, y=debt_60_90, mode='none', name='60-90 дней', stackgroup='one', fillcolor='#ff0000'))
    fig_debt.update_layout(layout_template)
    fig_debt.update_layout(title='Динамика просроченной дебиторской задолженности (млн руб.)', hovermode='x unified')

    # 6. ГРАФИК 6: Соотношение затрат и доходов по направлениям (Scatter)
    categories = ['Направление A', 'Направление B', 'Направление C', 'Направление D']
    income = [50, 80, 30, 65]
    costs = [20, 50, 25, 30]
    profitability = [((i - c) / i) * 100 for i, c in zip(income, costs)]  # Расчет рентабельности в %

    fig_scatter = go.Figure()
    fig_scatter.add_trace(go.Scatter(
        x=income,
        y=costs,
        mode='markers+text',
        marker=dict(size=profitability, sizemode='area', sizeref=2.*max(profitability)/(40.**2), sizemin=4, color=profitability, colorscale='Blues', showscale=True),
        text=categories,
        textposition='middle right',
        hovertemplate='<b>%{text}</b><br>Доход: ₽%{x} млн<br>Затраты: ₽%{y} млн<br>Рентабельность: %{marker.size:.1f}%<extra></extra>'
    ))
    fig_scatter.update_layout(layout_template)
    fig_scatter.update_layout(
        title='Соотношение доходов и затрат по направлениям',
        xaxis_title='Доходы (млн руб.)',
        yaxis_title='Затраты (млн руб.)',
        yaxis={'tickprefix': '₽'},
        xaxis={'tickprefix': '₽'}
    )

    # 7. ГРАФИК 7: Отклонение от плана (Waterfall)
    waterfall_labels = ['Нач. остаток', 'Продажи', 'Возвраты', 'Закупки', 'Корректировки', 'Кон. остаток']
    waterfall_values = [100, 50, -15, -40, 5, None]  # None для конечного остатка

    fig_waterfall = go.Figure(go.Waterfall(
        name="Склад",
        orientation="v",
        measure=["absolute", "relative", "relative", "relative", "relative", "total"],
        x=waterfall_labels,
        textposition="outside",
        text=[f"+{v}" if v > 0 else str(v) for v in waterfall_values if v is not None],
        y=waterfall_values,
        connector={"line":{"color":"rgb(63, 63, 63)"}},
        increasing={"marker":{"color":color_secondary}},
        decreasing={"marker":{"color":color_tertiary}},
        totals={"marker":{"color":color_primary}}
    ))
    fig_waterfall.update_layout(layout_template)
    fig_waterfall.update_layout(title='Движение товарных запасов (тыс. ед.)')

    # 8. ГРАФИК 8: Эффективность каналов продаж (Horizontal Bar)
    channels = ['Партнеры', 'Сайт', 'Кол-центр', 'Соц. сети', 'Прямые продажи']
    conversion = [22, 15, 18, 10, 25]  # %

    fig_hbar = go.Figure()
    fig_hbar.add_trace(go.Bar(
        y=channels,
        x=conversion,
        orientation='h',
        marker_color=color_primary,
        text=conversion,
        texttemplate='%{text}%',
        textposition='auto'
    ))
    fig_hbar.update_layout(layout_template)
    fig_hbar.update_layout(
        title='Конверсия по каналам продаж',
        xaxis_title='Конверсия, %',
        yaxis={'autorange': 'reversed'}  # Чтобы список шел сверху вниз
    )

    # Преобразование всех графиков в HTML
    context = {
        'plot_div_trend': mark_safe(fig_trend.to_html(full_html=False, include_plotlyjs=False, div_id='trend-chart')),
        'plot_div_expenses': mark_safe(fig_expenses.to_html(full_html=False, include_plotlyjs=False, div_id='expenses-chart')),
        'plot_div_plan_fact': mark_safe(fig_plan_vs_fact.to_html(full_html=False, include_plotlyjs=False, div_id='plan-fact-chart')),
        'plot_div_funnel': mark_safe(fig_funnel.to_html(full_html=False, include_plotlyjs=False, div_id='funnel-chart')),
        'plot_div_debt': mark_safe(fig_debt.to_html(full_html=False, include_plotlyjs=False, div_id='debt-chart')),
        'plot_div_scatter': mark_safe(fig_scatter.to_html(full_html=False, include_plotlyjs=False, div_id='scatter-chart')),
        'plot_div_waterfall': mark_safe(fig_waterfall.to_html(full_html=False, include_plotlyjs=False, div_id='waterfall-chart')),
        'plot_div_hbar': mark_safe(fig_hbar.to_html(full_html=False, include_plotlyjs=False, div_id='hbar-chart')),
    }

    return render(request, 'dashboard/dashboards.html', context)


def about_view(request):
    """Страница 'О проекте'."""
    context = {
        'page_title': 'О проекте',
    }
    return render(request, 'dashboard/about.html', context)
