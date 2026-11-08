from pathlib import Path
p = Path("android/app/src/main/AndroidManifest.xml")
s = p.read_text()
if "android.permission.INTERNET" not in s:
    s = s.replace("<application", "<uses-permission android:name=\"android.permission.INTERNET\" />\n    <application", 1)
if "android.software.leanback" not in s:
    s = s.replace("<application", "<uses-feature android:name=\"android.software.leanback\" android:required=\"false\" />\n    <uses-feature android:name=\"android.hardware.touchscreen\" android:required=\"false\" />\n    <application", 1)
if "usesCleartextTraffic" not in s:
    s = s.replace("<application", "<application android:usesCleartextTraffic=\"true\"", 1)
if "android.intent.category.LEANBACK_LAUNCHER" not in s:
    s = s.replace("<category android:name=\"android.intent.category.LAUNCHER\" />", "<category android:name=\"android.intent.category.LAUNCHER\" />\n                <category android:name=\"android.intent.category.LEANBACK_LAUNCHER\" />")
p.write_text(s)
