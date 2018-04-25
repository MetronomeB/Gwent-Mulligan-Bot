# Gwent-Mulligan-Bot

#### A. About

The bot is a simple AutoHotkey script that collects screenshots of mulligan samples.

The python scripts uses the dhash algorithm to identify repeating mulliganed cards.

#### B. Requirements

Windows 10 64-bit w/1920x1080 resolution  
Python 3.6+  
AutoHotkey 1.1.28+  

#### C. Python dependencies

Pillow  
dhash  

#### D. Gwent settings
Resolution = 1920x1080  
Fullscreen = On  
Graphics = Low  
Vsync = Enabled  
Antialising = Full  
Premium cards = Off  
Tooltips = Off  
GOG Galaxy client = Off  

#### E. Tutorial 

1. Download the package and ensure compliance with all of the above.
2. Create a deck with any Bronze specials and Calveit as leader, then exit Gwent.
3. Run 'gwent_mulligan_bot.ahk', and input the number of batches of 50 mulligans to sample.
4. Let the bot run to completion uninterrupted. Any key press - even moving the mouse cursor a single pixel - might cause the bot to de-sync.
5. Move all screenshots taken by the bot from Windows' built-in 'Pictures\Screenshots' folder to the 'data' folder.
6. Run 'prepare_screenshot_pairs.py'. This script identifies faulty screenshot pairs, moves them to the 'faulty_screenshot_pairs' folder, and enumerates all screenshot pairs properly.
7. Run 'write_raw_data_to_files.py'. This script identifies all instances of mulliganed cards ending up in the top three spots of the deck, and writes the results to the files in the 'raw_data' folder.
8. Run 'analyze_raw_data.py'. This script analyses the raw data, producing values for common metrics.

#### F. Explanation of Raw Data

The raw data is a series of digits, for which ever set of three digits contain exact information about a mulligan. E.g.:

  * '013' means the first card ended up outside of top three, the second ended up at the very top, and the third ended up in the third spot.

The raw data are written to four files with differing syntax:
1. 'raw_data' - '013002100'
2. 'raw_data_ls' - \['013', '002', '100'\]
3. 'raw_data_ll' - \[\[0, 1, 3\], \[0, 0, 2\], \[1, 0, 0\]\]
4. 'raw_data.csv' - Spreadsheet readable

#### G. Notes

The scripts are poorly optimized and will take quite a while to complete when used on large data sets.

The package includes the script 'mulligan_simulator.py' which can be run with parameters '1a', '1b', or '2', to calculate expected values for common metrics with respect to the mulligan implementation provided as parameter.

The package includes the script 'validate_accuracy.py' which can be run with parameters '0', '1', or '2', to calculate how far the Hammington Distance limit would have to be increased/reduced to produce false negatives/positives, for the respective modes. '0' is the mode identifying repeating mulligans. '1' is the mode identifying faulty screenshots. '2' is the mode identifying faulty mulligans. **Warning:** This script is *very* poorly optimized.


