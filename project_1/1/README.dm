# OrderBlockIndicator

OrderBlockIndicator - це Python-клас для аналізу цінових графіків, визначення блоків замовлень та їх візуалізації.

## Встановлення

Встановіть необхідні бібліотеки за допомогою команди:

```bash
pip install -r requirements.txt

## Використання

from OrderBlockIndicator import OrderBlockIndicator

symbol = "AAPL"
indicator = OrderBlockIndicator(symbol)
indicator.plot_chart()

## Параметри
symbol (строка): Тікер акції для аналізу.
timeframe (строка): Таймфрейм для отримання даних (за замовчуванням '1d').
range_ (ціле число): Розмір блоку замовлень (за замовчуванням 15).

## Методи
get_price_data() -> pd.DataFrame
Отримати історію цін для заданого тікера, таймфрейму та періоду.

structure_low_index_pointer(low_prices: pd.Series, range_: int) -> int
Знайти індекс мінімальної ціни в заданому діапазоні.

plot_order_blocks() -> None
Логіка для візуалізації блоків замовлень.

plot_similar_lines(x: pd.Index, y: pd.Series, color: str) -> None
Вивести лінії для аналогічних висот чи мінімумів.

plot_chart() -> None
Відобразити графік з блоками замовлень та аналогічними лініями.

## Автор: darieaufg23
