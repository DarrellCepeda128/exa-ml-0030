# Reporte de Análisis de Datos - Pandas

`Cepeda Darrell Machine Learning pandas, NC 0030`

## 1. DataFrame Convertido
```text
        Evento  Asistentes  Duracion_dias
0  Conferencia         500              3
1       Taller         150              1
2    Seminario         300              2
3     Congreso         800              5
4     Simposio         250              2
5         Foro         400              4
```

## 2.1 Primeras Filas (head)
```text
        Evento  Asistentes  Duracion_dias
0  Conferencia         500              3
1       Taller         150              1
```

## 2.2 Últimas Filas (tail)
```text
     Evento  Asistentes  Duracion_dias
4  Simposio         250              2
5      Foro         400              4
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Evento             str
Asistentes       int64
Duracion_dias    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   Evento         6 non-null      str  
 1   Asistentes     6 non-null      int64
 2   Duracion_dias  6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Asistentes'
```text
count      6.000000
mean     400.000000
std      230.217289
min      150.000000
25%      262.500000
50%      350.000000
75%      475.000000
max      800.000000
Name: Asistentes, dtype: float64
```

## 4. Ordenar Ascendente por Asistentes
```text
        Evento  Asistentes  Duracion_dias
1       Taller         150              1
4     Simposio         250              2
2    Seminario         300              2
5         Foro         400              4
0  Conferencia         500              3
3     Congreso         800              5
```

## 5. Ordenar Descendente por Duracion_dias
```text
        Evento  Asistentes  Duracion_dias
3     Congreso         800              5
5         Foro         400              4
0  Conferencia         500              3
2    Seminario         300              2
4     Simposio         250              2
1       Taller         150              1
```

`Cepeda Darrell Machine Learning pandas, NC 0030`