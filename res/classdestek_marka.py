# Class Destek: hbb_common (alt modül) içindeki ad + sunucu + anahtar ayarı; CI'da checkout sonrası çalışır
import sys, pathlib
host = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] else "destek.classreklam.com"
p = pathlib.Path("libs/hbb_common/src/config.rs"); s = p.read_text(encoding="utf-8")
yeni = s.replace('RwLock::new("RustDesk".to_owned())', 'RwLock::new("ClassDestek".to_owned())', 1)
yeni = yeni.replace('&["rs-ny.rustdesk.com"]', '&["%s"]' % host, 1)
yeni = yeni.replace('"OeVuKk5nlHiXp+APNn0Y3pC1Iwpwn44JGqrQCsWqmBw="', '"wMHPTqwfT+YPyYNkhk500wdL4tzI8g6gbgvbQdPPNQw="', 1)
assert yeni.count("ClassDestek") == 1 and host in yeni and "wMHPTqwfT+YPyYNkhk500wdL4tzI8g6gbgvbQdPPNQw=" in yeni, "marka yamasi tutmadi"
p.write_text(yeni, encoding="utf-8"); print("marka tamam", host)
