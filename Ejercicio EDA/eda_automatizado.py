import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def automated_eda(df, target_column='price', columns_to_drop=["id", "name", "host_name", "reviews_per_month" , 
                                                                "last_review", "longitude", "latitude"],categorical_to_numerical = [
    {'categorical_col': 'room_type'},
    {'categorical_col': 'neighbourhood_group'},
    {'categorical_col': 'neighbourhood'}
]):
    """
    Automatiza el análisis exploratorio de datos (EDA) de un DataFrame siguiendo el orden y los pasos especificados.

    Args:
        df (pd.DataFrame): DataFrame a analizar.
        target_column (str, optional): Nombre de la columna que representa la variable objetivo. Defaults to 'price'.
        columns_to_drop (list, optional): Lista de columnas a eliminar. Defaults to ["id", "name", "host_name", "reviews_per_month" , 
        "last_review", "longitude", "latitude"].

    Returns:
        None
    """

    # 1. Exploración y Limpieza de Datos
    print("## 1. Exploración y Limpieza de Datos")

    # 1.1 Exploración inicial
    print("### 1.1 Exploración inicial")
    print("Información general del dataframe:")
    df.info()
    print("\n")
    print("Estadísticas descriptivas:")
    print(df.shape)
    print("\n")

    # 1.1.1 Quitar Duplicados
    print("### 1.1.1 Quitar Duplicados")
    df.drop_duplicates(inplace=True)
    print(f"Registros duplicados eliminados: {len(df) - len(df.drop_duplicates())}")

    # 1.1.2 Eliminar información irrelevante
    print("### 1.1.2 Eliminar información irrelevante")
    df.drop(columns=columns_to_drop, axis=1, inplace=True, errors='ignore')
    print(f"Columnas irrelevantes eliminadas: {columns_to_drop}")

    # 1.2 Análisis de variables Univariadas
    print("## 1.2 Análisis de variables Univariadas")

    # 1.2.1 Variables categóricas
    print("### 1.2.1 Variables categóricas")
    categorical_cols = df.select_dtypes(include=['object']).columns
    num_categorical = len(categorical_cols)
    num_rows = (num_categorical + 2) // 3  # Calcular el número de filas para la cuadrícula

    fig, axes = plt.subplots(num_rows, 3, figsize=(15, 5 * num_rows))
    axes = axes.flatten()  # Aplanar la matriz de ejes

    for i, col in enumerate(categorical_cols):
        sns.countplot(x=col, data=df, ax=axes[i])
        axes[i].set_title(f'Distribución de {col}')
        axes[i].tick_params(axis='x', rotation=45)

    # Eliminar los subplots vacíos si los hay
    for i in range(num_categorical, len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()

    # 1.2.2 Variables Numéricas
    print("### 1.2.2 Variables Numéricas")
    numerical_cols = df.select_dtypes(include=['number']).columns.difference([target_column])
    num_numerical = len(numerical_cols)
    num_rows = (num_numerical + 1) // 2 # Calcular el número de filas para la cuadrícula

    fig, axes = plt.subplots(num_rows, 2, figsize=(12, 6 * num_rows))
    axes = axes.flatten()  # Aplanar la matriz de ejes

    for i, col in enumerate(numerical_cols):
        sns.histplot(x=col, data=df, kde=True, ax=axes[i])
        axes[i].set_title(f'Distribución de {col}')

        # Agregar esta condición para evitar el IndexError
        if i + num_numerical < len(axes):
            sns.boxplot(y=col, data=df, ax=axes[i+num_numerical])
            axes[i+num_numerical].set_title(f'Boxplot de {col}')

    # Eliminar los subplots vacíos si los hay
    for i in range(num_numerical*2, len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()

    print("## 1.3 Análisis de variables Multivariadas")

     # 1.3.1 Numérico-numérico
    print("### 1.3.1 Numérico-numérico")
    numerical_cols = df.select_dtypes(include=['number']).columns.difference([target_column])

    num_plots = len(numerical_cols) * (len(numerical_cols) - 1) // 2
    cols = 3
    rows = (num_plots // cols) + (1 if num_plots % cols != 0 else 0)

    fig, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))
    axes = axes.flatten()

    plot_index = 0
    for i in range(len(numerical_cols)):
        for j in range(i + 1, len(numerical_cols)):
            ax = axes[plot_index]
            sns.scatterplot(x=numerical_cols[i], y=numerical_cols[j], data=df, ax=ax)
            ax.set_title(f'{numerical_cols[i]} vs {numerical_cols[j]}')
            plot_index += 1

    for i in range(plot_index, len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()

    # 1.3.2 Categórico-categórico
    print("### 1.3.2 Categórico-categórico")
    categorical_cols = df.select_dtypes(include=['object']).columns

    num_plots = len(categorical_cols) * (len(categorical_cols) - 1) // 2
    cols = 3
    rows = (num_plots // cols) + (1 if num_plots % cols != 0 else 0)

    fig, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))
    axes = axes.flatten()

    plot_index = 0
    for i in range(len(categorical_cols)):
        for j in range(i + 1, len(categorical_cols)):
            ax = axes[plot_index]
            sns.countplot(x=categorical_cols[i], hue=categorical_cols[j], data=df, ax=ax)
            ax.set_title(f'{categorical_cols[i]} vs {categorical_cols[j]}')
            plot_index += 1

    for i in range(plot_index, len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()

    # 1.3.3 Combinaciones de la clase con varias predictoras
    print("### 1.3.3 Combinaciones de la clase con varias predictoras")
    numerical_cols = df.select_dtypes(include=['number']).columns.difference([target_column])

    cols = 3
    rows = len(numerical_cols) // cols + (1 if len(numerical_cols) % cols != 0 else 0)

    fig, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))
    axes = axes.flatten()

    for plot_index, col in enumerate(numerical_cols):
        ax = axes[plot_index]
        sns.boxplot(x='room_type', y=col, data=df, ax=ax)
        ax.set_title(f'{col} por tipo de habitación')

    for i in range(plot_index + 1, len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()

    # 1.3.4 Análisis de correlaciones
    print("### 1.3.4 Análisis de correlaciones")

   # Conversión de variables categóricas a numéricas
    if categorical_to_numerical:
        for conversion in categorical_to_numerical:
            categorical_col = conversion['categorical_col']
            numerical_col = conversion.get('numerical_col', f"{categorical_col}_n")
            df[numerical_col] = pd.factorize(df[categorical_col])[0]

            transformation_rules = {row[categorical_col]: row[numerical_col] for _, row in df[[categorical_col, numerical_col]].drop_duplicates().iterrows()}
            with open(f"{numerical_col}_transformation_rules.json", "w") as f:
                json.dump(transformation_rules, f)
            # No se elimina la columna categórica original

    # Selecciona solo las columnas numéricas (DESPUÉS de la conversión)
    numerical_df = df.select_dtypes(include='number')

    plt.figure(figsize=(10, 8))
    # Calcula la correlación y crea el heatmap solo para las columnas numéricas
    sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm')

    plt.title('Matriz de correlación')
    plt.show()

    # 1.3.5 Categórico-numérico
    print("### 1.3.5 Categórico-numérico")
    categorical_cols = df.select_dtypes(include=['object']).columns  # Selecciona todas las columnas categóricas del DataFrame.

    # Filtrar las columnas categóricas originales
    if categorical_to_numerical:
        original_categorical_cols = [conversion['categorical_col'] for conversion in categorical_to_numerical]  # Obtiene una lista de las columnas categóricas originales que se convirtieron a numéricas.
        categorical_cols = [col for col in categorical_cols if col not in original_categorical_cols]  # Filtra las columnas categóricas para excluir las originales que se convirtieron.

    numerical_cols = df.select_dtypes(include=['number']).columns.difference([target_column])  # Selecciona las columnas numéricas excluyendo la columna objetivo.

    cols = 3  # Número de columnas para los subplots.
    rows = len(categorical_cols) * len(numerical_cols) // cols + (1 if (len(categorical_cols) * len(numerical_cols)) % cols != 0 else 0)  # Calcula el número de filas necesarias para los subplots.

    fig, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))  # Crea la figura y los ejes para los subplots.
    axes = axes.flatten()  # Aplanar la matriz de ejes.

    plot_index = 0
    for cat_col in categorical_cols:
        for num_col in numerical_cols:
            ax = axes[plot_index]
            sns.boxplot(x=cat_col, y=num_col, data=df, ax=ax)  # Crea un boxplot para comparar cada columna categórica con cada columna numérica.
            ax.set_title(f'{num_col} por {cat_col}')  # Establece el título del subplot.
            plot_index += 1

    for i in range(plot_index, len(axes)):
        fig.delaxes(axes[i])  # Elimina los subplots vacíos.

    plt.tight_layout()  # Ajusta los subplots para que no se superpongan.
    plt.show()  # Muestra los gráficos.

    # 2. Feature Engineering
    print("## 2. Feature Engineering")

    # 2.1 Análisis Outliers
    print("### 2.1 Análisis Outliers")
    # ... (código para detectar y manejar outliers)

    # 2.2 Análisis de valores faltantes
    print("### 2.2 Análisis de valores faltantes")
    # ... (código para detectar e imputar valores faltantes)

    # 2.3 Inferencia de nuevas caraterísticas
    print("### 2.3 Inferencia de nuevas caraterísticas")
    # ... (código para crear nuevas variables)

    # 2.4 Feature Scalling
    print("### 2.4 Feature Scalling") 
    # ... (código para escalar variables - StandardScaler o MinMaxScaler)