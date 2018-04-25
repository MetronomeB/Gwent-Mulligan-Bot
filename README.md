# Gwent-Mulligan-Bot

0a. Requirements
Windows 10 64-bit
Python 3.6+
AutoHotkey 1.1.28+

0b. Python dependencies
Pillow
dhash

0c. Gwent settings
Resolution = 1920x1080
Fullscreen = On
Graphics = Low
Vsync = Full
Antialising = Enabled
Premium cards = Off
Tooltips = Off
GOG Galaxy client = Off

1. Download the bot package and ensure compliance with all of step 0.

2. Create a deck with any Bronze specials and Calveit as leader, then exit Gwent.

3. Run 'gwent_mulligan_bot.ahk', and input the number of batches of 50 mulligans to sample.

4. Let the bot run to completion uninterrupted. Any key press - even moving the mouse cursor a single pixel - might cause the bot to de-sync.

5. Move all screenshots taken by the bot from 'C:\Users\<UserName>\Pictures\Screenshots' to the 'data' folder.

6. Run 'prepare_screenshot_pairs.py'. This script moves all faulty screenshot pairs to 'faulty_screenshot_pairs' and enumerates all screenshot pairs properly.

7. Run 'write_raw_data_to_files.py'. This script identifies all instances of mulliganed cards ending up in the top three spots of the deck, and writes the results to the file 'raw_data'.

8. Analyze/share the raw data. The file 'raw_data' now contains all mulligan info. Every set of three digits represents one mulligan sampling. Every digit represents the location the respective cards ended up in (0 = outside of top 3).
E.g. '013' = The first mulliganed card ended up outside of the deck's top three spots. The second ended up at the top spot, the third at the third spot.
