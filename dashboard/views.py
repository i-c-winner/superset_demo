from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.offline import plot
import numpy as np
from datetime import datetime, timedelta
import random


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
    """Страница дашбордов с интерактивными графиками Plotly."""
    
    # Кастомная цветовая палитра для соответствия дизайну сайта
    custom_colors = {
        'primary': '#667eea',
        'secondary': '#764ba2', 
        'accent1': '#f093fb',
        'accent2': '#f5576c',
        'accent3': '#4facfe',
        'accent4': '#00f2fe',
        'success': '#96fbc4',
        'warning': '#f9f586'
    }
    
    color_palette = [custom_colors['primary'], custom_colors['accent1'], custom_colors['accent3'], 
                    custom_colors['accent2'], custom_colors['secondary'], custom_colors['accent4']]
    
    # Генерация демонстрационных данных
    
    # 1. Данные для временного ряда (продажи)
    dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')
    sales_data = {
        'date': dates,
        'revenue': np.cumsum(np.random.normal(1000, 300, len(dates))) + 50000,
        'orders': np.random.poisson(25, len(dates)) + np.sin(np.arange(len(dates)) * 2 * np.pi / 365) * 10 + 30
    }
    df_sales = pd.DataFrame(sales_data)
    
    # 2. Данные по категориям товаров
    categories_data = {
        'category': ['Электроника', 'Одежда', 'Книги', 'Спорт', 'Дом и сад', 'Красота'],
        'sales': [45000, 32000, 18000, 25000, 28000, 22000],
        'profit_margin': [15.2, 35.8, 45.1, 28.3, 31.7, 42.5]
    }
    df_categories = pd.DataFrame(categories_data)
    
    # 3. Данные по регионам
    regions_data = {
        'region': ['Москва', 'СПб', 'Новосибирск', 'Екатеринбург', 'Казань'],
        'market_share': [35, 20, 15, 18, 12]
    }
    df_regions = pd.DataFrame(regions_data)
    
    # 4. Данные для scatter plot (бюджет вс результат)
    campaigns_data = {
        'campaign': [f'Кампания {i}' for i in range(1, 21)],
        'budget': np.random.uniform(5000, 50000, 20),
        'conversions': np.random.uniform(50, 500, 20),
        'channel': np.random.choice(['Соцсети', 'Google Ads', 'Email', 'SEO'], 20)
    }
    df_campaigns = pd.DataFrame(campaigns_data)
    
    # 5. Данные для heatmap (посещаемость по часам и дням)
    days = ['Пон', 'Вто', 'Сре', 'Чет', 'Пят', 'Суб', 'Вос']
    hours = list(range(24))
    traffic_matrix = np.random.poisson(10, (len(days), len(hours))) + \
                    np.outer(np.array([8, 9, 10, 11, 12, 6, 5]), 
                            np.sin(np.linspace(0, 2*np.pi, 24)) * 5 + 10)
    
    # Создание графиков Plotly
    
    # 1. Линейный график - динамика продаж
    line_fig = go.Figure()
    line_fig.add_trace(go.Scatter(
        x=df_sales['date'], 
        y=df_sales['revenue'],
        mode='lines',
        name='Выручка',
        line=dict(color='#667eea', width=3),
        hovertemplate='<b>Дата:</b> %{x}<br><b>Выручка:</b> %{y:,.0f} ₽<extra></extra>'
    ))
    
    line_fig.update_layout(
        title='Динамика выручки по времени',
        xaxis_title='Дата',
        yaxis_title='Выручка (₽)',
        font=dict(family='Inter, sans-serif'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    line_chart = plot(line_fig, output_type='div', include_plotlyjs=False)
    
    # 2. Столбчатая диаграмма - продажи по категориям
    bar_fig = go.Figure(data=[
        go.Bar(
            x=df_categories['category'],
            y=df_categories['sales'],
            marker_color=color_palette,
            hovertemplate='<b>Категория:</b> %{x}<br><b>Продажи:</b> %{y:,.0f} ₽<extra></extra>'
        )
    ])
    
    bar_fig.update_layout(
        title='Продажи по категориям товаров',
        xaxis_title='Категории',
        yaxis_title='Продажи (₽)',
        font=dict(family='Inter, sans-serif'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    bar_chart = plot(bar_fig, output_type='div', include_plotlyjs=False)
    
    # 3. Круговая диаграмма - доля рынка по регионам
    pie_fig = go.Figure(data=[
        go.Pie(
            labels=df_regions['region'],
            values=df_regions['market_share'],
            hole=0.4,  # Для создания donut chart
            marker_colors=color_palette[:5],
            hovertemplate='<b>Регион:</b> %{label}<br><b>Доля:</b> %{value}%<extra></extra>'
        )
    ])
    
    pie_fig.update_layout(
        title='Доля рынка по регионам',
        font=dict(family='Inter, sans-serif'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    pie_chart = plot(pie_fig, output_type='div', include_plotlyjs=False)
    
    # 4. Точечная диаграмма - эффективность кампаний
    scatter_fig = px.scatter(
        df_campaigns, 
        x='budget', 
        y='conversions',
        color='channel',
        size='conversions',
        hover_data=['campaign'],
        color_discrete_sequence=color_palette
    )
    
    scatter_fig.update_layout(
        title='Эффективность рекламных кампаний',
        xaxis_title='Бюджет (₽)',
        yaxis_title='Конверсии',
        font=dict(family='Inter, sans-serif'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    scatter_chart = plot(scatter_fig, output_type='div', include_plotlyjs=False)
    
    # 5. Heatmap - посещаемость по часам и дням
    heatmap_fig = go.Figure(data=go.Heatmap(
        z=traffic_matrix,
        x=hours,
        y=days,
        colorscale='Viridis',
        hovertemplate='<b>День:</b> %{y}<br><b>Час:</b> %{x}:00<br><b>Посетители:</b> %{z}<extra></extra>'
    ))
    
    heatmap_fig.update_layout(
        title='Посещаемость сайта по часам и дням недели',
        xaxis_title='Час дня',
        yaxis_title='День недели',
        font=dict(family='Inter, sans-serif'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    heatmap_chart = plot(heatmap_fig, output_type='div', include_plotlyjs=False)
    
    # 6. Treemap - структура прибыли по категориям
    treemap_fig = go.Figure(go.Treemap(
        labels=df_categories['category'],
        values=df_categories['sales'],
        parents=[""] * len(df_categories),
        textinfo="label+value+percent parent",
        hovertemplate='<b>Категория:</b> %{label}<br><b>Продажи:</b> %{value:,.0f} ₽<extra></extra>'
    ))
    
    treemap_fig.update_layout(
        title='Структура продаж по категориям',
        font=dict(family='Inter, sans-serif'),
        height=400
    )
    treemap_chart = plot(treemap_fig, output_type='div', include_plotlyjs=False)
    
    context = {
        'page_title': 'Дашборды',
        'line_chart': line_chart,
        'bar_chart': bar_chart,
        'pie_chart': pie_chart,
        'scatter_chart': scatter_chart,
        'heatmap_chart': heatmap_chart,
        'treemap_chart': treemap_chart,
    }
    
    return render(request, 'dashboard/dashboards.html', context)


def about_view(request):
    """Страница 'О проекте'."""
    context = {
        'page_title': 'О проекте',
    }
    return render(request, 'dashboard/about.html', context)
