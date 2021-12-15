import defcon
import sys

font = defcon.Font(sys.argv[1])
font.lib["com.github.googlei18n.ufo2ft.featureWriters"] = []
font.save()

# note: you must also delete groups.plist and kerning.plist