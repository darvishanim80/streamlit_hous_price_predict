import streamlit as st
import folium
from streamlit_folium import st_folium
import json

st.set_page_config(layout="wide")
st.title("انتخاب موقعیت مکانی روی نقشه")

# مرکز نقشه را تنظیم کنید (مثلاً تهران)
map_center = [35.6892, 51.3890]
zoom_level = 12

# ایجاد یک نقشه folium
# در اینجا از `folium.Map` استفاده می‌کنیم.
# برای اینکه بتوانیم مختصات کلیک را دریافت کنیم، نیاز به تنظیماتی داریم.
# روش معمول این است که یک Event Listener در جاوااسکریپت داشته باشیم.
# streamlit-folium این کار را ساده می‌کند.

# ایجاد نقشه اولیه
m = folium.Map(location=map_center, zoom_start=zoom_level)

# --- قسمت مهم: دریافت مختصات کلیک ---
# `st_folium` نقشه را نمایش می‌دهد و اطلاعات حاصل از تعامل کاربر را برمی‌گرداند.
# پارامتر `key` برای اطمینان از اینکه Streamlit تعاملات را به درستی مدیریت می‌کند.
# پارامتر `height` و `width` برای تنظیم اندازه نقشه.
# پارامتر `returned_objects` مشخص می‌کند که چه داده‌هایی از تعامل کاربر برگردانده شود.
# ما به دنبال `last_clicked` هستیم که مختصات آخرین کلیک را می‌دهد.

# نمایش نقشه و دریافت نتیجه کلیک
# اگر کاربر هیچ کلیکی نکرده باشد، `clicked_location` برابر None خواهد بود.
clicked_location = st_folium(
    m,
    height=500,
    width=1000,
    key="map_click_interaction",
    returned_objects=["last_clicked"] # درخواست اطلاعات آخرین کلیک
)

# بررسی اینکه آیا کاربر کلیکی انجام داده است یا خیر
if clicked_location and clicked_location.get("last_clicked"):
    # استخراج مختصات Latitude و Longitude از نتیجه
    # `last_clicked` یک دیکشنری حاوی 'lat' و 'lng' است
    lat = clicked_location["last_clicked"]["lat"]
    lng = clicked_location["last_clicked"]["lng"]

    st.subheader("موقعیت انتخاب شده:")
    st.write(f"عرض جغرافیایی (Latitude): **{lat:.6f}**")
    st.write(f"طول جغرافیایی (Longitude): **{lng:.6f}**")

    # اختیاری: نمایش یک مارکر روی نقطه کلیک شده
    # برای این کار، باید نقشه را دوباره با مارکر اضافه شده رسم کنیم
    # یا اینکه `st_folium` بتواند مارکر را مستقیماً اضافه کند.
    # ساده‌ترین راه برای نمایش نقطه انتخاب شده، این است که دوباره نقشه را با آن مرکز و مارکر بسازیم.

    # ایجاد یک نقشه جدید با مرکزیت نقطه کلیک شده و اضافه کردن یک مارکر
    m_selected = folium.Map(location=[lat, lng], zoom_start=15)
    folium.Marker(
        location=[lat, lng],
        popup=f"مختصات: {lat:.6f}, {lng:.6f}",
        tooltip="نقطه انتخاب شده"
    ).add_to(m_selected)

    st.write("نقشه با نقطه انتخاب شده:") 
    st_folium(
        m_selected,
        height=400,
        width=1000,
        key="selected_location_map"
    )

    # شما می‌توانید این مختصات (lat, lng) را ذخیره کنید یا برای پردازش‌های بعدی استفاده کنید.
    # مثال: st.session_state["selected_lat"] = lat
    # مثال: st.session_state["selected_lng"] = lng

else:
    st.info("لطفاً روی نقشه کلیک کنید تا موقعیت مورد نظر خود را انتخاب کنید.")

st.markdown("---")
st.write("با کلیک بر روی نقشه بالا، مختصات جغرافیایی آن نقطه در کادر زیر نمایش داده می‌شود.")
