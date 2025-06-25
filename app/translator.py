from googletrans import Translator

translator = Translator()

# src: source language code, dest: destination language code
def translate(text, src, dest):
    lang_map = {"English": "en", "Hindi": "hi", "Telugu": "te", "Tamil": "ta"}
    src_code = lang_map.get(src, "en")
    dest_code = lang_map.get(dest, "en")
    if src_code == dest_code:
        return text
    try:
        return translator.translate(text, src=src_code, dest=dest_code).text
    except Exception:
        return text 