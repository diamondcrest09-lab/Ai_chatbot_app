[app]
# App details
title = AI Chatbot App
package.name = aichatbot
package.domain = org.example
version = 0.1

# Source files
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Requirements (keep it light!)
requirements = python3,kivy

# Orientation & display
orientation = portrait
fullscreen = 0

# Android settings
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# (Optional: if you want a custom icon, add it later)
# icon.filename = %(source.dir)s/data/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
