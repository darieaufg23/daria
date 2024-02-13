import numpy as np
import talib

# Input options
candle_range = 15
show_pd = False
show_bearish_bos = False
show_bullish_bos = False
bearish_ob_color = (255, 0, 0, 90)
bullish_ob_color = (0, 255, 0, 90)
bos_candle_color = (255, 255, 0)
bullish_trend_color = (0, 255, 0)
bearish_trend_color = (255, 0, 0)

# Initialize variables
last_down_index = 0
last_down = 0
last_low = 0
last_up_index = 0
last_up = 0
last_up_low = 0
last_up_open = 0
last_high = 0
last_bull_break_low = 0
structure_low_index = 0
structure_low = 1000000
long_boxes = []
short_boxes = []
bos_lines = []

# Calculate the lowest point in the range
def structure_low_index_pointer(length):
    min_value = np.max(high[-length-1:-1])
    min_index = bar_index
    for i in range(length):
        if low[i] < min_value:
            min_value = low[i]
            min_index = bar_index[i]
    return min_index

# Bearish break of structure
if np.cross(low, structure_low):
    if (bar_index - last_up_index) < 1000:
        # Add bear order block
        short_boxes.append((last_up_index, last_high, last_up_low, last_up_index, bearish_ob_color))
        # Add bearish bos line
        if show_bearish_bos:
            bos_lines.append((structure_low_index, structure_low, bar_index, structure_low, (255, 0, 0), 2))
        # Set BosCandle to True
        bos_candle = True
        # Set CandleColourMode to bearish
        candle_colour_mode = 0
        last_short_index = last_up_index

# Bullish break of structure
if short_boxes:
    for i in range(len(short_boxes) - 1, -1, -1):
        box = short_boxes[i]
        top = box[1]
        left = box[0]
        if close > top:
            # Remove the short box
            short_boxes.pop(i)
            # Check conditions for drawing bullish order block
            if (bar_index - last_down_index) < 1000 and bar_index > last_long_index:
                long_boxes.append((last_down_index, last_down, last_low, last_down_index, bullish_ob_color))
                # Add bullish bos line
                if show_bullish_bos:
                    bos_lines.append((left, top, bar_index, top, (0, 255, 0), 1))
                # Set BosCandle to True
                bos_candle = True
                # Set CandleColourMode to bullish
                candle_colour_mode = 1
                # Record last bull bar index to prevent duplication
                last_long_index = bar_index
                last_bull_break_low = low

# Remove bullish order block if close is below
if long_boxes:
    for i in range(len(long_boxes) - 1, -1, -1):
        box = long_boxes[i]
        bottom = box[2]
        if close < bottom:
            long_boxes.pop(i)

# Candle coloring
candle_colour = bullish_trend_color if candle_colour_mode == 1 else bearish_trend_color
candle_colour = bos_candle_color if bos_candle else candle_colour
plot(bar_index, close, color=candle_colour)
