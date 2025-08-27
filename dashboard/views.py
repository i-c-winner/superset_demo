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
    """Страница дашбордов с интерактивными графиками Plotly - НОВЫЙ УПРОЩЕННЫЙ МЕТОД."""
    
    # ГЕНЕРАЦИЯ ДЕМО-ДАННЫХ
    
    # График 1: Линейный график - динамика продаж
    dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
    sales_values = [1000 + i*50 + np.random.normal(0, 100) for i in range(30)]
    
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(
        x=dates, 
        y=sales_values, 
        mode='lines+markers', 
        name='Продажи',
        line=dict(color='#667eea', width=3),
        marker=dict(size=6)
    ))
    fig_line.update_layout(
        title='Динамика продаж за январь 2023',
        xaxis_title='Дата',
        yaxis_title='Сумма (руб.)',
        height=400,
        font=dict(family='Inter, sans-serif'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    # График 2: Столбчатая диаграмма - выручка по продуктам
    categories = ['Продукт A', 'Продукт B', 'Продукт C', 'Продукт D', 'Продукт E']
    revenue = [45000, 35000, 61000, 28000, 52000]
    
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(
        x=categories, 
        y=revenue, 
        name='Выручка',
        marker_color=['#667eea', '#f093fb', '#4facfe', '#f5576c', '#764ba2']
    ))
    fig_bar.update_layout(
        title='Выручка по продуктам',
        xaxis_title='Продукт',
        yaxis_title='Руб.',
        height=400,
        font=dict(family='Inter, sans-serif'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    # График 3: Круговая диаграмма - распределение бюджета
    labels = ['Маркетинг', 'Разработка', 'Администрация', 'Продажи']
    values_pie = [35, 25, 20, 20]
    
    fig_pie = go.Figure(data=[go.Pie(
        labels=labels, 
        values=values_pie, 
        hole=.3,
        marker_colors=['#667eea', '#f093fb', '#4facfe', '#f5576c']
    )])
    fig_pie.update_layout(
        title='Распределение бюджета по отделам',
        height=400,
        font=dict(family='Inter, sans-serif')
    )
    
    # ПРЕОБРАЗОВАНИЕ ГРАФИКОВ В HTML-СТРОКИ
    # Ключевой момент: используем fig.to_html() - САМЫЙ ПРОСТОЙ И НАДЕЖНЫЙ СПОСОБ!
    plot_div_line = fig_line.to_html(
        full_html=False, 
        include_plotlyjs=False, 
        div_id='plotly-line-chart'
    )
    plot_div_bar = fig_bar.to_html(
        full_html=False, 
        include_plotlyjs=False, 
        div_id='plotly-bar-chart'
    )
    plot_div_pie = fig_pie.to_html(
        full_html=False, 
        include_plotlyjs=False, 
        div_id='plotly-pie-chart'
    )
    
    # Подготовка контекста с mark_safe для безопасного HTML
    context = {
        'page_title': 'Дашборды',
        'plot_div_line': mark_safe(plot_div_line),
        'plot_div_bar': mark_safe(plot_div_bar),
        'plot_div_pie': mark_safe(plot_div_pie),
    }
    
    return render(request, 'dashboard/dashboards.html', context)


def about_view(request):
    """Страница 'О проекте'."""
    context = {
        'page_title': 'О проекте',
    }
    return render(request, 'dashboard/about.html', context)
