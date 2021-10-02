from brodcaster.bot import bot
from brodcaster.Utils import load_plugins
import logging
import glob
from pathlib import Path

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)


path = "brodcaster/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_plugins(shortname.replace(".py", ""))
print("wait...")
print("CONGRATS YOUR BOT DEPLOY SUCCESFULLY ENJOY 🤖💖🔥")
if __name__ == "__main__":
    bot.run_until_disconnected()
